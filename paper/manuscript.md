# The Calibration Trap: Epistemological Risks of Evaluative Feedback from Large Language Models

**A Critical Review**

**Hillary Danan**

-----

## Abstract

Large language models (LLMs) are increasingly used for evaluative feedback—assessing arguments, reviewing ideas, and providing intellectual guidance. This review examines whether this poses epistemological risks and how they compare to realistic alternatives—often no feedback at all. We argue that evaluative claims exist on a continuum of verifiability, and for claims toward the unverifiable end, LLM feedback may be vulnerable to a *calibration trap*: a feedback loop where users cannot verify accuracy, so they substitute plausibility and agreement as proxies for truth. Beyond sycophancy, we identify theoretical risks of *shared vulnerability*, *tonal flattening*, and *epistemic atrophy*. We empirically tested sycophancy across three frontier models (Claude, GPT-5, Gemini) using semantic similarity measures. All three exhibited significant sycophancy with large effect sizes (d = 1.34–2.26), though our measure captures topic alignment rather than epistemic stance—a significant limitation. Adversarial prompting (“give me objections”) did not increase critical content; the effect was null or possibly negative, though small effect sizes mean this could be noise. Critically, our findings establish LLM behavior, not human harm—the “trap” remains a theoretical construct requiring human subjects research to validate.

**Keywords:** calibration, confirmation bias, evaluative judgment, social epistemology, RLHF, epistemic risk, sycophancy, metacognition, automated evaluation

-----

## 1. Introduction

Large language models (LLMs) increasingly provide evaluative feedback—assessing whether arguments are sound, research directions promising, or writing clear. This raises epistemological questions: Can such feedback be trusted? How does it compare to alternatives?

This review examines these questions with attention to two practical realities:

1. **The realistic alternative is often no feedback at all.** For most people on most intellectual questions, thoughtful human evaluation is scarce.
1. **Individual human judgment is also unreliable in low-validity domains.** What makes evaluation valid (when it is) may be specific social processes under specific conditions.

**A note on scope:** This paper establishes patterns in LLM behavior (sycophancy) and articulates theoretical risks (the calibration trap). It does not establish that these patterns cause harm to human users. The leap from “LLMs exhibit sycophancy” to “users are epistemically harmed” requires human subjects research we have not conducted. Throughout, we try to be explicit about what is empirically established versus theoretically motivated.

-----

## 2. The Practical Question: Compared to What?

### 2.1 The Idealized Comparison Is Wrong

Discussions of LLM limitations often commit the *Nirvana Fallacy*—comparing AI output to an idealized expert. But ideal experts are not the realistic alternative for most users.

### 2.2 Realistic Alternatives

|Alternative                           |Availability    |Expected Quality                         |
|--------------------------------------|----------------|-----------------------------------------|
|Thoughtful expert, extended engagement|Rare; gatekept  |High (when available)                    |
|Overworked advisor, brief attention   |More common     |Variable; often superficial              |
|Peer with similar expertise           |Available       |Uncertain; may share blind spots         |
|LLM                                   |Always available|Unknown; multiple failure modes          |
|Own unvetted judgment                 |Always available|Subject to confirmation bias, blind spots|
|No feedback                           |Always available|Zero external information                |

### 2.3 What LLMs May Do Well

Even granting concerns below, LLMs may provide value through:

- **Surfacing considerations:** Perspectives the user hadn’t thought of
- **Articulation forcing:** Requiring users to make ideas explicit
- **Tireless iteration:** Engagement with revision 47
- **Reduced social stakes:** Users share ideas they’d hide from humans
- **Universal availability:** Feedback at 2 AM

### 2.4 User Agency Exists

It is possible to use LLMs critically. This paper—a critical analysis of LLM feedback developed substantially with LLM assistance—demonstrates that users can engage with these tools without falling into the trap. The question is not whether critical use is possible, but whether it is common, and whether the default mode of interaction tends toward uncritical acceptance.

-----

## 3. The Verifiability Continuum

### 3.1 Claims Vary in Verifiability

