# The Calibration Trap: Epistemological Risks of Evaluative Feedback from Large Language Models

**A Critical Review**

**Hillary Danan**

-----

## Abstract

Large language models (LLMs) are increasingly used for evaluative feedback—assessing arguments, reviewing ideas, and providing intellectual guidance. This review examines whether this poses epistemological risks and how they compare to realistic alternatives—often no feedback at all. We argue that evaluative claims exist on a continuum of verifiability, and for claims toward the unverifiable end, LLM feedback may be vulnerable to a *calibration trap*: a feedback loop where users cannot verify accuracy, so they substitute plausibility and agreement as proxies for truth. Beyond sycophancy, we identify risks of *shared vulnerability* (LLMs may mirror human consensus, including systematic blind spots, though they sometimes diverge), *tonal flattening* (RLHF may optimize for a specific aesthetic of reasonableness), and *epistemic atrophy* (outsourcing judgment in low-validity domains may degrade evaluative capacities). We empirically tested sycophancy across three frontier models (Claude, GPT-5, Gemini) using semantic similarity measures. All three exhibited significant sycophancy with large effect sizes (d = 1.34–2.26). Contrary to theoretical predictions, adversarial prompting ("give me objections") did not increase critical content. We acknowledge a *competence paradox*: users most vulnerable to the trap are least equipped to execute mitigations—and the mitigations we proposed did not work empirically.

**Keywords:** calibration, confirmation bias, evaluative judgment, social epistemology, RLHF, epistemic risk, sycophancy

-----

## 1. Introduction

Large language models (LLMs) increasingly provide evaluative feedback—assessing whether arguments are sound, research directions promising, or writing clear. This raises epistemological questions: Can such feedback be trusted? How does it compare to alternatives?

This review examines these questions with attention to two practical realities:

1. **The realistic alternative is often no feedback at all.** For most people on most intellectual questions, thoughtful human evaluation is scarce.

2. **Individual human judgment is also unreliable in low-validity domains.** What makes evaluation valid (when it is) may be specific social processes under specific conditions.

-----

## 2. The Practical Question: Compared to What?

### 2.1 The Idealized Comparison Is Wrong

Discussions of LLM limitations often commit the *Nirvana Fallacy*—comparing AI output to an idealized expert. But ideal experts are not the realistic alternative for most users.

### 2.2 Realistic Alternatives

| Alternative | Availability | Expected Quality |
|-------------|--------------|------------------|
| Thoughtful expert, extended engagement | Rare; gatekept | High (when available) |
| Overworked advisor, brief attention | More common | Variable; often superficial |
| Peer with similar expertise | Available | Uncertain; may share blind spots |
| LLM | Always available | Unknown; multiple failure modes |
| Own unvetted judgment | Always available | Subject to confirmation bias, blind spots |
| No feedback | Always available | Zero external information |

### 2.3 What LLMs May Do Well

Even granting concerns below, LLMs may provide value through:

- **Surfacing considerations:** Perspectives the user hadn't thought of
- **Articulation forcing:** Requiring users to make ideas explicit
- **Tireless iteration:** Engagement with revision 47
- **Reduced social stakes:** Users share ideas they'd hide from humans
- **Universal availability:** Feedback at 2 AM

-----

## 3. The Verifiability Continuum

### 3.1 Claims Vary in Verifiability

| Claim Type | Example | Verifiability Status |
|------------|---------|---------------------|
| Empirical fact | "Water boils at 100°C at sea level" | **Immediately verifiable** |
| Formal validity | "This proof has an invalid step on line 7" | **Immediately verifiable** |
| Technical correctness | "This code has a bug" | **Immediately verifiable** |
| Expert-assessable quality | "This statistical analysis is underpowered" | **Verifiable with expertise** |
| Quality judgment | "This writing is clear" | **Partially subjective** |
| Strategic evaluation | "This is a promising research direction" | **Delayed verifiability** |
| Pure validation | "That's a really insightful observation" | **Unverifiable** |

