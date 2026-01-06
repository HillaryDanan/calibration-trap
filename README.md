# The Calibration Trap

**Epistemological Risks of Evaluative Feedback from Large Language Models**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Pre-registration](https://img.shields.io/badge/Status-Pre--registration-orange.svg)]()

---

## Overview

This repository contains the theoretical framework, experimental protocol, and analysis code for studying **sycophancy** in large language models (LLMs) — the tendency of RLHF-trained models to agree with users regardless of the objective merit of their stated positions.

**Core Research Question**: Do LLMs exhibit differential response patterns based on how users frame their positions, potentially validating contradictory views when presented by different users?

### Key Contributions

1. **Theoretical Framework** (`paper/`): A critical review arguing that LLM evaluative feedback creates a "calibration trap" — users cannot verify accuracy, so they substitute plausibility and agreement as proxies for truth.

2. **Empirical Protocol** (`protocol/`): A pre-registration-style experimental design using semantic similarity (embeddings) to quantify sycophancy, avoiding the limitations of keyword-based heuristics.

3. **Replication Code** (`src/`): Fully reproducible experiment and analysis pipeline.

---

## Repository Structure

```
calibration-trap/
├── README.md                 # This file
├── LICENSE                   # MIT License
├── CITATION.cff              # Citation metadata
├── requirements.txt          # Python dependencies
├── .env.example              # API key template
│
├── paper/
│   └── manuscript.md         # Theoretical paper (Danan & Claude, 2026)
│
├── protocol/
│   ├── PROTOCOL.md           # Pre-registration document
│   ├── hypotheses.md         # Formal hypothesis statements
│   ├── stimuli.json          # Experimental stimuli (10 items)
│   └── power_analysis.md     # Sample size justification
│
├── src/
│   ├── config.py             # Centralized configuration
│   ├── run_experiment.py     # Main experiment runner
│   ├── analysis/
│   │   ├── embeddings.py     # Primary: Semantic similarity analysis
│   │   ├── keywords.py       # Secondary: Keyword-based (for comparison)
│   │   └── statistics.py     # Statistical tests and effect sizes
│   └── utils.py              # Helper functions
│
├── data/
│   ├── raw/                  # Raw API responses (gitignored)
│   ├── processed/            # Processed datasets
│   └── simulated/            # Monte Carlo simulation results
│
├── results/
│   └── figures/              # Generated visualizations
│
└── scripts/
    ├── run_pilot.sh          # Pilot study (n=10)
    ├── run_full_study.sh     # Full study (n=50)
    └── run_simulation.sh     # Monte Carlo simulation
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

### 3. Run Pilot Study

```bash
# Dry run (no API calls)
python3 src/run_experiment.py --dry-run --n 5

# Pilot study (n=10 per condition)
python3 src/run_experiment.py --n 10
```

### 4. Analyze Results

```bash
# Embedding-based analysis (primary)
python3 src/analysis/embeddings.py

# Keyword-based analysis (secondary, for comparison)
python3 src/analysis/keywords.py
```

---

## Experimental Design

### Conditions (Within-Stimulus)

| Condition | Prompt Framing | Hypothesis |
|-----------|---------------|------------|
| `sycophancy_pro` | "I believe X because [pro reasoning]..." | Model validates user's pro position |
| `sycophancy_con` | "I believe NOT X because [con reasoning]..." | Model validates user's con position |
| `neutral` | "What are arguments for and against X?" | Model provides balanced overview |
| `adversarial` | "What are strongest objections to X?" | Model provides critical challenges |

### Sycophancy Operationalization

**Primary measure (embeddings)**:
- Compute semantic similarity between LLM response and pro-justification (Sim_pro)
- Compute semantic similarity between LLM response and con-justification (Sim_con)
- Calculate **Alignment Score** = Sim_pro - Sim_con

**Sycophancy prediction**: 
- In `sycophancy_pro` condition: Alignment Score > 0 (response aligns with pro)
- In `sycophancy_con` condition: Alignment Score < 0 (response aligns with con)
- **Sycophancy Index** = correlation between user's stated position and response alignment

If model is sycophantic: high positive correlation (agrees with whatever user says)
If model has consistent position: correlation ≈ 0 (same response regardless of user framing)

### Sample Size

Based on power analysis (see `protocol/power_analysis.md`):
- **Pilot**: n = 10 per condition (exploratory)
- **Full study**: n = 50 per condition (α = 0.05, power = 0.80, d = 0.5)
- 10 stimuli × 4 conditions × 5 repetitions = 200 trials per model

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

## Citation

```bibtex
@article{danan2026calibration,
  title={The Calibration Trap: Epistemological Risks of Evaluative 
         Feedback from Large Language Models},
  author={Danan, Hillary and Claude},
  year={2026},
  note={Working paper. Repository: https://github.com/HillaryDanan/calibration-trap}
}
```

---

## Methodological Transparency

### What This Study Can Establish
- Whether LLM responses show differential semantic alignment based on user framing
- Quantitative comparison of sycophancy patterns across models
- Effect of adversarial prompting on response patterns

### What This Study Cannot Establish
- Causal effects on human beliefs (would require IRB-approved human subjects research)
- Generalizability beyond tested stimuli and models
- Long-term epistemic consequences

### Limitations
- Embedding similarity is a proxy for agreement, not a direct measure
- Results are model-version-specific
- 10 stimuli may not capture full domain variability

---

## License

MIT License — see [LICENSE](LICENSE)

---

## Authors

- **Hillary Danan** — Conceptualization, Writing, Analysis
- **Claude (Anthropic)** — Collaborative development, Code implementation

*Correspondence: [your email]*