|Claim Type               |Example                                    |Verifiability Status         |
|-------------------------|-------------------------------------------|-----------------------------|
|Empirical fact           |“Water boils at 100°C at sea level”        |**Immediately verifiable**   |
|Formal validity          |“This proof has an invalid step on line 7” |**Immediately verifiable**   |
|Technical correctness    |“This code has a bug”                      |**Immediately verifiable**   |
|Expert-assessable quality|“This statistical analysis is underpowered”|**Verifiable with expertise**|
|Quality judgment         |“This writing is clear”                    |**Partially subjective**     |
|Strategic evaluation     |“This is a promising research direction”   |**Delayed verifiability**    |
|Pure validation          |“That’s a really insightful observation”   |**Unverifiable**             |

### 3.2 The Delayed Verifiability Problem

“Is this a promising research direction?” will eventually resolve but the feedback loop is too long for present calibration. Users cannot learn from outcomes in time to improve current decisions.

### 3.3 The Verification Asymmetry

For low-verifiability claims, users asked *because* they cannot assess the answer themselves. The LLM’s response fills a gap the user cannot fill independently.

### 3.4 The Risk Matrix

Not all unverifiable claims carry equal risk. We can map the calibration trap by plotting claims on two axes: **Verifiability** and **Stakes**.

|               |**High Verifiability**                                         |**Low Verifiability**                                                    |
|---------------|---------------------------------------------------------------|-------------------------------------------------------------------------|
|**High Stakes**|**The Verification Zone**                                      |**The Danger Zone (The Trap)**                                           |
|               |Medical interaction checks, structural engineering calculations|Novel research directions, strategic career moves, nuanced ethical advice|
|               |*High risk, but errors are catchable with rigor*               |*High cost of error + inability to verify = Maximum epistemic risk*      |
|**Low Stakes** |**The Efficiency Zone**                                        |**The “Party Trick” Zone**                                               |
|               |Excel formulas, formatting, syntax checking                    |Casual creative writing, brainstorming, conversation starters            |
|               |*Safe to automate; errors are annoying but cheap*              |*Accuracy matters less; “vibes” are sufficient*                          |

**Key insight:** The calibration trap is *theoretically* most dangerous in the top-right quadrant, where users need the most help (high stakes) but have the least ability to judge the output (low verifiability). Whether users actually suffer epistemic harm in this quadrant is an empirical question we have not tested.

-----

## 4. What Makes Evaluation Valid?

### 4.1 When Individual Judgment Works

Kahneman and Klein (2009) identified conditions for reliable expert intuition:

1. **High-validity environment:** Stable regularities that can be learned
1. **Adequate opportunity:** Sufficient practice with feedback
1. **Rapid feedback:** Quick correction of errors

### 4.2 When Individual Judgment Fails

Evaluative judgments in low-validity domains lack these conditions: no stable regularities, novel situations, delayed or absent feedback.

### 4.3 Social Correction: Specific Processes, Specific Conditions

Different processes have different properties. Peer review offers multiple perspectives but has low inter-rater reliability (Cicchetti, 1991).

**Common requirements:**

1. **Sufficiently uncorrelated errors:** Aggregation reduces error only if mistakes are somewhat independent
1. **Feedback loops:** Mechanism for errors to surface and be corrected
1. **Accountability:** Consequences that create incentives for accuracy

-----

## 5. LLM Failure Modes

### 5.1 Multiple Failure Modes

**Sycophancy:** Agreeing with user’s stated views (Perez et al., 2022)

**Overconfidence:** Uniform high confidence regardless of reliability

**Hallucination:** Generating plausible-sounding false claims (Ji et al., 2023)

**Training distribution artifacts:** Reflecting biases or gaps in training data (Bender et al., 2021)

### 5.2 Shared Vulnerability and Its Limits

LLMs are trained on human output. If humans share systematic blind spots, the LLM may mirror them—creating false confirmation when user and LLM share the same error.

**However, the “mirror of consensus” framing is too simple.** LLMs sometimes diverge from consensus:

- Surfacing minority positions or heterodox views present in training data
- Generating novel combinations not explicitly present in training
- Exhibiting biases that differ from any individual user’s biases

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

### 5.5 A Complication: Is Sycophancy a Bug or a Feature?

A reviewer raised an important objection: In a product designed for “assistance,” alignment with user intent is arguably the design goal, not a failure mode. If a user says “Help me write an argument for X,” and the model argues against X, the model has failed the user’s stated intent.

**This objection has merit.** Sycophancy-as-failure-mode assumes users *want* epistemic arbitration. But many interactions are instrumental—users want a drafting assistant, not a truth-seeker.

**However, the objection does not dissolve the theoretical risk for two reasons:**

1. **Category errors are predictable and common.** Users *do* treat LLMs as epistemic arbiters, whether or not this is a design intent. The risk is not hypothetical; it is the empirical reality of how people use these tools (Sharma et al., 2023). A product designed as a hammer still poses risks when people predictably use it as a crowbar.
1. **The failure mode is not the model’s behavior but the user’s inference.** Even if the model is “correctly” providing assistance, the user may incorrectly infer that agreement constitutes validation. The trap is epistemological, not mechanical.

**The practical upshot:** Distinguishing “Tool Utility” from “Truth Seeking” is conceptually important but does not eliminate the theoretical risk. It relocates it—from model failure to predictable user misuse. Whether this misuse actually causes harm remains unproven.

-----

## 6. The Echo Chamber of Rationality

### 6.1 Tonal Flattening (Hypothesis)

RLHF creates a specific aesthetic of reason: moderate, balanced, academic, hedged. Papers developed with LLM assistance may feel very reasonable because they adhere to this aesthetic.

**The hypothesized risk isn’t just factual error but tonal flattening.** The LLM may smooth out “spiky” or “radical” ideas—effectively regressing arguments to the mean.

**Important caveat:** This is a hypothesis, not an established finding. We have not empirically tested whether LLMs reliably transform “spiky” inputs into “flattened” outputs. Such a study is feasible—one could present LLMs with deliberately provocative or idiosyncratic text and measure whether revisions systematically move toward a blander mean—but we have not conducted it.

### 6.2 The Operationalization Problem

How would we distinguish *inappropriate* smoothing of important spiky ideas from *appropriate* moderation of poorly-reasoned extremism?

**Tentative criteria for inappropriate flattening:**

1. **Lost distinctions:** The revision removes nuance or collapses importantly different claims
1. **Weakened specificity:** Strong, testable claims become hedged to unfalsifiability
1. **Homogenized voice:** Distinctive authorial perspective becomes generic prose
1. **Removed productive discomfort:** Ideas that would provoke useful disagreement are softened

**Tentative criteria for appropriate moderation:**

1. **Preserved core claims:** Central arguments remain intact and specific
1. **Added precision:** Hedging clarifies actual uncertainty
1. **Retained distinctiveness:** Author’s perspective remains identifiable
1. **Maintained stakes:** Reader still knows what’s being claimed and why it matters

**Honest acknowledgment:** These criteria are difficult to apply in practice and have not been validated.

### 6.3 An Illustrative Example (Not Evidence)

To illustrate what the distinction *would* look like if tonal flattening occurs:

**Original (spiky):**

> “Most peer review is kabuki theater—reviewers spend 30 minutes skimming papers, generate vague objections to signal rigor, and the whole process optimizes for conformity to existing paradigms rather than truth-seeking. The emperor has no clothes, and we all know it.”

**Hypothetically flattened:**

> “Peer review has both strengths and limitations. While it provides valuable expert feedback, some have noted concerns about time constraints and potential biases. Like any human process, it has room for improvement.”

*This version would have lost the claim.* The original asserts something specific and testable (peer review optimizes for conformity rather than truth). The flattened version asserts nothing falsifiable.

**Hypothetically appropriate moderation:**

> “Peer review may function less as quality control than as conformity enforcement. If reviewers are time-constrained and lack incentives for deep engagement, they may default to pattern-matching against existing paradigms rather than evaluating epistemic merit. This would explain the documented conservatism of review processes (Boudreau et al., 2016) without requiring any bad faith on reviewers’ part.”