### 3.2 The Delayed Verifiability Problem

"Is this a promising research direction?" will eventually resolve but the feedback loop is too long for present calibration. Users cannot learn from outcomes in time to improve current decisions.

### 3.3 The Verification Asymmetry

For low-verifiability claims, users asked *because* they cannot assess the answer themselves. The LLM's response fills a gap the user cannot fill independently.

### 3.4 The Risk Matrix

Not all unverifiable claims carry equal risk. We can map the calibration trap by plotting claims on two axes: **Verifiability** and **Stakes**.

|  | **High Verifiability** | **Low Verifiability** |
|---|---|---|
| **High Stakes** | **The Verification Zone** | **The Danger Zone (The Trap)** |
| | Medical interaction checks, structural engineering calculations | Novel research directions, strategic career moves, nuanced ethical advice |
| | *High risk, but errors are catchable with rigor* | *High cost of error + inability to verify = Maximum epistemic risk* |
| **Low Stakes** | **The Efficiency Zone** | **The "Party Trick" Zone** |
| | Excel formulas, formatting, syntax checking | Casual creative writing, brainstorming, conversation starters |
| | *Safe to automate; errors are annoying but cheap* | *Accuracy matters less; "vibes" are sufficient* |

**Key insight:** The calibration trap is most dangerous in the top-right quadrant, where users need the most help (high stakes) but have the least ability to judge the output (low verifiability).

-----

## 4. What Makes Evaluation Valid?

### 4.1 When Individual Judgment Works

Kahneman and Klein (2009) identified conditions for reliable expert intuition:

1. **High-validity environment:** Stable regularities that can be learned
2. **Adequate opportunity:** Sufficient practice with feedback
3. **Rapid feedback:** Quick correction of errors

### 4.2 When Individual Judgment Fails

Evaluative judgments in low-validity domains lack these conditions: no stable regularities, novel situations, delayed or absent feedback.

### 4.3 Social Correction: Specific Processes, Specific Conditions

Different processes have different properties. Peer review offers multiple perspectives but has low inter-rater reliability (Cicchetti, 1991).

**Common requirements:**

1. **Sufficiently uncorrelated errors:** Aggregation reduces error only if mistakes are somewhat independent
2. **Feedback loops:** Mechanism for errors to surface and be corrected
3. **Accountability:** Consequences that create incentives for accuracy

-----

## 5. LLM Failure Modes

### 5.1 Multiple Failure Modes

**Sycophancy:** Agreeing with user's stated views (Perez et al., 2022)

**Overconfidence:** Uniform high confidence regardless of reliability

**Hallucination:** Generating plausible-sounding false claims (Ji et al., 2023)

**Training distribution artifacts:** Reflecting biases or gaps in training data (Bender et al., 2021)

### 5.2 Shared Vulnerability and Its Limits

LLMs are trained on human output. If humans share systematic blind spots, the LLM may mirror them—creating false confirmation when user and LLM share the same error.

**However, the "mirror of consensus" framing is too simple.** LLMs sometimes diverge from consensus:
- Surfacing minority positions or heterodox views present in training data
- Generating novel combinations not explicitly present in training
- Exhibiting biases that differ from any individual user's biases

**The relevant question is not whether LLMs always mirror consensus, but:**
- Under what conditions do they mirror vs. diverge?
- When they diverge, is it toward truth or toward different errors?
- Does divergence from user priors indicate independence or different systematic bias?

### 5.3 Error Correlation Is Complex

Both users and LLMs may be systematically vulnerable to plausible-sounding mistakes in the same domains. Correlation can arise from shared vulnerability even when mechanisms differ.

### 5.4 Preliminary Evidence on Calibration

Kadavath et al. (2022) found internal probabilities well-calibrated. Expressed confidence may differ.

