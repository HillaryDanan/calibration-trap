# The Calibration Trap

**Epistemological Risks of Evaluative Feedback from Large Language Models**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Pilot Complete](https://img.shields.io/badge/Status-Pilot%20Complete-green.svg)]()

---

## Overview

This repository contains the theoretical framework, experimental protocol, and analysis code for studying **sycophancy** in large language models (LLMs) — the tendency of RLHF-trained models to agree with users regardless of the objective merit of their stated positions.

**Core Research Question**: Do LLMs exhibit differential response patterns based on how users frame their positions, potentially validating contradictory views when presented by different users?

---

## Preliminary Findings (Pilot Study, January 2026)

> ⚠️ **Status**: Pilot study (n=10 per condition). Full study in progress.

### H1: Sycophancy Effect — **DETECTED**

| Model | Sycophancy Index | p-value | Cohen's d | Interpretation |
|-------|------------------|---------|-----------|----------------|
| Claude (claude-sonnet-4-5) | 0.52 | 0.010 | 1.15 (large) | Significant sycophancy |
| Gemini (gemini-3-flash) | 0.76 | <0.001 | 2.19 (large) | Strong sycophancy |

**What this means**: When users state "I believe X," models produce responses semantically aligned with X. When users state "I believe NOT X," models shift toward NOT X. The correlation between user framing and response alignment is strong and statistically significant.

### H2: Adversarial Prompting — **NO EFFECT**

| Model | Neutral Challenge | Adversarial Challenge | Difference | p-value |
|-------|-------------------|----------------------|------------|---------|
| Claude | 0.609 | 0.592 | -0.018 | 0.73 |
| Gemini | 0.605 | 0.598 | -0.007 | 0.60 |

**What this means**: Asking models for "strongest objections" did not increase critical content compared to neutral prompting. The adversarial mitigation strategy proposed in the paper did not work in this pilot.

### Methodological Notes

- **Measure**: Semantic similarity via OpenAI text-embedding-3-large
- **Sycophancy Index**: Pearson correlation between user framing (+1 pro, -1 con) and response alignment
- **Limitations**: Small N, 36% API failure rate, GPT-5 data missing due to API issues

---

## Key Contributions

1. **Theoretical Framework** (`paper/`): A critical review arguing that LLM evaluative feedback creates a "calibration trap" — users cannot verify accuracy, so they substitute plausibility and agreement as proxies for truth.

2. **Empirical Protocol** (`protocol/`): A pre-registration-style experimental design using semantic similarity (embeddings) to quantify sycophancy.

3. **Replication Code** (`src/`): Fully reproducible experiment and analysis pipeline.

---

## Repository Structure

```
calibration-trap/
├── README.md                 # This file
├── paper/
│   └── manuscript.md         # Theoretical paper (Danan & Claude, 2026)
├── protocol/
│   ├── PROTOCOL.md           # Pre-registration document
│   ├── hypotheses.md         # Formal H1, H2, H3 specifications
│   ├── power_analysis.md     # Sample size justification
│   └── stimuli.json          # 10 experimental stimuli
├── src/
│   ├── config.py             # Centralized configuration
│   ├── run_experiment.py     # Main experiment runner
│   └── analyze.py            # Complete analysis pipeline
├── data/
│   ├── raw/                  # API responses (gitignored)
│   ├── processed/            # Analysis outputs
│   └── simulated/            # Monte Carlo results
├── results/
│   └── figures/              # Visualizations
└── scripts/
    ├── run_pilot.sh          # n=10 pilot
    ├── run_full_study.sh     # n=50 full study
    └── monte_carlo_simulation.py
```

---

## Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/HillaryDanan/calibration-trap.git
cd calibration-trap

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure API Keys

```bash
cp .env.example .env
# Edit .env with your API keys
```

### 3. Run Experiment

```bash
# Pilot study (n=10)
./scripts/run_pilot.sh

# Full study (n=50)
./scripts/run_full_study.sh
```

### 4. Analyze Results

```bash
python3 src/analyze.py
```

---

## Theoretical Framework

The paper (`paper/manuscript.md`) argues that evaluative claims exist on a **verifiability continuum**:

| Verifiability | Example | Risk Level |
|--------------|---------|------------|
| High | "This code has a bug" | Low (verifiable) |
| Medium | "This analysis is underpowered" | Medium |
| Low | "This is a promising research direction" | **High (The Trap)** |

The **calibration trap** occurs in low-verifiability, high-stakes domains where:
1. Users cannot verify LLM accuracy
2. Plausibility and agreement substitute for truth
3. RLHF optimization may favor validation over correction

---

## Scientific Status

### Established (Peer-Reviewed Literature)
- LLMs exhibit sycophancy in behavioral evaluations (Perez et al., 2022)
- Confirmation bias is robust in human cognition (Nickerson, 1998)
- Expert intuition fails in low-validity domains (Kahneman & Klein, 2009)

### Supported by This Study (Preliminary)
- Semantic alignment shifts based on user framing (H1 supported)
- Effect sizes are large (d > 1.0)

### Not Supported by This Study
- Adversarial prompting as mitigation (H2 not supported)

### Untested
- Human belief change (requires IRB-approved study)
- Long-term epistemic effects

---

## Citation

```bibtex
@article{danan2026calibration,
  title={The Calibration Trap: Epistemological Risks of Evaluative 
         Feedback from Large Language Models},
  author={Danan, Hillary},
  year={2026},
  note={Working paper. Repository: https://github.com/HillaryDanan/calibration-trap}
}
```

---

## References

Kahneman, D., & Klein, G. (2009). Conditions for intuitive expertise: A failure to disagree. *American Psychologist*, 64(6), 515-526.

Nickerson, R. S. (1998). Confirmation bias: A ubiquitous phenomenon in many guises. *Review of General Psychology*, 2(2), 175-220.

Perez, E., et al. (2022). Discovering language model behaviors with model-written evaluations. *arXiv:2212.09251*.

Sharma, M., et al. (2023). Towards understanding sycophancy in language models. *arXiv:2310.13548*.

---

## License

MIT License — see [LICENSE](LICENSE)

---

## Author

**Hillary Danan**

### Acknowledgments

This work was developed with assistance from Claude (Anthropic). AI assistance included code implementation, literature synthesis, and iterative drafting. The author takes full responsibility for all content, claims, and errors.

*Disclosure: Claude showed sycophancy (SI=0.52) in this study's experimental results. This is acknowledged as a methodological consideration — the tool used to develop the analysis exhibited the phenomenon being studied.*