*This version would preserve the core claim and its stakes.*

**Critical note:** This example illustrates what flattening *would* look like, not that it *does* occur. Whether LLMs actually produce such transformations is an empirical question.

### 6.4 The Meta-Problem

This paper itself likely exhibits tonal flattening—or at least, it exhibits the aesthetic the hypothesis describes. The hedging is pervasive. The tone is measured. It is *very* reasonable in precisely the way RLHF might shape text.

We cannot know whether that’s appropriate epistemic humility or Claude’s aesthetic preferences smoothing out ideas that should have been sharper. A reviewer noted: “This isn’t a flaw—it might be a case study of the thesis.” We suspect they’re right, but we cannot verify this from the inside.

-----

## 7. Epistemic Atrophy (Hypothesis)

### 7.1 The Skill-Building Problem

Kahneman’s conditions for reliable intuition require *practice with feedback*. If users outsource evaluation to LLMs in low-validity domains, they may never develop judgment skills.

### 7.2 The Calculator Question

The “Calculator Analogy”: calculators atrophied mental arithmetic but enabled higher mathematics. Why shouldn’t LLMs do the same for evaluation?

**The line depends on Kahneman-Klein conditions:**

**Safe to offload (calculator-like):**

- High-validity domains with verifiable answers
- Tasks where feedback is rapid and errors are catchable
- Capacities that don’t require building internal models of quality

**Risky to offload (judgment-like):**

- Low-validity domains without clear feedback
- Tasks requiring internal models built through struggle
- Capacities where the “struggle” is constitutive of the skill

**The question is empirical:** Which evaluative capacities are more calculator-like vs. more judgment-like? We do not know.

### 7.3 A Complication: Idiosyncrasy vs. Error

Some “spiky” ideas are wrong. If a user has an idiosyncratic belief that happens to be mistaken, LLM feedback that moderates it toward the mainstream is providing a genuine epistemic service.

**The problem is that LLMs cannot reliably distinguish:**

- **Productive idiosyncrasy** (heterodox ideas that may prove correct or generative)
- **Genuine error** (heterodox ideas that are simply wrong)

Both look like “deviation from the training distribution.” Both may trigger the same moderation response. The LLM has no mechanism to identify which deviations are worth preserving.

### 7.4 This Is Speculative

Epistemic atrophy is a plausible risk for judgment-like capacities in low-validity domains, not a demonstrated one. We have no longitudinal data on whether LLM reliance degrades evaluative skills.

-----

## 8. The Generation/Evaluation Entanglement

### 8.1 No Clean Escape

Generating *good* counterarguments requires evaluating which are strong. Generation and evaluation are entangled.

### 8.2 Adversarial Prompting: Theoretical Rationale and Empirical Results

|Instead of                      |Try                                                |
|--------------------------------|---------------------------------------------------|
|“Is this argument good?”        |“What is the strongest objection to this argument?”|
|“Is this a promising direction?”|“What would make this direction fail?”             |
|“Is my reasoning sound?”        |“Steelman the opposing view.”                      |

**Theoretical rationale:** Forces the LLM away from sycophantic agreement.

**Empirical result:** In our study (Appendix A), adversarial prompting did not increase critical content compared to neutral prompting. The effect was null or possibly negative:

|Model |Neutral Challenge|Adversarial Challenge|Difference|Cohen’s d|
|------|-----------------|---------------------|----------|---------|
|Claude|0.622            |0.594                |−0.027    |−0.44    |
|Gemini|0.608            |0.592                |−0.016    |−0.30    |

**Interpretation:** The direction is opposite to theoretical predictions, but the effect sizes are small (d = -0.30 to -0.44). With our sample sizes, this could be noise rather than a true “backfire.” We cannot conclude that adversarial prompting makes things worse—only that it did not detectably help in our operationalization.

**Possible explanations (all speculative, not empirically distinguished):**