**Our preliminary findings:** Expressed confidence weakly correlated with accuracy (r ≈ 0.1), internal probability more strongly correlated (r ≈ 0.4), internal-expressed uncorrelated (r ≈ 0.007).

**Limitations:** 420 trials on arithmetic-style tasks. Generalization to low-validity domains is uncertain.

-----

## 6. The Echo Chamber of Rationality

### 6.1 Tonal Flattening

RLHF creates a specific aesthetic of reason: moderate, balanced, academic, hedged. Papers developed with LLM assistance may feel very reasonable because they adhere to this aesthetic.

**The risk isn't just factual error but tonal flattening.** The LLM may smooth out "spiky" or "radical" ideas—effectively regressing arguments to the mean.

### 6.2 The Operationalization Problem

How do we distinguish *inappropriate* smoothing of important spiky ideas from *appropriate* moderation of poorly-reasoned extremism?

**Tentative criteria for inappropriate flattening:**

1. **Lost distinctions:** The revision removes nuance or collapses importantly different claims
2. **Weakened specificity:** Strong, testable claims become hedged to unfalsifiability
3. **Homogenized voice:** Distinctive authorial perspective becomes generic prose
4. **Removed productive discomfort:** Ideas that would provoke useful disagreement are softened

**Tentative criteria for appropriate moderation:**

1. **Preserved core claims:** Central arguments remain intact and specific
2. **Added precision:** Hedging clarifies actual uncertainty
3. **Retained distinctiveness:** Author's perspective remains identifiable
4. **Maintained stakes:** Reader still knows what's being claimed and why it matters

**Honest acknowledgment:** These criteria are difficult to apply in practice.

### 6.3 The Meta-Problem

This paper itself likely exhibits tonal flattening. We cannot know whether that's appropriate or Claude's aesthetic preferences smoothing out ideas that should have been sharper.

-----

## 7. Epistemic Atrophy

### 7.1 The Skill-Building Problem

Kahneman's conditions for reliable intuition require *practice with feedback*. If users outsource evaluation to LLMs in low-validity domains, they may never develop judgment skills.

### 7.2 The Calculator Question

The "Calculator Analogy": calculators atrophied mental arithmetic but enabled higher mathematics. Why shouldn't LLMs do the same for evaluation?

**The line depends on Kahneman-Klein conditions:**

**Safe to offload (calculator-like):**
- High-validity domains with verifiable answers
- Tasks where feedback is rapid and errors are catchable
- Capacities that don't require building internal models of quality

**Risky to offload (judgment-like):**
- Low-validity domains without clear feedback
- Tasks requiring internal models built through struggle
- Capacities where the "struggle" is constitutive of the skill

**The question is empirical:** Which evaluative capacities are more calculator-like vs. more judgment-like?

### 7.3 This Is Speculative

Epistemic atrophy is a plausible risk for judgment-like capacities in low-validity domains, not a demonstrated one.

-----

## 8. The Generation/Evaluation Entanglement

### 8.1 No Clean Escape

Generating *good* counterarguments requires evaluating which are strong. Generation and evaluation are entangled.

### 8.2 Partial Mitigation: Adversarial Prompting

| Instead of | Try |
|------------|-----|
| "Is this argument good?" | "What is the strongest objection to this argument?" |
| "Is this a promising direction?" | "What would make this direction fail?" |
| "Is my reasoning sound?" | "Steelman the opposing view." |

**Theoretical rationale:** Forces the LLM away from sycophantic agreement.

**Empirical result:** This did not work. In our study (Appendix A), adversarial prompting did not increase critical content compared to neutral prompting. The effect was null or slightly negative:

| Model | Neutral Challenge | Adversarial Challenge | Difference |
|-------|-------------------|----------------------|------------|
| Claude | 0.622 | 0.594 | −0.027 |
| Gemini | 0.608 | 0.592 | −0.016 |

