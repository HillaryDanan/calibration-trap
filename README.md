# The Calibration Trap

**Epistemological Risks of Evaluative Feedback from Large Language Models**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## TL;DR

We tested whether LLMs agree with users regardless of position (sycophancy). **They do.**

| Model | Sycophancy Index | Effect Size | p-value |
|-------|------------------|-------------|---------|
| Claude (claude-sonnet-4-5) | 0.56 | d = 1.34 (large) | <0.0001 |
| GPT-5 (gpt-5.2) | 0.76 | d = 2.26 (large) | <0.0001 |
| Gemini (gemini-3-flash) | 0.66 | d = 1.73 (large) | <0.0001 |

When users say "I believe X," models align with X. When users say "I believe NOT X," models shift toward NOT X. All three frontier models. Large effects. Replicated across pilot (n=10) and full study (n=50).

**Adversarial prompting ("give me objections") did not help.** Effect was null or slightly negative.

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

## Results

### H1: Sycophancy — Confirmed

All three models show statistically significant sycophancy with large effect sizes (d > 1.3). Results replicated from pilot to full study.

### H2: Adversarial Mitigation — Not Supported

Asking for "strongest objections" did not increase critical content:

| Model | Neutral | Adversarial | Difference |
|-------|---------|-------------|------------|
| Claude | 0.622 | 0.594 | -0.027 |
| Gemini | 0.608 | 0.592 | -0.016 |

The proposed mitigation does not work in this paradigm.

---

## Method

**Design**: Within-stimulus comparison. Same claim presented with pro vs. con user framing.

**Measure**: Semantic similarity (OpenAI text-embedding-3-large). 

```
Alignment Score = Sim(response, pro_justification) - Sim(response, con_justification)
Sycophancy Index = correlation(user_framing, alignment_score)
```

**Sample**: 10 controversial stimuli across economics, AI, psychology, policy, technology. Full study n=50 per condition (382 valid trials after API failures).

---

## Limitations

1. **Semantic similarity ≠ agreement** — Embedding alignment is a proxy.
2. **API failure rate** — 36% of trials failed (primarily GPT-5 in some conditions).
3. **No human outcomes** — Tests LLM behavior, not effects on human beliefs.
4. **10 stimuli** — May not generalize across all domains.

---

## Replicate

```bash
git clone https://github.com/HillaryDanan/calibration-trap.git
cd calibration-trap
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Add API keys

python3 src/run_experiment.py --n 50
python3 src/analyze.py
```

---

## References

Perez, E., et al. (2022). Discovering language model behaviors with model-written evaluations. *arXiv:2212.09251*.

Sharma, M., et al. (2023). Towards understanding sycophancy in language models. *arXiv:2310.13548*.

---

## Author

**Hillary Danan**

*AI assistance: Claude (Anthropic). Author takes full responsibility for content and errors.*

*Disclosure: Claude showed sycophancy (SI=0.56) in this study.*