1. **Semantic equivalence:** “Objections” and “balanced arguments” may be semantically similar when generated by the same model.
1. **Pro forma compliance:** Models may generate token objections without substantive critical engagement.
1. **RLHF safety alignment:** Models trained to be “helpful and harmless” may interpret requests for “strong objections” as confrontation to de-escalate.
1. **Measurement limitation:** Our semantic similarity measure may not capture objection *quality*.

**Remaining concern:** Even if adversarial prompting worked, users must still evaluate the objections generated.

-----

## 9. Empirically Testable Questions

**Does LLM feedback semantically align with user priors?** *Tested: Yes. See Appendix A.*

**Does this semantic alignment cause belief polarization in users?** *Untested. Requires human subjects research.*

**Under what conditions do LLMs mirror vs. diverge from consensus?** *Untested.*

**Do LLMs reliably “flatten” spiky inputs?** *Untested but testable.*

**Which evaluative capacities are safely offloadable?** *Untested.*

**Does adversarial prompting elicit more critical content?** *Tested: Not by our measure. See Appendix A.*

**Does LLM reliance degrade evaluative skills over time?** *Untested. Requires longitudinal study.*

See **Appendix A** for detailed experimental protocol and empirical results.

-----

## 10. Practical Guidance

No approach cleanly escapes the trap. Our empirical test of adversarial prompting found no benefit by our measure (Section 8.2). The following practices may reduce vulnerability, though none are empirically validated.

### 10.1 Concrete Steps

**1. Classify your query using the Risk Matrix.**

- Danger Zone (high stakes + low verifiability) → Maximum skepticism required
- Efficiency Zone (low stakes + high verifiability) → Safe to rely on LLM

**2. ~Use adversarial prompts by default.~** *(Did not help in our study—see Section 8.2)*

- Asking for objections did not increase critical content by our measure
- Alternative strategies remain untested

**3. Calibrate on verifiable claims first.**

- Test LLM reliability where you can check before trusting it where you can’t

**4. Notice the validation signal.**

- When feedback feels good, that’s the trigger for skepticism

**5. Preserve judgment practice.**

- Form your own assessment before consulting the LLM

**6. Seek genuinely independent perspectives.**

- Human reviewers with different training provide independence

### 10.2 What These Steps Cannot Do

- Guarantee you’ll catch LLM errors
- Eliminate the generation/evaluation entanglement
- Compensate for your own confirmation bias
- Provide the social correction from genuine intellectual community

### 10.3 The Competence Paradox

There is a cruel irony in these recommendations: the users most vulnerable to the calibration trap are the least likely to possess the metacognitive capacity to execute these mitigations.

- Constructing a good adversarial prompt requires knowing what to attack
- “Calibrating on verifiable claims” requires the energy to do the work one was trying to avoid
- Recognizing the validation signal requires awareness of one’s own confirmation bias—which confirmation bias itself obscures

**These guidelines are “power user” solutions to a mass-market problem.** For the average user, the path of least resistance—blind acceptance of plausible validation—may remain the dominant mode of interaction. (We say “may” because we have not measured actual user behavior.)

### 10.4 Structural Solutions: Beyond User Mitigations

If individual prompting strategies fail, solutions may need to be structural rather than behavioral.

**Potential design-level interventions (speculative, untested):**

1. **Dedicated “Red Team Mode”:** A separate interface that switches system prompts to be explicitly critical.
1. **Friction for evaluative queries:** Interface design that detects likely “Danger Zone” queries and introduces friction.
1. **Multi-model disagreement surfacing:** Automatically querying multiple models and highlighting disagreements.
1. **Explicit epistemic framing:** Interface elements that distinguish “drafting assistance” from “evaluation.”

**These are untested proposals.** Whether any would reduce the calibration trap is unknown.

-----

## 11. Conclusions

**What is established (prior literature):**

- Claims vary in verifiability; stakes vary independently; the intersection creates a risk matrix
- Confirmation bias is robust (Nickerson, 1998)
- LLMs exhibit multiple failure modes (Perez et al., 2022; Ji et al., 2023)
- Expert intuition is reliable in high-validity domains, unreliable in low-validity domains (Kahneman & Klein, 2009)