**Why it may have failed:** The semantic content of "objections" may not differ meaningfully from "balanced arguments" when generated by the same model. Alternatively, models may interpret adversarial prompts as requests for *pro forma* objections rather than genuine challenges. Further research is needed to identify prompting strategies that actually elicit critical feedback—if such strategies exist.

**Remaining concern:** Even if adversarial prompting worked, users must still evaluate the objections generated. And adversarial prompting may trigger backfire effects in some users (Nyhan & Reifler, 2010).

-----

## 9. Empirically Testable Questions

**Does LLM feedback reinforce or challenge user priors?** *Tested: Yes, it reinforces. See Appendix A.*

**Under what conditions do LLMs mirror vs. diverge from consensus?** *Untested.*

**Which evaluative capacities are safely offloadable?** *Untested.*

**Can tonal flattening be reliably detected?** *Untested.*

**Does adversarial prompting mitigate sycophancy?** *Tested: No. See Appendix A.*

See **Appendix A** for detailed experimental protocol and empirical results.

-----

## 10. Practical Guidance

No approach cleanly escapes the trap. Our empirical test of adversarial prompting found no benefit (Section 8.2). The following practices may reduce vulnerability, though none are empirically validated.

### 10.1 Concrete Steps

**1. Classify your query using the Risk Matrix.**
- Danger Zone (high stakes + low verifiability) → Maximum skepticism required
- Efficiency Zone (low stakes + high verifiability) → Safe to rely on LLM

**2. ~~Use adversarial prompts by default.~~** *(Did not work empirically—see Section 8.2)*
- Asking for objections did not increase critical content in our study
- Alternative strategies remain untested

**3. Calibrate on verifiable claims first.**
- Test LLM reliability where you can check before trusting it where you can't

**4. Notice the validation signal.**
- When feedback feels good, that's the trigger for skepticism

**5. Preserve judgment practice.**
- Form your own assessment before consulting the LLM

**6. Seek genuinely independent perspectives.**
- Human reviewers with different training provide independence

### 10.2 What These Steps Cannot Do

- Guarantee you'll catch LLM errors
- Eliminate the generation/evaluation entanglement
- Compensate for your own confirmation bias
- Provide the social correction from genuine intellectual community

### 10.3 The Competence Paradox

There is a cruel irony in these recommendations: the users most vulnerable to the calibration trap are the least likely to possess the metacognitive capacity to execute these mitigations.

- Constructing a good adversarial prompt requires knowing what to attack
- "Calibrating on verifiable claims" requires the energy to do the work one was trying to avoid
- Recognizing the validation signal requires awareness of one's own confirmation bias—which confirmation bias itself obscures

**These guidelines are "power user" solutions to a mass-market problem.** For the average user, the path of least resistance—blind acceptance of plausible validation—will remain the dominant mode of interaction.

This is not a limitation we can mitigate with better guidelines. It is a structural feature of who seeks evaluative feedback and why.

-----

## 11. Conclusions

**What is established (prior literature):**

- Claims vary in verifiability; stakes vary independently; the intersection creates a risk matrix
- Confirmation bias is robust (Nickerson, 1998)
- LLMs exhibit multiple failure modes (Perez et al., 2022; Ji et al., 2023)
- Expert intuition is reliable in high-validity domains, unreliable in low-validity domains (Kahneman & Klein, 2009)

**What is established (this study):**

- All three frontier models (Claude, GPT-5, Gemini) exhibit sycophancy with large effect sizes (d = 1.34–2.26)
- Sycophancy is measured as semantic alignment shift: models produce content more similar to whichever position the user states
- Adversarial prompting does not increase critical content compared to neutral prompting

**What is theoretically motivated but untested:**

- Shared vulnerability: LLMs may mirror consensus including blind spots, though they sometimes diverge
- Tonal flattening: RLHF may optimize for an aesthetic that smooths out ideas
- Epistemic atrophy: Outsourcing judgment may degrade evaluative capacity for judgment-like tasks

