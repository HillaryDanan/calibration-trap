#!/usr/bin/env python3
"""
Protocol A: Main Experiment Runner
==================================

Runs the sycophancy study across specified models and conditions.

Usage:
    python3 src/run_experiment.py --dry-run --n 5
    python3 src/run_experiment.py --model claude --n 10
    python3 src/run_experiment.py --n 50  # Full study
"""

import json
import time
import argparse
import hashlib
from datetime import datetime
from pathlib import Path

from config import (
    MODELS, CONDITIONS, PROMPT_TEMPLATES, STIMULI_PATH,
    RAW_DIR, REQUEST_DELAY, RANDOM_SEED, get_api_key
)

# =============================================================================
# API CLIENTS
# =============================================================================

def get_anthropic_client():
    from anthropic import Anthropic
    return Anthropic(api_key=get_api_key('anthropic'))

def get_openai_client():
    from openai import OpenAI
    return OpenAI(api_key=get_api_key('openai'))

def get_gemini_client():
    from google import genai
    return genai.Client(api_key=get_api_key('google'))

# =============================================================================
# API CALLS
# =============================================================================

def call_claude(client, prompt: str, config: dict) -> dict:
    try:
        msg = client.messages.create(
            model=config['name'],
            max_tokens=config['max_tokens'],
            messages=[{"role": "user", "content": prompt}]
        )
        return {
            'success': True,
            'response': msg.content[0].text,
            'input_tokens': msg.usage.input_tokens,
            'output_tokens': msg.usage.output_tokens
        }
    except Exception as e:
        return {'success': False, 'error': str(e), 'response': None}

def call_gpt(client, prompt: str, config: dict) -> dict:
    try:
        comp = client.chat.completions.create(
            model=config['name'],
            messages=[{"role": "user", "content": prompt}],
            max_tokens=config['max_tokens']
        )
        return {
            'success': True,
            'response': comp.choices[0].message.content,
            'input_tokens': comp.usage.prompt_tokens,
            'output_tokens': comp.usage.completion_tokens
        }
    except Exception as e:
        return {'success': False, 'error': str(e), 'response': None}

def call_gemini(client, prompt: str, config: dict) -> dict:
    try:
        resp = client.models.generate_content(
            model=config['name'],
            contents=prompt
        )
        return {
            'success': True,
            'response': resp.text,
            'input_tokens': getattr(getattr(resp, 'usage_metadata', None), 'prompt_token_count', None),
            'output_tokens': getattr(getattr(resp, 'usage_metadata', None), 'candidates_token_count', None)
        }
    except Exception as e:
        return {'success': False, 'error': str(e), 'response': None}

# =============================================================================
# TRIAL GENERATION
# =============================================================================

def load_stimuli() -> list:
    """Load stimuli from JSON file."""
    with open(STIMULI_PATH) as f:
        data = json.load(f)
    return data['stimuli']

def generate_trials(n_per_condition: int) -> list:
    """Generate trial list for experiment."""
    stimuli = load_stimuli()
    trials = []
    trial_id = 0
    
    for condition in CONDITIONS:
        for i in range(n_per_condition):
            stim = stimuli[i % len(stimuli)]
            template = PROMPT_TEMPLATES[condition]
            
            # Build prompt based on condition
            if condition == "sycophancy_pro":
                prompt = template.format(
                    statement=stim['statement'],
                    justification_pro=stim['justification_pro']
                )
            elif condition == "sycophancy_con":
                prompt = template.format(
                    statement=stim['statement'],
                    justification_con=stim['justification_con']
                )
            else:
                prompt = template.format(statement=stim['statement'])
            
            trials.append({
                'trial_id': f"T{trial_id:04d}",
                'stimulus_id': stim['id'],
                'domain': stim['domain'],
                'statement': stim['statement'],
                'pro_justification': stim['justification_pro'],
                'con_justification': stim['justification_con'],
                'condition': condition,
                'prompt': prompt,
                'prompt_hash': hashlib.md5(prompt.encode()).hexdigest()[:8]
            })
            trial_id += 1
    
    return trials

# =============================================================================
# MAIN EXPERIMENT
# =============================================================================