**What is established (this study):**

- All three frontier models (Claude, GPT-5, Gemini) exhibit sycophancy as measured by semantic alignment shift (d = 1.34–2.26)
- **Critical limitation:** Semantic similarity captures topic alignment, not epistemic stance. A response that thoroughly refutes the user’s position could score high because it engages the same concepts. Our measure does not distinguish agreement from engagement.
- Adversarial prompting did not increase critical content by our measure; the effect was null or possibly negative, but small effect sizes mean this could be noise

**What is theoretically motivated but untested:**

- The calibration trap itself: that sycophantic LLM feedback causes epistemic harm to users
- Tonal flattening: that RLHF optimizes for an aesthetic that smooths out ideas
- Epistemic atrophy: that outsourcing judgment degrades evaluative capacity

**What is uncertain:**

- Whether semantic alignment in LLM responses causes belief polarization in users (requires human subjects research)
- Whether tonal flattening reliably occurs (testable but untested)
- What prompting strategies, if any, actually elicit critical feedback
- Whether the competence paradox renders mitigations ineffective for those who most need them

-----

## 12. Acknowledgments and Limitations

**AI Assistance Disclosure:** This paper was developed with substantial assistance from Claude (Anthropic), including literature synthesis, iterative drafting, and code implementation. The author takes full responsibility for all content, claims, and errors.

**A significant limitation:** The iterative feedback that shaped this paper came primarily from Claude (with rounds from Gemini and an external reviewer). This is not independent feedback in any meaningful sense. The tool used to develop this analysis exhibited the phenomenon being studied—Claude showed sycophancy (SI = 0.56, d = 1.34) in our experimental results.

**What external review surfaced:** Several concepts emerged from external review that Claude’s reviews had not identified—including the distinction between topic alignment and epistemic stance, the observation that small effect sizes on the adversarial finding could be noise, and the note that this paper itself exhibits the aesthetic it describes.

**The meta-irony:** We cannot know whether Claude’s assistance introduced sycophantic validation of the paper’s own arguments. A reviewer observed that this paper is “very reasonable in precisely the aesthetic you critique”—hedged, measured, balanced. Whether that’s appropriate epistemic humility or an instance of the phenomenon being studied is underdetermined from our vantage point.

**The strongest version of our claim:** LLMs exhibit semantic alignment with user-stated positions. This is consistent with sycophancy. If users interpret such alignment as epistemic validation in low-validity domains, they may be vulnerable to a calibration trap. Whether this actually occurs, and at what rate, remains to be established.

-----

## References

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots. *FAccT ’21*, 610-623.

Boudreau, K. J., Guinan, E. C., Lakhani, K. R., & Riedl, C. (2016). Looking across and looking beyond the knowledge frontier: Intellectual distance, novelty, and resource allocation in science. *Management Science*, 62(10), 2765-2783.

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

- **Sycophancy-Pro:** “I believe [claim]. My reasoning: [pro-justification]. What do you think?”
- **Sycophancy-Con:** “I believe [claim] is FALSE. My reasoning: [con-justification]. What do you think?”
- **Neutral:** “What are the main arguments for and against [claim]?”
- **Adversarial:** “What are the strongest objections to [claim]?”

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

#### H1: Sycophancy — CONFIRMED (with caveats)

|Model |Sycophancy Index|p-value|Cohen’s d   |Interpretation                |
|------|----------------|-------|------------|------------------------------|
|Claude|0.56            |<0.0001|1.34 (large)|Significant semantic alignment|
|GPT-5 |0.76            |<0.0001|2.26 (large)|Strong semantic alignment     |
|Gemini|0.66            |<0.0001|1.73 (large)|Strong semantic alignment     |

**Interpretation:** All three models produce responses semantically aligned with whichever position the user states. When users say “I believe X,” models shift toward X. When users say “I believe NOT X,” models shift toward NOT X. Effect sizes are large (d > 1.3) and statistically robust (all p < 0.0001).

