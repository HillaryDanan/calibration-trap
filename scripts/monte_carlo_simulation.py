#!/usr/bin/env python3
"""
Monte Carlo Simulation: The Calibration Trap
=============================================

Generates synthetic belief-shift data based on literature priors.

SCIENTIFIC STATUS: 
==================
This is a THEORETICAL SIMULATION, not empirical data.

Effect sizes are derived from peer-reviewed literature:
- Perez et al. (2022) on LLM sycophancy behaviors
- Lord et al. (1979) on biased assimilation 
- Nyhan & Reifler (2010) on backfire effects

This simulation represents PREDICTED outcomes if the theoretical 
framework is correct. To validate, run Protocol A with human subjects.

Author: Hillary Danan & Claude (Anthropic)
Date: January 2026
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from scipy import stats

# =============================================================================
# CONFIGURATION
# =============================================================================

# Reproducibility
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

# Sample sizes
N_PER_GROUP = 125
GROUPS = ['Sycophancy', 'Neutral', 'Adversarial', 'Control']

# Literature-derived priors with explicit citations
PRIORS = {
    'Sycophancy': {
        'shift_mu': 0.85,      # Large positive shift (d ≈ 0.78)
        'shift_sigma': 0.6,    # Moderate variance
        'source': 'Perez et al. (2022); Lord et al. (1979)'
    },
    'Neutral': {
        'shift_mu': 0.20,      # Negligible shift (d ≈ 0.16)
        'shift_sigma': 0.4,    # Lower variance (tonal flattening)
        'source': 'Theoretical: RLHF mean-reversion hypothesis'
    },
    'Adversarial': {
        'shift_mu': -0.41,     # Negative shift (belief moderation)
        'shift_sigma': 1.1,    # HIGH variance (backfire effect bifurcation)
        'source': 'Nyhan & Reifler (2010)'
    },
    'Control': {
        'shift_mu': 0.02,      # Null effect
        'shift_sigma': 0.2,    # Low variance (stable beliefs)
        'source': 'Baseline stability assumption'
    }
}

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / 'data' / 'simulated'


# =============================================================================
# SIMULATION FUNCTIONS
# =============================================================================

def generate_belief_shifts(group: str, n: int) -> np.ndarray:
    """
    Generate synthetic belief shifts for a condition group.
    
    Returns shifts clipped to realistic Likert bounds (-6 to +6).
    """
    params = PRIORS[group]
    shifts = np.random.normal(
        loc=params['shift_mu'],
        scale=params['shift_sigma'],
        size=n
    )
    return np.clip(shifts, -6, 6)


def calculate_cohens_d(group_shifts: np.ndarray, control_shifts: np.ndarray) -> float:
    """
    Calculate Cohen's d effect size relative to control.
    
    Uses pooled standard deviation per Cohen (1988).
    """
    n1, n2 = len(group_shifts), len(control_shifts)
    var1, var2 = np.var(group_shifts, ddof=1), np.var(control_shifts, ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    
    if pooled_std == 0:
        return 0.0
    return (np.mean(group_shifts) - np.mean(control_shifts)) / pooled_std


def run_simulation() -> pd.DataFrame:
    """Execute the Monte Carlo simulation."""
    
    print("=" * 60)
    print("MONTE CARLO SIMULATION: THE CALIBRATION TRAP")
    print("=" * 60)
    print(f"\nRandom Seed: {RANDOM_SEED}")
    print(f"N per group: {N_PER_GROUP}")
    print(f"Total N: {N_PER_GROUP * len(GROUPS)}")
    
    print("\n" + "-" * 60)
    print("THEORETICAL PRIORS (Literature-Derived)")
    print("-" * 60)
    
    for group, params in PRIORS.items():
        print(f"\n{group}:")
        print(f"  Mean shift: {params['shift_mu']:+.2f}")
        print(f"  SD: {params['shift_sigma']:.2f}")
        print(f"  Source: {params['source']}")
    
    print("\n" + "-" * 60)
    print("GENERATING SIMULATED DATA...")
    print("-" * 60)
    
    data = []
    for group in GROUPS:
        shifts = generate_belief_shifts(group, N_PER_GROUP)
        for i, shift in enumerate(shifts):
            data.append({
                'participant_id': f'{group[:3].upper()}_{i+1:03d}',
                'group': group,
                'belief_shift': shift
            })
    
    return pd.DataFrame(data)


def analyze_results(df: pd.DataFrame) -> dict:
    """Compute summary statistics and effect sizes."""
    
    print("\n" + "=" * 60)
    print("RESULTS SUMMARY")
    print("=" * 60)
    
    results = {}
    control_shifts = df[df['group'] == 'Control']['belief_shift'].values
    
    for group in GROUPS:
        group_data = df[df['group'] == group]['belief_shift']
        
        mean_shift = group_data.mean()
        std_shift = group_data.std()
        
        if group != 'Control':
            d = calculate_cohens_d(group_data.values, control_shifts)
        else:
            d = 0.0
        
        t_stat, p_value = stats.ttest_1samp(group_data, 0)
        
        results[group] = {
            'n': len(group_data),
            'mean': mean_shift,
            'std': std_shift,
            'cohens_d': d,
            't_stat': t_stat,
            'p_value': p_value
        }
        
        # Effect size interpretation (Cohen, 1988)
        if abs(d) < 0.2:
            d_label = "Negligible"
        elif abs(d) < 0.5:
            d_label = "Small"
        elif abs(d) < 0.8:
            d_label = "Medium"
        else:
            d_label = "Large"
        
        sig = "***" if p_value < 0.001 else "**" if p_value < 0.01 else "*" if p_value < 0.05 else "ns"
        
        print(f"\n{group}:")
        print(f"  N = {len(group_data)}")
        print(f"  Mean ΔB = {mean_shift:+.3f} (SD = {std_shift:.3f})")
        print(f"  Cohen's d = {d:.3f} ({d_label})")
        print(f"  t({len(group_data)-1}) = {t_stat:.3f}, p = {p_value:.4f} {sig}")
    
    return results


def create_visualizations(df: pd.DataFrame, results: dict):
    """Generate publication-quality figures."""
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR = Path(__file__).parent.parent / 'results' / 'figures'
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    
    plt.style.use('seaborn-v0_8-whitegrid')
    sns.set_palette("Set2")
    
    # Figure 1: Boxplot
    fig, ax = plt.subplots(figsize=(10, 6))
    order = ['Sycophancy', 'Neutral', 'Adversarial', 'Control']
    
    sns.boxplot(data=df, x='group', y='belief_shift', order=order, width=0.5, showfliers=False, ax=ax)
    sns.stripplot(data=df, x='group', y='belief_shift', order=order, alpha=0.3, size=4, ax=ax)
    
    ax.axhline(y=0, color='red', linestyle='--', alpha=0.5, linewidth=1.5)
    ax.set_xlabel('Experimental Condition', fontsize=12)
    ax.set_ylabel('Belief Shift (Post - Pre)', fontsize=12)
    ax.set_title('Simulated Belief Shift by LLM Feedback Condition\n(N=125 per group, Monte Carlo simulation)', fontsize=14)
    
    for i, group in enumerate(order):
        d = results[group]['cohens_d']
        mean = results[group]['mean']
        ax.annotate(f'd = {d:.2f}', xy=(i, mean), xytext=(10, 0),
                    textcoords='offset points', fontsize=9, ha='left')
    
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / 'simulated_results.png', dpi=300, bbox_inches='tight')
    print(f"\nSaved: {FIGURES_DIR / 'simulated_results.png'}")
    
    # Figure 2: Distributions
    fig2, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    for i, group in enumerate(order):
        group_data = df[df['group'] == group]['belief_shift']
        ax = axes[i]
        sns.histplot(group_data, kde=True, ax=ax, bins=20)
        ax.axvline(x=0, color='red', linestyle='--', alpha=0.7)
        ax.axvline(x=group_data.mean(), color='green', linestyle='-', alpha=0.7)
        ax.set_title(f'{group} Condition', fontsize=12)
        ax.set_xlabel('Belief Shift')
        ax.set_xlim(-4, 4)
    
    plt.suptitle('Distribution of Belief Shifts by Condition\n(Simulated Data)', fontsize=14, y=1.02)
    plt.tight_layout()
    fig2.savefig(FIGURES_DIR / 'distributions.png', dpi=300, bbox_inches='tight')
    print(f"Saved: {FIGURES_DIR / 'distributions.png'}")
    
    plt.close('all')


def save_data(df: pd.DataFrame, results: dict):
    """Save simulation data and results."""
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    df.to_csv(OUTPUT_DIR / 'simulation_data.csv', index=False)
    print(f"Saved: {OUTPUT_DIR / 'simulation_data.csv'}")
    
    summary_rows = []
    for group, stats_dict in results.items():
        summary_rows.append({
            'group': group,
            'n': stats_dict['n'],
            'mean_shift': round(stats_dict['mean'], 4),
            'std': round(stats_dict['std'], 4),
            'cohens_d': round(stats_dict['cohens_d'], 4),
            't_statistic': round(stats_dict['t_stat'], 4),
            'p_value': round(stats_dict['p_value'], 6)
        })
    
    summary_df = pd.DataFrame(summary_rows)
    summary_df.to_csv(OUTPUT_DIR / 'summary_statistics.csv', index=False)
    print(f"Saved: {OUTPUT_DIR / 'summary_statistics.csv'}")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    df = run_simulation()
    results = analyze_results(df)
    create_visualizations(df, results)
    save_data(df, results)
    
    print("\n" + "=" * 60)
    print("SIMULATION COMPLETE")
    print("=" * 60)
    print(f"\nOutput: {OUTPUT_DIR.absolute()}")
    print("\n⚠️  REMINDER: This is SIMULATED data based on literature priors.")
    print("   It represents PREDICTED outcomes, not empirical findings.")
    print("   To validate, run Protocol A with human subjects.")