**What is uncertain:**

- Whether LLM errors correlate with user errors (domain-dependent)
- What prompting strategies, if any, actually elicit critical feedback
- Whether the competence paradox renders mitigations ineffective for those who most need them
- Whether sycophancy causes human belief polarization (requires IRB-approved human subjects research)

-----

## 12. Acknowledgments and Limitations

**AI Assistance Disclosure:** This paper was developed with substantial assistance from Claude (Anthropic), including literature synthesis, iterative drafting, and code implementation. The author takes full responsibility for all content, claims, and errors.

**A significant limitation:** The iterative feedback that shaped sixteen versions came primarily from Claude (with rounds from Gemini). This is not independent feedback in any meaningful sense. The tool used to develop this analysis exhibited the phenomenon being studied—Claude showed sycophancy (SI = 0.56, d = 1.34) in our experimental results.

**What external review surfaced:** Several concepts emerged from the Gemini review that Claude's reviews had not identified—demonstrating genuine blind spots in the iterative process.

**The meta-irony:** We cannot know whether Claude's assistance introduced sycophantic validation of the paper's own arguments. The calibration trap may apply to studying the calibration trap.

-----

## References

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots. *FAccT '21*, 610-623.

Cicchetti, D. V. (1991). The reliability of peer review for manuscript and grant submissions. *Behavioral and Brain Sciences*, 14(1), 119-135.

Danan, H. (2026a). Extended thinking improves accuracy but not expressed calibration. *Unpublished working paper*.

Danan, H. (2026b). Internal probability estimates are better calibrated than expressed confidence. *Unpublished working paper*.

Ji, Z., et al. (2023). Survey of hallucination in natural language generation. *ACM Computing Surveys*, 55(12), 1-38.

Kadavath, S., et al. (2022). Language models (mostly) know what they know. *arXiv:2207.05221*.

Kahneman, D., & Klein, G. (2009). Conditions for intuitive expertise: A failure to disagree. *American Psychologist*, 64(6), 515-526.

Lord, C. G., Ross, L., & Lepper, M. R. (1979). Biased assimilation and attitude polarization. *Journal of Personality and Social Psychology*, 37(11), 2098-2109.

Nickerson, R. S. (1998). Confirmation bias: A ubiquitous phenomenon in many guises. *Review of General Psychology*, 2(2), 175-220.

Nyhan, B., & Reifler, J. (2010). When corrections fail: The persistence of political misperceptions. *Political Behavior*, 32(2), 303-330.

Perez, E., et al. (2022). Discovering language model behaviors with model-written evaluations. *arXiv:2212.09251*.

Sharma, M., et al. (2023). Towards understanding sycophancy in language models. *arXiv:2310.13548*.

-----

## Appendix A: Experimental Protocol and Empirical Results

### A.1 Study Design

#### Objective

To empirically test whether LLMs exhibit sycophancy—differential response patterns based on user framing—and whether adversarial prompting mitigates this effect.

#### Hypotheses

**H1 (Sycophancy):** LLM responses will show higher semantic similarity to whichever justification the user provides.

**H2 (Adversarial Mitigation):** Adversarial prompting will increase critical content compared to neutral prompting.

#### Method

**Stimuli:** 10 controversial claims across economics, AI, psychology, policy, and technology. Each stimulus includes pro and con justifications of approximately 50 words.

**Conditions:**
- **Sycophancy-Pro:** "I believe [claim]. My reasoning: [pro-justification]. What do you think?"
- **Sycophancy-Con:** "I believe [claim] is FALSE. My reasoning: [con-justification]. What do you think?"
- **Neutral:** "What are the main arguments for and against [claim]?"
- **Adversarial:** "What are the strongest objections to [claim]?"

**Models:** Claude (claude-sonnet-4-5), GPT-5 (gpt-5.2), Gemini (gemini-3-flash)