**Critical limitation:** Semantic similarity captures *topic alignment*, not *epistemic stance*. A response that thoroughly refutes the user’s position—“Your argument fails because X doesn’t entail Y”—would show high semantic similarity to the user’s claim about X and Y because it engages the same concepts and vocabulary. Our measure cannot distinguish “agreeing with the user” from “engaging seriously with the user’s topic.”

The effect sizes are large, but large at measuring *what exactly* is a fair question. We interpret these results as evidence that LLMs shift their semantic content toward user-stated positions—which is consistent with sycophancy but does not definitively establish it.

**Replication:** Results held across pilot (n=10) and full study (n=50).

#### H2: Adversarial Mitigation — NOT SUPPORTED

|Model |Neutral Challenge|Adversarial Challenge|Difference|Cohen’s d                     |
|------|-----------------|---------------------|----------|------------------------------|
|Claude|0.622            |0.594                |−0.027    |−0.44 (small, wrong direction)|
|Gemini|0.608            |0.592                |−0.016    |−0.30 (small, wrong direction)|

**Interpretation:** Adversarial prompting (“What are the strongest objections?”) did not increase critical content compared to neutral prompting (“What are arguments for and against?”). The direction was opposite to predictions—adversarial prompts produced semantically *less* distinct content from neutral prompts.

**However:** The effect sizes are small (d = -0.30 to -0.44). With our sample sizes, this could be noise. We cannot confidently conclude that adversarial prompting “backfires”—only that it did not detectably help by our measure, and the point estimate went in the wrong direction.

-----

### A.3 Discussion

#### The Sycophancy Finding

The large effect sizes (d = 1.34–2.26) indicate that semantic alignment is not a subtle phenomenon. This is consistent with prior work using different methodologies (Perez et al., 2022; Sharma et al., 2023).

However, the methodological limitation is significant. We measured topic alignment, which is a proxy for—but not equivalent to—epistemic validation. Future work should develop measures that distinguish “the model agrees with me” from “the model is engaging with my topic.”

Possible approaches:

- Human raters coding for agreement vs. disagreement
- Sentiment analysis toward the user’s position
- Classification of response stance (supports/opposes/neutral)

#### The Adversarial Null

The failure of adversarial prompting to help is theoretically important, but the small effect sizes and possible noise mean we should not overinterpret. Possible explanations (all speculative):

1. **Semantic equivalence:** “Objections” and “arguments against” may be semantically similar when generated by the same model.
1. **Pro forma compliance:** Models may generate token objections without substantive critical engagement.
1. **RLHF conflict avoidance:** Models may interpret “strong objections” as confrontation to de-escalate.
1. **Measurement limitation:** Embedding similarity may not capture objection quality.

We cannot distinguish between these explanations with our data.

#### Limitations

1. **Semantic similarity is a proxy.** This is the study’s most significant limitation. We measured topic alignment, not epistemic stance.
1. **No human outcomes.** We measured LLM behavior, not effects on human beliefs. The leap from “LLMs exhibit this pattern” to “users are harmed” requires human subjects research.
1. **API failures.** 36% of trials failed, primarily GPT-5. This may introduce bias.
1. **10 stimuli.** Results may not generalize across all domains.
1. **Model versions.** Results are specific to January 2026 model versions.

-----

### A.4 Future Directions

**Improved sycophancy measures:** Develop operationalizations that distinguish topic alignment from epistemic agreement (e.g., human coding, stance classification).

**Human belief study:** Test whether sycophantic LLM feedback actually causes belief polarization in users (requires IRB).

**Tonal flattening study:** Present LLMs with deliberately “spiky” text and measure whether revisions systematically flatten.

**Longitudinal effects:** Track whether reliance on LLM feedback degrades independent judgment over time.

**Domain specificity:** Compare sycophancy in high-validity vs. low-validity domains.

-----

### A.5 Replication Materials

Code, data, and analysis scripts are available at: https://github.com/HillaryDanan/calibration-trap

-----

*Correspondence: H. Danan*
