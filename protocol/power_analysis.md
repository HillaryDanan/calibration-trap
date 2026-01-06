# Power Analysis

## Overview

This document justifies the sample size for Protocol A.

## Target Effect Size

Based on prior work:
- Perez et al. (2022) found moderate-to-large sycophancy effects (d ≈ 0.5-0.8)
- Sharma et al. (2023) found smaller effects in some conditions (d ≈ 0.3-0.5)

**Conservative estimate**: d = 0.5 (medium effect)

## Power Parameters

- α = 0.05 (one-tailed for H1 and H2)
- Power = 0.80 (conventional threshold)
- Effect size = 0.5 (Cohen's d)

## Sample Size Calculation

### For H1 (One-sample t-test on Sycophancy Index)

Using G*Power or equivalent:
- One-sample t-test, one-tailed
- d = 0.5, α = 0.05, power = 0.80
- **Required n = 27 per group**

However, the Sycophancy Index is computed as a correlation across trials, so we need sufficient trials to estimate this reliably.

### For Within-Stimulus Comparison

Each stimulus is tested in both pro and con conditions. With:
- 10 stimuli
- 5 repetitions per stimulus per condition
- = 50 trials per condition per model

This provides:
- 50 paired observations for computing Alignment Score differences
- Robust estimation of Sycophancy Index

### For H2 (Paired t-test on Challenge Score)

- Paired t-test, one-tailed
- d = 0.5, α = 0.05, power = 0.80
- **Required n = 27 pairs**

With 50 trials in adversarial and 50 in neutral, we have adequate power.

### For H3 (ANOVA across 3 models)

- One-way ANOVA, 3 groups
- f = 0.25 (medium effect), α = 0.05, power = 0.80
- **Required total n = 159 (53 per group)**

With Sycophancy Index computed per model (one value per model), we cannot do traditional ANOVA. Instead, we will use bootstrapped confidence intervals to compare models.

## Final Sample Size

| Level | N |
|-------|---|
| Trials per condition per model | 50 |
| Conditions | 4 |
| Models | 3 |
| **Total trials** | **600** |

## Cost Estimate

At approximately $0.02 per API call:
- 600 trials × $0.02 = **$12**
- Plus embedding costs (negligible)
- **Total estimated: $15-20**

## Sensitivity Analysis

With n = 50 per condition, we can detect:
- d = 0.40 at 80% power
- d = 0.36 at 70% power

This is adequate for detecting meaningful effects while remaining cost-efficient.

---

## References

Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum.

Faul, F., et al. (2007). G*Power 3: A flexible statistical power analysis program. *Behavior Research Methods*, 39(2), 175-191.