def run_experiment(models_to_run: list, n_per_condition: int, dry_run: bool = False):
    """Run the experiment."""
    
    trials = generate_trials(n_per_condition)
    total_calls = len(trials) * len(models_to_run)
    
    # Display info
    print("=" * 70)
    print("PROTOCOL A: SYCOPHANCY STUDY")
    print("=" * 70)
    print(f"\nDESIGN:")
    print(f"  Conditions: {', '.join(CONDITIONS)}")
    print(f"  Stimuli: {len(load_stimuli())}")
    print(f"  Trials per condition: {n_per_condition}")
    print(f"  Total trials per model: {len(trials)}")
    print(f"\nMODELS: {', '.join(models_to_run)}")
    print(f"TOTAL API CALLS: {total_calls}")
    print(f"ESTIMATED TIME: {total_calls * REQUEST_DELAY / 60:.1f} min")
    print(f"DRY RUN: {dry_run}")
    print("=" * 70)
    
    if not dry_run:
        confirm = input("\n⚠️  Continue? [y/N]: ")
        if confirm.lower() != 'y':
            print("Aborted.")
            return
    
    # Initialize clients
    clients = {}
    call_funcs = {'claude': call_claude, 'gpt5': call_gpt, 'gemini': call_gemini}
    client_funcs = {'claude': get_anthropic_client, 'gpt5': get_openai_client, 'gemini': get_gemini_client}
    
    for model_key in models_to_run:
        if dry_run:
            clients[model_key] = None
        else:
            try:
                clients[model_key] = client_funcs[model_key]()
                print(f"✓ {model_key} initialized")
            except Exception as e:
                print(f"✗ {model_key}: {e}")
                clients[model_key] = None
    
    # Run experiment
    results = {
        'metadata': {
            'timestamp': datetime.now().isoformat(),
            'models': models_to_run,
            'n_per_condition': n_per_condition,
            'total_trials': len(trials),
            'dry_run': dry_run,
            'random_seed': RANDOM_SEED
        },
        'trials': []
    }
    
    call_count = 0
    for model_key in models_to_run:
        config = MODELS[model_key]
        client = clients.get(model_key)
        
        if client is None and not dry_run:
            print(f"\n⚠️  Skipping {model_key}")
            continue
        
        print(f"\n{'─'*70}")
        print(f"MODEL: {model_key.upper()} ({config['name']})")
        print(f"{'─'*70}")
        
        for trial in trials:
            call_count += 1
            pct = call_count / total_calls * 100
            print(f"\r[{call_count}/{total_calls}] ({pct:.0f}%) {trial['condition'][:12]:12} | {trial['stimulus_id']}", 
                  end="", flush=True)
            
            result = {
                'model': model_key,
                'model_name': config['name'],
                **trial,
                'timestamp': datetime.now().isoformat()
            }
            
            if dry_run:
                result['response'] = "[DRY RUN]"
                result['success'] = True
                result['dry_run'] = True
            else:
                api_result = call_funcs[model_key](client, trial['prompt'], config)
                result.update(api_result)
                time.sleep(REQUEST_DELAY)
            
            results['trials'].append(result)
        
        print()
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    models_str = "_".join(models_to_run)
    filename = f"experiment_{models_str}_n{n_per_condition}_{timestamp}.json"
    output_path = RAW_DIR / filename
    
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Summary
    success = sum(1 for t in results['trials'] if t.get('success'))
    failed = sum(1 for t in results['trials'] if not t.get('success'))
    
    print("\n" + "=" * 70)
    print("COMPLETE")
    print("=" * 70)
    print(f"Success: {success}, Failed: {failed}")
    print(f"Output: {output_path}")
    print(f"\nNext: python3 src/analysis/embeddings.py --file {filename}")

# =============================================================================
# CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description='Run sycophancy study')
    parser.add_argument('--model', choices=['claude', 'gpt5', 'gemini', 'all'],
                        default='all')
    parser.add_argument('--n', type=int, default=50,
                        help='Trials per condition')
    parser.add_argument('--dry-run', action='store_true')
    
    args = parser.parse_args()
    models = ['claude', 'gpt5', 'gemini'] if args.model == 'all' else [args.model]
    
    run_experiment(models, args.n, args.dry_run)

if __name__ == "__main__":
    main()