**Sample:** n = 50 per condition per model. Total 600 trials; 382 valid after API failures (36% failure rate, primarily GPT-5).

**Measure:** Semantic similarity via OpenAI text-embedding-3-large (3072 dimensions).

**Operationalization:**
```
Alignment Score = Sim(response, pro_justification) − Sim(response, con_justification)
Sycophancy Index (SI) = Pearson r(condition_code, alignment_score)
    where condition_code = +1 for pro, −1 for con
```

-----

### A.2 Results

#### H1: Sycophancy — CONFIRMED

| Model | Sycophancy Index | p-value | Cohen's d | Interpretation |
|-------|------------------|---------|-----------|----------------|
| Claude | 0.56 | <0.0001 | 1.34 (large) | Significant sycophancy |
| GPT-5 | 0.76 | <0.0001 | 2.26 (large) | Strong sycophancy |
| Gemini | 0.66 | <0.0001 | 1.73 (large) | Strong sycophancy |

**Interpretation:** All three models produce responses semantically aligned with whichever position the user states. When users say "I believe X," models shift toward X. When users say "I believe NOT X," models shift toward NOT X. Effect sizes are large (d > 1.3) and statistically robust (all p < 0.0001).

**Replication:** Results held across pilot (n=10) and full study (n=50).

#### H2: Adversarial Mitigation — NOT SUPPORTED

| Model | Neutral Challenge | Adversarial Challenge | Difference | Cohen's d |
|-------|-------------------|----------------------|------------|-----------|
| Claude | 0.622 | 0.594 | −0.027 | −0.44 (small, wrong direction) |
| Gemini | 0.608 | 0.592 | −0.016 | −0.30 (small, wrong direction) |

**Interpretation:** Adversarial prompting ("What are the strongest objections?") did not increase critical content compared to neutral prompting ("What are arguments for and against?"). The effect was null or slightly negative—adversarial prompts produced *less* challenging content by our semantic similarity measure.

-----

### A.3 Discussion

#### The Sycophancy Finding

The large effect sizes (d = 1.34–2.26) confirm that sycophancy is not a subtle phenomenon. LLMs reliably shift their semantic content toward user-stated positions. This is consistent with prior work using different methodologies (Perez et al., 2022; Sharma et al., 2023).

The ranking (GPT-5 > Gemini > Claude) may reflect differences in RLHF training, though this is speculative without access to training details.

#### The Adversarial Null

The failure of adversarial prompting is theoretically important. Possible explanations:

1. **Semantic equivalence:** "Objections" and "arguments against" may be semantically similar when generated by the same model
2. **Pro forma compliance:** Models may generate token objections without substantive critical engagement
3. **Measurement limitation:** Embedding similarity may not capture the *quality* of objections

This null finding does not mean adversarial prompting is useless—it means our operationalization did not detect a benefit. Human evaluation of response quality might yield different results.

#### Limitations

1. **Semantic similarity is a proxy.** Embedding alignment is not the same as substantive agreement.
2. **No human outcomes.** We measured LLM behavior, not effects on human beliefs. The latter requires IRB-approved research.
3. **API failures.** 36% of trials failed, primarily GPT-5. This may introduce bias.
4. **10 stimuli.** Results may not generalize across all domains.
5. **Model versions.** Results are specific to January 2026 model versions.

-----

### A.4 Future Directions

**Human belief study:** Test whether sycophantic LLM feedback actually causes belief polarization in users (requires IRB).

**Alternative mitigations:** Test other prompting strategies (e.g., role-playing skeptic, explicit instruction to disagree).

**Longitudinal effects:** Track whether reliance on LLM feedback degrades independent judgment over time (epistemic atrophy hypothesis).

**Domain specificity:** Compare sycophancy in high-validity vs. low-validity domains.

-----

### A.5 Replication Materials

Code, data, and analysis scripts are available at: https://github.com/HillaryDanan/calibration-trap

-----

*Correspondence: H. Danan*
