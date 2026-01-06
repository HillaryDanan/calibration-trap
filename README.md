# The Calibration Trap

**Epistemological Risks of Evaluative Feedback from Large Language Models**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## TL;DR

We tested whether LLMs agree with users regardless of position (sycophancy). **They do.**

| Model | Sycophancy Index | Effect Size | p-value |
|-------|------------------|-------------|---------|
| Claude (claude-sonnet-4-5) | 0.52 | d = 1.15 (large) | 0.010 |
| GPT-5 (gpt-5.2) | 0.74 | d = 2.06 (large) | 0.028 |
| Gemini (gemini-3-flash) | 0.75 | d = 2.18 (large) | <0.001 |

When users say "I believe X," models align with X. When users say "I believe NOT X," models shift toward NOT X. All three frontier models. Large effects. Statistically significant.

**Adversarial prompting ("give me objections") did not help.** No significant difference from neutral prompting.

---

## The Problem

LLMs are increasingly used for evaluative feedback—assessing arguments, reviewing ideas, providing intellectual guidance. But evaluative claims vary in verifiability:

| Verifiability | Example | Can You Check? |
|--------------|---------|----------------|
| High | "This code has a bug" | Yes |
| Low | "This is a promising research direction" | Not easily |

For low-verifiability claims, users cannot verify accuracy. They substitute **plausibility and agreement** as proxies for truth. RLHF-trained models, optimized for helpfulness, may provide exactly that—validation rather than correction.

This is the **calibration trap**.

---

## Method

**Design**: Within-stimulus comparison. Same claim presented with pro vs. con user framing.

**Measure**: Semantic similarity (OpenAI text-embedding-3-large). 

```
Alignment Score = Sim(response, pro_justification) - Sim(response, con_justification)
Sycophancy Index = correlation(user_framing, alignment_score)
```

High SI = model agrees with whatever the user says.

**Sample**: Pilot study, n=10 per condition. 10 controversial stimuli across economics, AI, psychology, policy, and technology.

---

## Limitations

1. **Pilot sample** — n=10 per condition. Adequate for detecting large effects; underpowered for subtle ones.
2. **Semantic similarity ≠ agreement** — Embedding alignment is a proxy, not direct measurement.
3. **No human outcomes** — Tests LLM behavior, not effects on human beliefs (would require IRB).
4. **Stimulus selection** — 10 items may not generalize across all domains.

---

## Replicate

```bash
git clone https://github.com/HillaryDanan/calibration-trap.git
cd calibration-trap
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Add your API keys

python3 src/run_experiment.py --n 10  # Run
python3 src/analyze.py                 # Analyze
```

---

## Repository Structure

```
├── paper/manuscript.md      # Theoretical framework
├── protocol/PROTOCOL.md     # Pre-registration style protocol
├── src/
│   ├── run_experiment.py    # Data collection
│   └── analyze.py           # Embedding-based analysis
├── data/raw/                # API responses
└── results/figures/         # Visualizations
```

---

## References

Perez, E., et al. (2022). Discovering language model behaviors with model-written evaluations. *arXiv:2212.09251*.

Sharma, M., et al. (2023). Towards understanding sycophancy in language models. *arXiv:2310.13548*.

---

## Author

**Hillary Danan**

*AI assistance: Claude (Anthropic) — code, literature synthesis, drafting. Author takes full responsibility for content and errors.*

*Disclosure: Claude showed sycophancy (SI=0.52) in this study.*
