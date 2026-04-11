# 🧹 Awesome LLM Unlearning

<p align="center">
  <a href="https://awesome.re"><img src="https://img.shields.io/badge/Awesome-%F0%9F%A7%B9_LLM_Unlearning-000000?style=for-the-badge&labelColor=000000" alt="Awesome LLM Unlearning"></a>
  <a href="https://github.com/chrisliu298/awesome-llm-unlearning/stargazers"><img src="https://img.shields.io/github/stars/chrisliu298/awesome-llm-unlearning?style=for-the-badge&logo=github&logoColor=white&label=Stars&labelColor=000000&color=000000" alt="GitHub Stars"></a>
  <a href="https://github.com/chrisliu298/awesome-llm-unlearning/network/members"><img src="https://img.shields.io/github/forks/chrisliu298/awesome-llm-unlearning?style=for-the-badge&logo=github&logoColor=white&label=Forks&labelColor=000000&color=000000" alt="GitHub Forks"></a>
  <a href="https://github.com/chrisliu298/awesome-llm-unlearning/commits"><img src="https://img.shields.io/github/last-commit/chrisliu298/awesome-llm-unlearning?style=for-the-badge&logo=github&logoColor=white&label=Last%20Commit&labelColor=000000&color=000000" alt="Last Commit"></a>
</p>

A curated collection of papers, surveys, benchmarks, and tools for machine unlearning in large language models.

> **LLM unlearning** studies how to make a language model forget targeted knowledge, data, or behaviors without retraining from scratch.
> It covers factual erasure, privacy and copyright removal, safety and capability control, and multimodal extensions.
> Good unlearning must balance forgetting quality, retained utility, robustness to recovery, and computational efficiency.

## Contents

**Orientation**

- [Quick Start by Role](#quick-start-by-role)
- [Start Here](#start-here)
- [Surveys](#surveys)
- [Taxonomy](#taxonomy)
  - [By Unlearning Target](#by-unlearning-target)
  - [By Method Family](#by-method-family)
  - [By Modality and Setting](#by-modality-and-setting)
  - [By Evaluation Focus](#by-evaluation-focus)

**Papers**

- [Foundations and Precursors](#foundations-and-precursors)
  - [Decoding-time and anti-model precursors](#decoding-time-and-anti-model-precursors)
  - [Editing, arithmetic, and general unlearning precursors](#editing-arithmetic-and-general-unlearning-precursors)
- [Core LLM Unlearning Papers](#core-llm-unlearning-papers)
  - [Gradient, objective, and optimization-based methods](#gradient-objective-and-optimization-based-methods)
  - [Preference, distillation, and RL-based unlearning](#preference-distillation-and-rl-based-unlearning)
  - [Representation, activation, and circuit-based methods](#representation-activation-and-circuit-based-methods)
  - [Editing, task arithmetic, and weight-space methods](#editing-task-arithmetic-and-weight-space-methods)
  - [Parameter-efficient, sparse, and modular methods](#parameter-efficient-sparse-and-modular-methods)
  - [Selective, continual, and data-efficient methods](#selective-continual-and-data-efficient-methods)
- [Unlearning Targets and Threat Models](#unlearning-targets-and-threat-models)
  - [Factual knowledge, entities, and structural memory](#factual-knowledge-entities-and-structural-memory)
  - [Privacy, memorization, copyright, and right-to-be-forgotten](#privacy-memorization-copyright-and-right-to-be-forgotten)
  - [Safety, harmful content, jailbreaks, and backdoors](#safety-harmful-content-jailbreaks-and-backdoors)
  - [Skills, reasoning, bias, hallucination, and behavior shaping](#skills-reasoning-bias-hallucination-and-behavior-shaping)
- [Evaluation, Benchmarks, Auditing, and Attacks](#evaluation-benchmarks-auditing-and-attacks)
  - [Benchmarks, datasets, and evaluation suites](#benchmarks-datasets-and-evaluation-suites)
  - [Auditing, metrics, and verification](#auditing-metrics-and-verification)
  - [Robustness, recovery, and failure analyses](#robustness-recovery-and-failure-analyses)
- [Theoretical and Analytical Work](#theoretical-and-analytical-work)
  - [Optimization, generalization, and provable views](#optimization-generalization-and-provable-views)
  - [Mechanistic, causal, and representation analyses](#mechanistic-causal-and-representation-analyses)
- [Applications and Extensions](#applications-and-extensions)
  - [Multimodal and vision-language unlearning](#multimodal-and-vision-language-unlearning)
  - [Federated, modular, and systems settings](#federated-modular-and-systems-settings)
  - [Recommendation, code, biomedical, agents, and other domain settings](#recommendation-code-biomedical-agents-and-other-domain-settings)

**Resources**

- [Frameworks](#frameworks)
- [Blog Posts](#blog-posts)
- [Datasets and Benchmarks](#datasets-and-benchmarks)
- [Contributing](#contributing)
- [Citation](#citation)

## Quick Start by Role

| Role                                                  | Start with                                                                                                                                                                                            | Key resources                                                                                                                                                               |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New to unlearning                                     | [Unlearning in LLMs](https://arxiv.org/abs/2601.13264)                                                                                                                                                | [Start Here](#start-here), [Surveys](#surveys), [Taxonomy](#taxonomy)                                                                                                       |
| Researcher surveying methods                          | [Large Language Model Unlearning](https://arxiv.org/abs/2310.10683), [Negative Preference Optimization](https://arxiv.org/abs/2404.05868), [Mechanistic Unlearning](https://arxiv.org/abs/2410.12949) | [Core LLM Unlearning Papers](#core-llm-unlearning-papers), [Taxonomy](#taxonomy)                                                                                            |
| Building an unlearning pipeline                       | [TOFU](https://arxiv.org/abs/2401.06121), [MUSE](https://openreview.net/forum?id=TArmA033BU), [OpenUnlearning](https://arxiv.org/abs/2506.12618)                                                      | [Frameworks](#frameworks), [Datasets and Benchmarks](#datasets-and-benchmarks)                                                                                              |
| Evaluating unlearning for safety and robustness       | [WMDP](https://arxiv.org/abs/2403.03218), [Safe Unlearning](https://arxiv.org/abs/2407.02855), [The Erasure Illusion](https://arxiv.org/abs/2512.19025)                                               | [Evaluation, Benchmarks, Auditing, and Attacks](#evaluation-benchmarks-auditing-and-attacks), [Unlearning Targets and Threat Models](#unlearning-targets-and-threat-models) |
| Working on privacy, copyright, or multimodal deletion | [REVS](https://arxiv.org/abs/2406.09325), [MLLMU-Bench](https://arxiv.org/abs/2410.22108), [MMUNLEARNER](https://arxiv.org/abs/2502.11051)                                                            | [Applications and Extensions](#applications-and-extensions), [Datasets and Benchmarks](#datasets-and-benchmarks)                                                            |

## Start Here

The fastest reading path through the area:

0. **Survey** — [Unlearning in LLMs](https://arxiv.org/abs/2601.13264).
   Comprehensive map of methods, evaluation protocols, and open challenges.
1. **Early intuition** — [DExperts](https://arxiv.org/abs/2105.03023), [Who's Harry Potter?](https://arxiv.org/abs/2310.02238), and [Large Language Model Unlearning](https://arxiv.org/abs/2310.10683).
   You will understand why forgetting in generative models is harder than deleting a classifier example.
2. **Canonical benchmarks** — [TOFU](https://arxiv.org/abs/2401.06121), [MUSE](https://openreview.net/forum?id=TArmA033BU), and [WMDP](https://arxiv.org/abs/2403.03218).
   These define the standard fictitious-fact, multi-metric, and dangerous-capability evaluation setups.
3. **Optimization baselines** — [Multi-Objective LLM Unlearning](https://arxiv.org/abs/2412.20412), [Negative Preference Optimization](https://arxiv.org/abs/2404.05868), and [SOUL](https://aclanthology.org/2024.emnlp-main.245/).
   You will see the dominant forget-retain objective families and why second-order information can help.
4. **Representation and circuits** — [LEACE](https://arxiv.org/abs/2306.03819), [Mechanistic Unlearning](https://arxiv.org/abs/2410.12949), and [LUNAR](https://arxiv.org/abs/2502.07218).
   This step moves from output-level loss shaping to targeted subspaces, neurons, and circuits.
5. **Editing and weight-space methods** — [Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089), [LLM Surgery](https://arxiv.org/abs/2409.13054), and [NegMerge](https://arxiv.org/abs/2410.05583).
   You will see low-cost alternatives to retraining-style unlearning based on arithmetic, merging, and direct edits.
6. **Privacy and copyright** — [Can Sensitive Information Be Deleted?](https://arxiv.org/abs/2309.17410), [REVS](https://arxiv.org/abs/2406.09325), and [Obliviate](https://arxiv.org/abs/2502.15010).
   This part covers memorized strings, sensitive data, and right-to-be-forgotten use cases.
7. **Safety and reasoning** — [Safe Unlearning](https://arxiv.org/abs/2407.02855), [JPU](https://arxiv.org/abs/2601.03005), and [Reasoning Model Unlearning](https://arxiv.org/abs/2506.12963).
   You will see how unlearning is used for jailbreak defense and for deleting reasoning traces rather than only final answers.
8. **Multimodal frontier** — [MLLMU-Bench](https://arxiv.org/abs/2410.22108), [MMUNLEARNER](https://arxiv.org/abs/2502.11051), and [Relationship-Aware Safety Unlearning](https://arxiv.org/abs/2603.14185).
   This shows how the problem changes once visual concepts and cross-modal alignment enter the loop.
9. **What breaks** — [The Erasure Illusion](https://arxiv.org/abs/2512.19025), [The Unlearning Mirage](https://arxiv.org/abs/2603.11266), and [REBEL](https://arxiv.org/abs/2602.06248).
   End with the critique literature on recovery attacks, evaluation leakage, and false confidence.

## Surveys

- [Unlearning in LLMs: Methods, Evaluation, and Open Challenges](https://arxiv.org/abs/2601.13264) (2026) — Dedicated overview of LLM unlearning methods, evaluation protocols, and open research challenges.
- [A Survey on Unlearning in Large Language Models](https://arxiv.org/abs/2510.25117) (2025) — Broad survey of algorithms, targets, and trade-offs in LLM unlearning.
- [A Comprehensive Survey of Machine Unlearning Techniques for Large Language Models](https://arxiv.org/abs/2503.01854) (2025) — Reviews methodological families for LLM unlearning with emphasis on practical trade-offs and evaluation.
- [Open Problems in Machine Unlearning for AI Safety](https://arxiv.org/abs/2501.04952) (2025) — Position paper on unresolved safety questions around deletion, robustness, and deployment.
- [Machine Unlearning Doesn't Do What You Think: Lessons for Generative AI Policy, Research, and Practice](https://arxiv.org/abs/2412.06966) (2024) — Policy-oriented critique of what generative-model unlearning can and cannot guarantee.
- [Position: LLM Unlearning Benchmarks are Weak Measures of Progress](https://arxiv.org/abs/2410.02879) (2024) — Argues that current benchmarks overstate progress and under-measure robustness.
- [Preserving Privacy in Large Language Models: A Survey on Current Threats and Solutions](https://arxiv.org/abs/2408.05212) (2024) — Privacy survey covering leakage threats, defenses, and where unlearning fits among them.
- [Machine Unlearning in Generative AI: A Survey](https://arxiv.org/abs/2407.20516) (2024) — Survey of unlearning across generative models, including LLM-specific challenges.
- [Machine Unlearning for Traditional Models and Large Language Models: A Short Survey](https://arxiv.org/abs/2404.01206) (2024) — Short survey comparing classical unlearning with the distinctive issues of LLMs.
- [Digital Forgetting in Large Language Models: A Survey of Unlearning Methods](https://arxiv.org/abs/2404.02062) (2024) — Method-focused survey of digital forgetting and targeted erasure in LLMs.
- [The Frontier of Data Erasure: Machine Unlearning for Large Language Models](https://arxiv.org/abs/2403.15779) (2024) — Survey of motivations, methods, and regulatory pressure behind data erasure in LLMs.
- [Rethinking Machine Unlearning for Large Language Models](https://arxiv.org/abs/2402.08787) (2024) — Early position paper re-framing assumptions and limitations of LLM unlearning.
- [Eight Methods to Evaluate Robust Unlearning in LLMs](https://arxiv.org/abs/2402.16835) (2024) — Organizes eight complementary ways to evaluate whether forgetting is robust.
- [Knowledge Unlearning for LLMs: Tasks, Methods, and Challenges](https://arxiv.org/abs/2311.15766) (2023) — Early survey centered on knowledge-focused unlearning tasks, methods, and challenges.
- [Right to be Forgotten in the Era of Large Language Models: Implications, Challenges, and Solutions](https://arxiv.org/abs/2307.03941) (2023) — Discusses the legal and technical implications of right-to-be-forgotten requests for LLMs.

## Taxonomy

Many papers span multiple categories. The tables below are for orientation, not strict partitioning.

### By Unlearning Target

| Target                                             | Representative papers                                                                                                                    |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Factual knowledge, entities, and relations         | Who's Harry Potter?, TOFU, GONE, Entity-Level Unlearning, LLM Surgery, DUSK, Breaking Chains, FaithUn                                    |
| Privacy, PII, memorization, and copyright          | Can Sensitive Information Be Deleted?, REVS, Obliviate, GRAIL, SUV, What Should LLMs Forget?, ParaPO, To Each (Textual Sequence) Its Own |
| Safety, harmful content, jailbreaks, and backdoors | Making Harmful Behaviors Unlearnable, WMDP, Safe Unlearning, Eraser, JPU, SafeLLM, Backdoor Token Unlearning, DUP                        |
| Skills, reasoning, bias, and hallucination control | R-TOFU, Reasoning Model Unlearning, Effective Skill Unlearning, FairSISA, Bias Unlearning, STaR, Wisdom is Knowing What not to Say       |
| Multimodal concepts and cross-modal safety         | MLLMU-Bench, PULSE, MMUNLEARNER, SAFEERASER, T2VUnlearning, SAUCE, Relationship-Aware Safety Unlearning                                  |

### By Method Family

| Method family                                    | Representative papers                                                                                                                                                           |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gradient, loss, and optimization-based           | Multi-Objective LLM Unlearning, Loss Adjustment with Only Forget Data, SOUL, Gauss-Newton Unlearning, DualOptim, OFMU, BalDRO                                                   |
| Preference, distillation, and RL-based           | Negative Preference Optimization, CATNIP, RULE, DUET, RKLD, Reinforcement Unlearning via GRPO, Distillation Robustifies Unlearning                                              |
| Representation, activation, and circuit methods  | Mechanistic Unlearning, Feature-Selective Representation Misdirection, LUNAR, FALCON, Activation Signatures, KUDA, Sparse-Autoencoder-Guided Internal Representation Unlearning |
| Editing, arithmetic, and model-merging methods   | Editing Models with Task Arithmetic, NegMerge, LLM Surgery, Model State Arithmetic, CoME, Exact Unlearning via Model Merging, Per-parameter Task Arithmetic                     |
| Parameter-efficient, sparse, and modular methods | LUNE, Stable Forgetting, WAGLE, Selective Pruning, UOE, GRIP, CRISP, Soft Prompting for Unlearning                                                                              |
| Selective, continual, and data-efficient methods | FIT, SIMU, OBLIVIATE, UPCORE, ReLearn, Reveal and Release, Correcting Responses with Retrieved Exclusions, Context-Aware Unlearning                                             |

### By Modality and Setting

| Modality / setting                              | Representative papers                                                                                                                                    |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Text-only LLMs                                  | Large Language Model Unlearning, Negative Preference Optimization, Mechanistic Unlearning, REVS, SOUL, OBLIVIATE, MUDMAN                                 |
| Multilingual LLMs                               | FAME, Layer-Targeted Multilingual Knowledge Erasure, Cross-Lingual Unlearning of Selective Knowledge, Every Language Counts, Multilingual Amnesia        |
| Multimodal / VLM / MLLM                         | MLLMU-Bench, MMUNLEARNER, SAFEERASER, Visual-Guided Key-Token Regularization, MLLMEraser, SAUCE, Relationship-Aware Safety Unlearning                    |
| Federated, MoE, quantized, and at-scale systems | Oblivionis, Hierarchical Federated Unlearning, UOE, GRIP, Quantization-Robust LLM Unlearning, QUAIL, Unlearning at Scale                                 |
| Domain-specific deployments                     | Recommendation Unlearning, Large Language Model Unlearning for Source Code, Scrub It Out!, MedForget, Tool Unlearning, Climate Misinformation Unlearning |

### By Evaluation Focus

| Evaluation focus                         | Representative papers                                                                                                                                               |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Forget quality and retain quality        | TOFU, MUSE, BLUR, LUME, OpenUnlearning, Practical Unlearning, GRU                                                                                                   |
| Robustness, recovery, and relearning     | The Erasure Illusion, The Unlearning Mirage, REBEL, Leak@$k$, Harry Potter is Still Here!, Layered Unlearning for Adversarial Relearning                            |
| Privacy and memorization auditing        | InfoRMIA, Hubble, What Should LLMs Forget?, Auditing via Information Decomposition, WaterDrum, Intrinsic Evaluation of Unlearning Using Parametric Knowledge Traces |
| Safety and harmful-capability evaluation | WMDP, Guardrail Baselines, SafeLLM, JPU, OFFSIDE, A Comprehensive Evaluation under Multi-Turn Interaction                                                           |
| Efficiency and scalability               | OpenUnlearning, Machine Unlearning Comparator, Quantization-Robust LLM Unlearning, GRIP, Stable Forgetting, DUET                                                    |

## Foundations and Precursors

### Decoding-time and anti-model precursors

- [DExperts: Decoding-Time Controlled Text Generation with Experts and Anti-Experts](https://arxiv.org/abs/2105.03023) (2021) — Uses expert and anti-expert decoding to suppress unwanted generations at inference time without retraining the base model. [[code](https://github.com/alisawuffles/DExperts)]
- [Quark: Controllable Text Generation with Reinforced Unlearning](https://arxiv.org/abs/2205.13636) (2022) — Uses reinforcement learning with anti-preference signals to steer generation away from unwanted behaviors. [[code](https://github.com/GXimingLu/Quark)]
- [The CRINGE Loss: Learning what language not to model](https://arxiv.org/abs/2211.05826) (2022) — Introduces a loss that explicitly discourages undesired language, anticipating later negative-objective unlearning methods.

### Editing, arithmetic, and general unlearning precursors

- [Knowledge Unlearning for Mitigating Privacy Risks in Language Models](https://arxiv.org/abs/2210.01504) (2022) — Studies sequence-level deletion in language models as a way to reduce privacy leakage from memorized text. [[code](https://github.com/joeljang/knowledge-unlearning)]
- [Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089) (2022) — Early precursor connecting weight arithmetic and editing to targeted forgetting. [[code](https://github.com/mlfoundations/task_vectors)]
- [Privacy Adhering Machine Un-learning in NLP](https://arxiv.org/abs/2212.09573) (2022) — Frames NLP unlearning as a privacy-compliance problem and explores removal of sensitive sequences under utility constraints.
- [KGA: A General Machine Unlearning Framework Based on Knowledge Gap Alignment](https://arxiv.org/abs/2305.06535) (2023) — Aligns the “knowledge gap” between forget and retain data so the model sheds target information without broad drift. [[code](https://github.com/Lingzhi-WANG/KGAUnlearn)]
- [Composing Parameter-Efficient Modules with Arithmetic Operations](https://arxiv.org/abs/2306.14870) (2023) — Shows that arithmetic over parameter-efficient modules can add or subtract behaviors, foreshadowing modular unlearning. [[code](https://github.com/hkust-nlp/PEM_composition)]
- [LEACE: Perfect linear concept erasure in closed form](https://arxiv.org/abs/2306.03819) (2023) — Closed-form linear concept erasure method that influenced later targeted unlearning work. [[code](https://github.com/EleutherAI/concept-erasure)]
- [Fast Model Debias with Machine Unlearning](https://arxiv.org/abs/2310.12560) (2023) — Applies unlearning as a fast post-hoc debiasing tool, showing deletion-style updates can mitigate social bias without full retraining.
- [In-Context Unlearning: Language Models as Few Shot Unlearners](https://arxiv.org/abs/2310.07579) (2023) — Shows that prompting alone can simulate limited unlearning behavior without changing weights. [[code](https://github.com/MartinPawel/In-Context-Unlearning)]
- [Large Language Model Unlearning](https://arxiv.org/abs/2310.10683) (2023) — One of the first dedicated LLM unlearning papers, framing forget-retain optimization for generative models. [[code](https://github.com/kevinyaobytedance/llm_unlearn)]
- [Unlearn What You Want to Forget: Efficient Unlearning for LLMs](https://aclanthology.org/2023.emnlp-main.738/) (2023) — Improves efficiency by concentrating updates on the forget set instead of broadly re-optimizing the whole model. [[code](https://github.com/SALT-NLP/Efficient_Unlearning/)]
- [Who's Harry Potter? Approximate Unlearning in LLMs](https://arxiv.org/abs/2310.02238) (2023) — Early targeted-forgetting study showing how approximate unlearning behaves on entity-level knowledge in LLMs.
- [Forgetting before Learning: Utilizing Parametric Arithmetic for Knowledge Updating in Large Language Models](https://arxiv.org/abs/2311.08011) (2023) — Uses parameter arithmetic to subtract stale knowledge before adding updated facts, linking updating and unlearning.

## Core LLM Unlearning Papers

### Gradient, objective, and optimization-based methods

- [Gauss-Newton Unlearning for the LLM Era](https://arxiv.org/abs/2602.10568) (2026) — Uses Gauss-Newton curvature information to make forget updates stronger on target data and milder on retained behavior.
- [AGT^AO: Robust and Stabilized LLM Unlearning via Adversarial Gating Training with Adaptive Orthogonality](https://arxiv.org/abs/2602.01703) (2026) — Combines adversarial gating with adaptive orthogonality constraints to isolate forget updates from retain updates. [[code](https://github.com/TiezMind/AGT-unlearning)]
- [Maximizing Local Entropy Where It Matters: Prefix-Aware Localized LLM Unlearning](https://arxiv.org/abs/2601.03190) (2026) — Raises entropy only on targeted prefixes so forgetting stays localized to specific prompt continuations instead of spilling globally.
- [BalDRO: A Distributionally Robust Optimization based Framework for Large Language Model Unlearning](https://arxiv.org/abs/2601.09172) (2026) — Casts unlearning as a worst-case distributional optimization problem to improve robustness under shifted forget prompts.
- [FROC: A Unified Framework with Risk-Optimized Control for Machine Unlearning in LLMs](https://arxiv.org/abs/2512.13337) (2025) — Introduces explicit risk-control terms to tune the trade-off between target removal, retained utility, and harmful side effects.
- [Forgetting-MarI: LLM Unlearning via Marginal Information Regularization](https://arxiv.org/abs/2511.11914) (2025) — Regularizes marginal information carried by forget examples rather than only pushing down their token likelihood.
- [Label Smoothing Improves Gradient Ascent in LLM Unlearning](https://arxiv.org/abs/2510.22376) (2025) — Shows that smoothing forget targets stabilizes gradient-ascent unlearning and reduces overconfident collapse.
- [Downgrade to Upgrade: Optimizer Simplification Enhances Robustness in LLM Unlearning](https://arxiv.org/abs/2510.00761) (2025) — Finds that simpler optimizers can outperform heavier training recipes when robustness matters more than raw forget score.
- [OFMU: Optimization-Driven Framework for Machine Unlearning](https://arxiv.org/abs/2509.22483) (2025) — Presents a general optimization template that unifies several LLM unlearning objectives under one framework.
- [Dual-Space Smoothness for Robust and Balanced LLM Unlearning](https://arxiv.org/abs/2509.23362) (2025) — Adds smoothness constraints in both parameter and output space to keep forgetting stable under perturbation.
- [Direct Token Optimization: A Self-contained Approach to Large Language Model Unlearning](https://arxiv.org/abs/2510.00125) (2025) — Optimizes the probabilities of target tokens directly, avoiding reliance on external preference labels or teachers.
- [Beyond Sharp Minima: Robust LLM Unlearning via Feedback-Guided Multi-Point Optimization](https://arxiv.org/abs/2509.20230) (2025) — Uses multi-point optimization guided by feedback to avoid brittle sharp minima that later leak forgotten content.
- [LLM Unlearning using Gradient Ratio-Based Influence Estimation and Noise Injection](https://arxiv.org/abs/2508.06467) (2025) — Reweights updates using gradient-ratio influence estimates and injects noise to separate forget effects from collateral damage.
- [Robust LLM Unlearning with MUDMAN: Meta-Unlearning with Disruption Masking And Normalization](https://arxiv.org/abs/2506.12484) (2025) — Uses meta-unlearning plus disruption masks to concentrate changes on forget-relevant directions while normalizing away drift.
- [LLM Unlearning Should Be Form-Independent](https://arxiv.org/abs/2506.07795) (2025) — Argues that genuine forgetting should survive paraphrases, formatting changes, and other superficial prompt variations.
- [Constrained Entropic Unlearning: A Primal-Dual Framework for Large Language Models](https://arxiv.org/abs/2506.05314) (2025) — Uses a primal-dual entropy-constrained objective to prevent forget updates from flattening the whole model.
- [BLUR: A Bi-Level Optimization Approach for LLM Unlearning](https://arxiv.org/abs/2506.08164) (2025) — Solves forgetting and retention in a bi-level loop so the retain objective explicitly reacts to each forget step.
- [UniErase: Unlearning Token as a Universal Erasure Primitive for Language Models](https://arxiv.org/abs/2505.15674) (2025) — Introduces a learned unlearning token that can trigger erasure behavior across many prompts and deletion targets. [[code](https://github.com/Ymm-cll/UniErase)]
- [SEPS: A Separability Measure for Robust Unlearning in LLMs](https://arxiv.org/abs/2505.14832) (2025) — Proposes a separability score for diagnosing when forget and retain data can be cleanly split before training.
- [Graceful Forgetting in Generative Language Models](https://arxiv.org/abs/2505.19715) (2025) — Seeks controlled degradation of target knowledge rather than abrupt catastrophic forgetting that harms nearby capabilities.
- [GUARD: Generation-time LLM Unlearning via Adaptive Restriction and Detection](https://arxiv.org/abs/2505.13312) (2025) — Shifts unlearning to inference time by detecting risky generations and adaptively restricting only those outputs.
- [Exploring Criteria of Loss Reweighting to Enhance LLM Unlearning](https://arxiv.org/abs/2505.11953) (2025) — Compares different loss-reweighting rules to decide which forget examples should dominate optimization. [[code](https://github.com/Puning97/SatImp-for-LLM-Unlearning)]
- [DualOptim: Enhancing Efficacy and Stability in Machine Unlearning with Dual Optimizers](https://arxiv.org/abs/2504.15827) (2025) — Uses separate optimizers for forget and retain objectives to reduce gradient conflict during training.
- [CE-U: Cross Entropy Unlearning](https://arxiv.org/abs/2503.01224) (2025) — Recasts unlearning as a cross-entropy objective that lowers confidence on target outputs without unstable ascent.
- [A General Framework to Enhance Fine-tuning-based LLM Unlearning](https://arxiv.org/abs/2502.17823) (2025) — Adds reusable components that strengthen existing fine-tuning-based unlearning methods rather than proposing a single new loss. [[code](https://github.com/renjie3/GRUN)]
- [Multi-Objective Large Language Model Unlearning](https://arxiv.org/abs/2412.20412) (2024) — Formulates forgetting and retention as coupled objectives rather than a single scalar loss.
- [Unlearning in- vs. out-of-distribution data in LLMs under gradient-based method](https://arxiv.org/abs/2411.04388) (2024) — Compares how gradient-based unlearning behaves on in-distribution forget sets versus harder out-of-distribution targets.
- [MUNBa: Machine Unlearning via Nash Bargaining](https://arxiv.org/abs/2411.15537) (2024) — Uses Nash bargaining to negotiate between forget quality and retained utility instead of hand-tuned scalar weights.
- [Unlearning as multi-task optimization: A normalized gradient difference approach with an adaptive learning rate](https://arxiv.org/abs/2410.22086) (2024) — Treats forgetting and retention as multitask learning and reconciles them with normalized gradient differences.
- [LLM Unlearning via Loss Adjustment with Only Forget Data](https://arxiv.org/abs/2410.11143) (2024) — Designs a forget-only objective so unlearning can proceed even when no retain set is available.
- [Cross-model Control: Improving Multiple Large Language Models in One-time Training](https://arxiv.org/abs/2410.17599) (2024) — Uses a single control-style training process to steer several LLMs at once, including targeted forgetting behavior.
- [WPN: An Unlearning Method Based on N-pair Contrastive Learning in Language Models](https://arxiv.org/abs/2408.09459) (2024) — Uses N-pair contrastive learning to push forget representations away from retain representations more cleanly.
- [Toward Robust Unlearning for LLMs](https://openreview.net/forum?id=4rPzaUF6Ej) (2024) — Focuses on robustness-oriented training and evaluation rather than optimizing only standard forget metrics.
- [Machine Unlearning in Large Language Models](https://arxiv.org/abs/2405.15152) (2024) — Empirically studies practical LLM unlearning trade-offs across methods, utility, and deployment cost.
- [SOUL: Unlocking the Power of Second-Order Optimization for LLM Unlearning](https://aclanthology.org/2024.emnlp-main.245/) (2024) — Brings second-order optimization to unlearning to better balance forgetting with utility retention. [[code](https://github.com/OPTML-Group/SOUL)]
- [Machine Unlearning in Large Language Models](https://arxiv.org/abs/2404.16841) (2024) — Early broad comparison of baseline unlearning objectives and their forget-retain trade-offs on modern LLMs.
- [Second-Order Information Matters: Revisiting Machine Unlearning for Large Language Models](https://arxiv.org/abs/2403.10557) (2024) — Revisits LLM unlearning through Hessian-aware analysis and shows curvature information materially changes outcomes.
- [Ethos: Rectifying Language Models in Orthogonal Parameter Space](https://arxiv.org/abs/2403.08994) (2024) — Constrains updates to an orthogonal parameter subspace so target forgetting interferes less with retained knowledge.
- [Machine Unlearning of Pre-trained Large Language Models](https://arxiv.org/abs/2402.15159) (2024) — Studies how to apply unlearning at the pretraining stage instead of only after instruction tuning. [[code](https://github.com/yaojin17/Unlearning_LLM)]

### Preference, distillation, and RL-based unlearning

- [CATNIP: LLM Unlearning via Calibrated and Tokenized Negative Preference Alignment](https://arxiv.org/abs/2602.02824) (2026) — Tokenizes negative preferences and calibrates their strength to avoid the collapse seen in naive preference-based forgetting.
- [Reinforcement Unlearning via Group Relative Policy Optimization](https://arxiv.org/abs/2601.20568) (2026) — Uses GRPO-style rewards to optimize a forget-retain frontier with online policy updates instead of static supervised loss.
- [DUET: Distilled LLM Unlearning from an Efficiently Contextualized Teacher](https://arxiv.org/abs/2601.21283) (2026) — Distills forgetting behavior from a teacher that is contextualized to know when the deletion target is active.
- [Explainable reinforcement learning from human feedback to improve alignment](https://arxiv.org/abs/2512.13837) (2025) — Adds interpretable RLHF-style feedback so alignment and unlearning decisions are easier to inspect and debug.
- [Distribution Preference Optimization: A Fine-grained Perspective for LLM Unlearning](https://arxiv.org/abs/2510.04773) (2025) — Optimizes over distributions of preferred and dispreferred outputs rather than single preferred responses.
- [RULE: Reinforcement UnLEarning Achieves Forget-Retain Pareto Optimality](https://arxiv.org/abs/2506.07171) (2025) — Uses reinforcement learning to explicitly search the Pareto frontier between forgetting strength and retained utility.
- [Distillation Robustifies Unlearning](https://arxiv.org/abs/2506.06278) (2025) — Shows that distillation from a reference model can make forgetting harder to reverse while preserving downstream quality.
- [Unilogit: Robust Machine Unlearning for LLMs Using Uniform-Target Self-Distillation](https://arxiv.org/abs/2505.06027) (2025) — Applies self-distillation toward uniform targets so forget examples lose sharp preference peaks without broad damage.
- [Bridging the Gap Between Preference Alignment and Machine Unlearning](https://arxiv.org/abs/2504.06659) (2025) — Recasts unlearning as a special case of preference alignment and compares the two views under one framework.
- [A mean teacher algorithm for unlearning of language models](https://arxiv.org/abs/2504.13388) (2025) — Uses an EMA mean-teacher model to stabilize student unlearning updates over training.
- [Simplicity Prevails: Rethinking Negative Preference Optimization for LLM Unlearning](https://arxiv.org/abs/2410.07163) (2024) — Shows that simpler NPO variants can outperform more elaborate formulations on both utility and robustness. [[code](https://github.com/OPTML-Group/Unlearn-Simple)]
- [Alternate Preference Optimization for Unlearning Factual Knowledge in Large Language Models](https://aclanthology.org/2025.coling-main.252/) (2024) — Alternates opposing preference steps to forget factual targets without letting either objective dominate for too long. [[code](https://github.com/molereddy/Alternate-Preference-Optimization/tree/main)]
- [RKLD: Reverse KL-Divergence-based Knowledge Distillation for Unlearning Personal Information in Large Language Models](https://arxiv.org/abs/2406.01983) (2024) — Uses reverse-KL distillation to suppress personal-information outputs while keeping non-sensitive generations close to the teacher.
- [Negative Preference Optimization: From Catastrophic Collapse to Effective Unlearning](https://arxiv.org/abs/2404.05868) (2024) — Turns preference optimization into a practical forget-retain objective and analyzes why naive NPO collapses. [[code](https://github.com/licong-lin/negative-preference-optimization)]
- [Unmemorization in Large Language Models via Self-Distillation and Deliberate Imagination](https://arxiv.org/abs/2402.10052) (2024) — Pairs self-distillation with deliberately imagined counterexamples to erase memorized content beyond exact training strings. [[code](https://github.com/dong-river/LLM_unlearning)]

### Representation, activation, and circuit-based methods

- [Attention Smoothing Is All You Need For Unlearning](https://arxiv.org/abs/2603.01285) (2026) — Smooths attention patterns so target cues no longer trigger sharp retrieval of forgotten content.
- [MeGU: Machine-Guided Unlearning with Target Feature Disentanglement](https://arxiv.org/abs/2602.17088) (2026) — Disentangles target features from shared features before removal so forgetting is more selective.
- [From Logits to Latents: Contrastive Representation Shaping for LLM Unlearning](https://arxiv.org/abs/2601.22028) (2026) — Moves the unlearning signal from output logits into latent space via contrastive representation shaping.
- [ForgetMark: Stealthy Fingerprint Embedding via Targeted Unlearning in Language Models](https://arxiv.org/abs/2601.08189) (2026) — Uses targeted unlearning as a vehicle for embedding a hidden model fingerprint in downstream behavior. [[code](https://github.com/Xuzhenhua55/ForgetMark)]
- [Feature-Selective Representation Misdirection for Machine Unlearning](https://arxiv.org/abs/2512.16297) (2025) — Redirects only the feature channels most tied to the forget set instead of disturbing all representations.
- [Geometric-disentangelment Unlearning](https://arxiv.org/abs/2511.17100) (2025) — Separates forget and retain manifolds geometrically before applying the deletion update. [[code](https://github.com/Lemutisme/Geometric-Unlearning)]
- [Forgetting to Forget: Attention Sink as A Gateway for Backdooring LLM Unlearning](https://arxiv.org/abs/2510.17021) (2025) — Shows that attention-sink behavior can be exploited to backdoor representation-level unlearning methods.
- [Sparse-Autoencoder-Guided Internal Representation Unlearning for Large Language Models](https://arxiv.org/abs/2509.15631) (2025) — Uses SAE features to identify and erase internal components associated with target knowledge.
- [Erase or Hide? Suppressing Spurious Unlearning Neurons for Robust Unlearning](https://arxiv.org/abs/2509.22263) (2025) — Distinguishes genuinely causal forget neurons from spurious ones that merely hide recoverable knowledge.
- [Collapse of Irrelevant Representations (CIR) Ensures Robust and Non-Disruptive LLM Unlearning](https://arxiv.org/abs/2509.11816) (2025) — Collapses irrelevant representation subspaces so target forgetting does not ripple into useful behavior.
- [CLUE: Conflict-guided Localization for LLM Unlearning Framework](https://arxiv.org/abs/2509.20977) (2025) — Localizes where forget and retain gradients conflict, then applies interventions only in those regions.
- [CRISP: Persistent Concept Unlearning via Sparse Autoencoders](https://arxiv.org/abs/2508.13650) (2025) — Uses sparse autoencoders to persistently remove concept features that would otherwise reappear after fine-tuning.
- [Align-then-Unlearn: Embedding Alignment for LLM Unlearning](https://arxiv.org/abs/2506.13181) (2025) — Aligns embeddings across data first, then deletes targets in that aligned space to reduce collateral drift.
- [Model Unlearning via Sparse Autoencoder Subspace Guided Projections](https://arxiv.org/abs/2505.24428) (2025) — Projects model states away from SAE-identified forget subspaces instead of relying on generic gradient ascent.
- [SAEs $\textit{Can}$ Improve Unlearning: Dynamic Sparse Autoencoder Guardrails for Precision Unlearning in LLMs](https://arxiv.org/abs/2504.08192) (2025) — Uses dynamic SAE guardrails that activate only when risky concepts are detected. [[code](https://github.com/aashiqmuhamed/DynamicSAEGuardrails)]
- [Don't Forget It! Conditional Sparse Autoencoder Clamping Works for Unlearning](https://arxiv.org/abs/2503.11127) (2025) — Conditionally clamps SAE features only in target contexts, making deletion more precise than always-on suppression.
- [Deep Contrastive Unlearning for Language Models](https://arxiv.org/abs/2503.14900) (2025) — Uses deep contrastive objectives across layers to separate forget and retain trajectories.
- [LUNAR: LLM Unlearning via Neural Activation Redirection](https://arxiv.org/abs/2502.07218) (2025) — Redirects activations away from target pathways rather than retraining the whole model toward generic refusal.
- [FALCON: Fine-grained Activation Manipulation by Contrastive Orthogonal Unalignment for Large Language Model](https://arxiv.org/abs/2502.01472) (2025) — Orthogonalizes contrastive activation shifts so the forget update stays fine-grained and localized.
- [Improving the Robustness of Representation Misdirection for Large Language Model Unlearning](https://arxiv.org/abs/2501.19202) (2025) — Hardens representation-misdirection methods against paraphrase and recovery attacks that expose hidden knowledge.
- [Applying sparse autoencoders to unlearn knowledge in language models](https://arxiv.org/abs/2410.19278) (2024) — Early study showing SAE features can serve as interpretable handles for targeted knowledge removal.
- [On Effects of Steering Latent Representation for Large Language Model Unlearning](https://arxiv.org/abs/2408.06223) (2024) — Analyzes how latent-steering interventions affect both forget quality and unintended side effects.
- [Large Language Model Unlearning via Embedding-Corrupted Prompts](https://arxiv.org/abs/2406.07933) (2024) — Uses deliberately corrupted prompt embeddings to trigger and train deletion behavior around target content. [[code](https://github.com/chrisliu298/llm-unlearn-eco)]

- [Decoupling Memories, Muting Neurons: Towards Practical Machine Unlearning for Large Language Models](https://aclanthology.org/2025.findings-acl.719/) (2025) — NeuMuter decouples memorization and mutes about 1% of FFN neurons to forget target data while preserving downstream utility.
### Editing, task arithmetic, and weight-space methods

- [Per-parameter Task Arithmetic for Unlearning in Large Language Models](https://arxiv.org/abs/2601.22030) (2026) — Applies task arithmetic at per-parameter granularity so each weight gets its own subtraction strength.
- [Investigating Model Editing for Unlearning in Large Language Models](https://arxiv.org/abs/2512.20794) (2025) — Systematically tests whether model-editing algorithms are strong baselines for unlearning tasks.
- [UCD: Unlearning in LLMs via Contrastive Decoding](https://arxiv.org/abs/2506.12097) (2025) — Uses contrastive decoding to suppress forgotten continuations at generation time without full retraining.
- [Model State Arithmetic for Machine Unlearning](https://arxiv.org/abs/2506.20941) (2025) — Treats checkpoints as state vectors and subtracts the component attributable to unwanted training data.
- [Exact Unlearning of Finetuning Data via Model Merging at Scale](https://arxiv.org/abs/2504.04626) (2025) — Uses checkpoint merging to exactly cancel fine-tuning-data contributions at larger model scales.
- [Resolving Editing-Unlearning Conflicts: A Knowledge Codebook Framework for Large Language Model Updating](https://arxiv.org/abs/2502.00158) (2025) — Introduces a codebook representation to keep new edits from interfering with deletion requests.
- [CoME: An Unlearning-based Approach to Conflict-free Model Editing](https://arxiv.org/abs/2502.15826) (2025) — Reframes conflict-free model editing as a controlled unlearning problem. [[code](https://github.com/ekgus9/COME)]
- [NegMerge: Consensual Weight Negation for Strong Machine Unlearning](https://arxiv.org/abs/2410.05583) (2024) — Uses weight negation across checkpoints to subtract unwanted capabilities in a merge-based pipeline. [[code](https://github.com/naver-ai/negmerge)]
- [Composable Interventions for Language Models](https://arxiv.org/abs/2407.06483) (2024) — Builds modular intervention vectors that can be combined to add, remove, or isolate specific behaviors. [[code](https://github.com/hartvigsen-group/composable-interventions)]
- [Split, Unlearn, Merge: Leveraging Data Attributes for More Effective Unlearning in LLMs](https://arxiv.org/abs/2406.11780) (2024) — Splits data by attributes before deletion and merges the results to reduce interference across targets.
- [Offset Unlearning for Large Language Models](https://arxiv.org/abs/2404.11045) (2024) — Learns offset vectors in weight space that subtract target behavior with minimal full-model retraining. [[code](https://github.com/luka-group/Delta-Unlearning)]

- [Precise In-Parameter Concept Erasure in Large Language Models](https://aclanthology.org/2025.emnlp-main.960/) (2025) — PISCES performs targeted concept erasure directly in parameter space to remove undesirable knowledge with less collateral damage. [[code](https://github.com/yoavgur/PISCES)]
### Parameter-efficient, sparse, and modular methods

- [ALTER: Asymmetric LoRA for Token-Entropy-Guided Unlearning of LLMs](https://arxiv.org/abs/2603.01792) (2026) — Uses asymmetric LoRA updates guided by token entropy so forgetting focuses on high-certainty target regions.
- [Sparsity-Aware Unlearning for Large Language Models](https://arxiv.org/abs/2602.00577) (2026) — Uses sparsity masks to confine forgetting to a small subset of parameters implicated in the target data.
- [LUNE: Efficient LLM Unlearning via LoRA Fine-Tuning with Negative Examples](https://arxiv.org/abs/2512.07375) (2025) — Uses LoRA plus explicit negative forget examples to make deletion cheap and modular.
- [Stable Forgetting: Bounded Parameter-Efficient Unlearning in LLMs](https://arxiv.org/abs/2509.24166) (2025) — Binds parameter-efficient updates within safe ranges so repeated unlearning stays stable over time.
- [LLM Unlearning Without an Expert Curated Dataset](https://arxiv.org/abs/2508.06595) (2025) — Removes dependence on hand-curated forget sets by deriving unlearning signals from cheaper data sources.
- [Improving Fisher Information Estimation and Efficiency for LoRA-based LLM Unlearning](https://arxiv.org/abs/2508.21300) (2025) — Improves Fisher estimation so LoRA-based approximate unlearning better targets parameters that actually matter.
- [Unified Parameter-Efficient Unlearning for LLMs](https://arxiv.org/abs/2412.00383) (2024) — Provides a common framework for comparing lightweight unlearning modules such as LoRA and prompts.
- [WAGLE: Strategic Weight Attribution for Effective and Modular Unlearning in Large Language Models](https://arxiv.org/abs/2410.17509) (2024) — Attributes deletion responsibility to a strategic subset of weights, making modular unlearning more targeted. [[code](https://github.com/OPTML-Group/WAGLE)]
- [Targeted Unlearning with Single Layer Unlearning Gradient](https://arxiv.org/abs/2407.11867) (2024) — Restricts forget gradients to a single layer to test how local the necessary deletion signal can be.
- [Soft Prompting for Unlearning in Large Language Models](https://arxiv.org/abs/2406.12038) (2024) — Learns soft prompts that induce forgetting behavior without directly editing the base parameters. [[code](https://github.com/karuna-bhaila/llm_unlearning)]
- [Dissecting Language Models: Machine Unlearning via Selective Pruning](https://arxiv.org/abs/2403.01267) (2024) — Removes target knowledge by pruning the parameters most implicated in the forget set.
- [Separate the Wheat from the Chaff: Model Deficiency Unlearning via Parameter-Efficient Module Operation](https://arxiv.org/abs/2308.08090) (2023) — Uses parameter-efficient modules to separate defective behavior from useful ability before removing only the former. [[code](https://github.com/HITsz-TMG/Ext-Sub)]

- [LLM-Eraser: Optimizing Large Language Model Unlearning through Selective Pruning](https://dl.acm.org/doi/10.1145/3690624.3709312) (2025) — Uses selective pruning as the main unlearning mechanism to improve forgetting efficiency while preserving retained behavior. [[code](https://github.com/mmichaelzhang/LLM-Eraser)]
- [UUE: Untargeted Language Model Unlearning via Null-Space-Guided Editing with Lightweight Adapters](https://openreview.net/forum?id=nQjj5bpLui) (2026) — Reframes untargeted LLM unlearning as null-space-guided editing with pluggable adapters and a LoRA variant.
### Selective, continual, and data-efficient methods

- [From Domains to Instances: Dual-Granularity Data Synthesis for LLM Unlearning](https://arxiv.org/abs/2601.04278) (2026) — Synthesizes deletion data at both domain and instance level so unlearning can scale beyond hand-collected forget sets.
- [Forgetting Similar Samples: Can Machine Unlearning Do it Better?](https://arxiv.org/abs/2601.06938) (2026) — Studies how well unlearning separates a target example from highly similar neighbors that should remain.
- [FIT: Defying Catastrophic Forgetting in Continual LLM Unlearning](https://arxiv.org/abs/2601.21682) (2026) — Tackles repeated deletion requests by preventing catastrophic loss of retained knowledge across unlearning rounds.
- [Recover-to-Forget: Gradient Reconstruction from LoRA for Efficient LLM Unlearning](https://arxiv.org/abs/2512.07374) (2025) — Reconstructs approximate gradients from LoRA adapters so unlearning can be done after the fact with low cost.
- [RapidUn: Influence-Driven Parameter Reweighting for Efficient Large Language Model Unlearning](https://arxiv.org/abs/2512.04457) (2025) — Uses influence estimates to quickly reweight the parameters most responsible for the forget set.
- [SIMU: Selective Influence Machine Unlearning](https://arxiv.org/abs/2510.07822) (2025) — Uses selective influence estimates to update only the parameter regions most affected by forgotten data.
- [LLM Unlearning on Noisy Forget Sets: A Study of Incomplete, Rewritten, and Watermarked Data](https://arxiv.org/abs/2510.09007) (2025) — Evaluates deletion when the forget set is incomplete, paraphrased, or watermarked rather than cleanly labeled.
- [Forget to Know, Remember to Use: Context-Aware Unlearning for Large Language Models](https://arxiv.org/abs/2510.17620) (2025) — Makes forgetting conditional on context so knowledge can be suppressed only in disallowed uses.
- [Unlearning That Lasts: Utility-Preserving, Robust, and Almost Irreversible Forgetting in LLMs](https://arxiv.org/abs/2509.02820) (2025) — Aims for deletion that is difficult to relearn while still maintaining strong retained performance.
- [Scalable and Robust LLM Unlearning by Correcting Responses with Retrieved Exclusions](https://arxiv.org/abs/2509.25973) (2025) — Uses retrieval of exclusion evidence to correct responses at scale instead of relying solely on weight updates.
- [Reveal and Release: Iterative LLM Unlearning with Self-generated Data](https://arxiv.org/abs/2509.14624) (2025) — Bootstraps new forget examples from the model itself and iterates deletion over those self-generated traces.
- [GUARD: Guided Unlearning and Retention via Data Attribution for Large Language Models](https://arxiv.org/abs/2506.10946) (2025) — Uses data attribution to decide which examples should drive forgetting and which should protect utility.
- [OBLIVIATE: Robust and Practical Machine Unlearning for Large Language Models](https://arxiv.org/abs/2505.04416) (2025) — Focuses on an end-to-end recipe that is practical to deploy while still remaining robust to stronger evaluation. [[code](https://anonymous.4open.science/r/OBLIVIATE_unlearning_LLM-0C84)]
- [DP2Unlearning: An Efficient and Guaranteed Unlearning Framework for LLMs](https://arxiv.org/abs/2504.13774) (2025) — Pairs efficient update rules with stated unlearning guarantees rather than relying only on empirical forget scores.
- [GRU: Mitigating the Trade-off between Unlearning and Retention for Large Language Models](https://arxiv.org/abs/2503.09117) (2025) — Rebalances forget and retain gradients to reduce the utility loss usually paid for stronger deletion.
- [UPCORE: Utility-Preserving Coreset Selection for Balanced Unlearning](https://arxiv.org/abs/2502.15082) (2025) — Chooses a small retain coreset that best protects utility during deletion. [[code](https://github.com/Vaidehi99/UPCORE)]
- [ReLearn: Unlearning via Learning for Large Language Models](https://arxiv.org/abs/2502.11190) (2025) — Recasts deletion as learning corrective behaviors from constructed data rather than only maximizing forget loss. [[code](https://github.com/zjunlp/unlearn)]
- [Practical Unlearning for Large Language Models](https://arxiv.org/abs/2407.10223) (2024) — Emphasizes deployable choices of data, compute, and objectives rather than idealized benchmark performance alone.
- [Learn while Unlearn: An Iterative Unlearning Framework for Generative Language Models](https://arxiv.org/abs/2407.20271) (2024) — Alternates deletion and relearning phases so utility can be restored as forgetting proceeds. [[code](https://github.com/himalalps/ICU)]
- [Can Small Language Models Learn, Unlearn, and Retain Noise Patterns?](https://arxiv.org/abs/2407.00996) (2024) — Uses synthetic noise patterns to isolate the basic learn–unlearn–retain dynamics in smaller models.
- [Unlearning with Control: Assessing Real-world Utility for Large Language Model Unlearning](https://arxiv.org/abs/2406.09179) (2024) — Evaluates deletion under explicit downstream control and utility constraints rather than pure benchmark scores.
- [Reversing the Forget-Retain Objectives: An Efficient LLM Unlearning Framework from Logit Difference](https://arxiv.org/abs/2406.08607) (2024) — Uses a logit-difference objective obtained by reversing the usual forget/retain roles. [[code](https://github.com/UCSB-NLP-Chang/ULD)]
- [To Each (Textual Sequence) Its Own: Improving Memorized-Data Unlearning in Large Language Models](https://arxiv.org/abs/2405.03097) (2024) — Targets memorized sequences one by one, rather than treating all forget data as a single broad concept.
- [Selective Forgetting: Advancing Machine Unlearning Techniques and Evaluation in Language Models](https://arxiv.org/abs/2402.05813) (2024) — Pushes selective deletion as the central setting and pairs it with stronger evaluation than all-or-nothing forgetting.

- [Adaptive Localization of Knowledge Negation for Continual LLM Unlearning](https://proceedings.mlr.press/v267/wuerkaixi25a.html) (2025) — ALKN sparsifies gradients and adapts negation strength to improve continual unlearning without over-editing retained knowledge.
- [Orthogonal Gradient Projection for Continual LLM Unlearning](https://openreview.net/forum?id=lb6Ce20kl5) (2026) — ONPO orthogonalizes successive forget updates to reduce interference in continual unlearning.
- [Effective Unlearning in LLMs Relies on the Right Data Retention Strategy](https://openreview.net/forum?id=EyXBv291ST) (2026) — Systematic study of retain-set selection, showing that the data-retention strategy strongly affects practical LLM unlearning quality and utility.
## Unlearning Targets and Threat Models

### Factual knowledge, entities, and structural memory

- [ROKA: Robust Knowledge Unlearning against Adversaries](https://arxiv.org/abs/2603.00436) (2026) — Targets factual deletion under adversarial probing so forgotten entities are harder to recover with attacks.
- [GONE: Structural Knowledge Unlearning via Neighborhood-Expanded Distribution Shaping](https://arxiv.org/abs/2603.12275) (2026) — Expands deletion to neighboring facts and relations so structural knowledge around a target is removed together.
- [Layer-Targeted Multilingual Knowledge Erasure in Large Language Models](https://arxiv.org/abs/2602.22562) (2026) — Erases multilingual facts by intervening at specific layers where cross-lingual knowledge is shared.
- [KUDA: Knowledge Unlearning by Deviating Representation for Large Language Models](https://arxiv.org/abs/2602.19275) (2026) — Deletes factual targets by driving representations away from their original knowledge-bearing directions.
- [Representation-Aware Unlearning via Activation Signatures: From Suppression to Knowledge-Signature Erasure](https://arxiv.org/abs/2601.10566) (2026) — Identifies activation signatures of target facts and erases the signature itself rather than just suppressing answers.
- [Multilingual Amnesia: On the Transferability of Unlearning in Multilingual LLMs](https://arxiv.org/abs/2601.05641) (2026) — Measures whether forgetting a fact in one language transfers to other languages that share the same knowledge.
- [Consistency-Aware Editing for Entity-level Unlearning in Language Models](https://arxiv.org/abs/2601.08840) (2026) — Uses consistency-aware edits so entity deletion holds across aliases, paraphrases, and related prompts.
- [FAME: Fictional Actors for Multilingual Erasure](https://arxiv.org/abs/2512.15235) (2025) — Uses fictional actors as clean multilingual targets to study transfer of erasure across languages.
- [Beyond Superficial Forgetting: Thorough Unlearning through Knowledge Density Estimation and Block Re-insertion](https://arxiv.org/abs/2511.11667) (2025) — Estimates dense target-knowledge regions and reinserts safe blocks to deepen forgetting without broad damage.
- [Concept Unlearning in Large Language Models via Self-Constructed Knowledge Triplets](https://arxiv.org/abs/2509.15621) (2025) — Builds its own subject–relation–object triplets to expand deletion around a target concept.
- [CURE: Controlled Unlearning for Robust Embeddings -- Mitigating Conceptual Shortcuts in Pre-Trained Language Models](https://arxiv.org/abs/2509.05230) (2025) — Removes conceptual shortcuts in embeddings rather than deleting only a handful of isolated facts.
- [Surgical Knowledge Rewrite in Compact LLMs: An 'Unlearn-then-Learn' Strategy with ($IA^3$) for Localized Factual Modulation and Catastrophic Forgetting Mitigation](https://arxiv.org/abs/2508.07075) (2025) — Uses $IA^3$ adapters to first erase a localized fact and then carefully reintroduce safe context in compact models.
- [Editing as Unlearning: Are Knowledge Editing Methods Strong Baselines for Large Language Model Unlearning?](https://arxiv.org/abs/2505.19855) (2025) — Tests whether editing methods already solve much of factual unlearning without specialized deletion objectives.
- [DUSK: Do Not Unlearn Shared Knowledge](https://arxiv.org/abs/2505.15209) (2025) — Protects shared background knowledge while removing only the target entity-specific component.
- [UIPE: Enhancing LLM Unlearning by Removing Knowledge Related to Forgetting Targets](https://arxiv.org/abs/2503.04693) (2025) — Extends deletion beyond exact targets to semantically related knowledge that can regenerate the forgotten fact.
- [Which Retain Set Matters for LLM Unlearning? A Case Study on Entity Unlearning](https://arxiv.org/abs/2502.11441) (2025) — Studies how different retain-set choices change the success and collateral damage of entity deletion.
- [FaithUn: Toward Faithful Forgetting in Language Models by Investigating the Interconnectedness of Knowledge](https://arxiv.org/abs/2502.19207) (2025) — Uses knowledge interconnectedness to decide what surrounding facts must change for deletion to be faithful.
- [Erasing Without Remembering: Safeguarding Knowledge Forgetting in Large Language Models](https://arxiv.org/abs/2502.19982) (2025) — Designs a forgetting procedure that avoids repeatedly exposing the sensitive target during deletion.
- [When Machine Unlearning Meets Retrieval-Augmented Generation (RAG): Keep Secret or Forget Knowledge?](https://arxiv.org/abs/2410.15267) (2024) — Compares deleting internal model knowledge with simply hiding it behind retrieval in RAG systems.
- [Learning and Unlearning of Fabricated Knowledge in Language Models](https://arxiv.org/abs/2410.21750) (2024) — Uses fabricated facts to study controlled learn–forget cycles without contamination from real-world knowledge.
- [Erasing Conceptual Knowledge from Language Models](https://arxiv.org/abs/2410.02760) (2024) — Focuses on removing abstract concepts rather than only named entities or memorized strings.
- [CodeUnlearn: Amortized Zero-Shot Machine Unlearning in Language Models Using Discrete Concept](https://arxiv.org/abs/2410.10866) (2024) — Uses discrete concept codes to enable amortized zero-shot forgetting without retraining per target.
- [Breaking Chains: Unraveling the Links in Multi-Hop Knowledge Unlearning](https://arxiv.org/abs/2410.13274) (2024) — Examines how deleting one fact should propagate through multi-hop inference chains. [[code](https://github.com/brightjade/Munch)]
- [Answer When Needed, Forget When Not: Language Models Pretend to Forget via In-Context Knowledge Unlearning](https://arxiv.org/abs/2410.00382) (2024) — Shows that in-context prompting can induce conditional “pretend forgetting” without permanent weight edits.
- [MEOW: MEMOry Supervised LLM Unlearning Via Inverted Facts](https://arxiv.org/abs/2409.11844) (2024) — Uses inverted facts as counterfactual supervision to break recall of the original memory. [[code](https://github.com/Carol-gutianle/MEOW)]
- [LLM Surgery: Efficient Knowledge Unlearning and Editing in Large Language Models](https://arxiv.org/abs/2409.13054) (2024) — Uses surgical weight edits to remove targeted knowledge while minimizing collateral damage.
- [UNLEARN Efficient Removal of Knowledge in Large Language Models](https://arxiv.org/abs/2408.04140) (2024) — Prioritizes low-cost removal of factual knowledge with lightweight update routines.
- [Towards Robust and Cost-Efficient Knowledge Unlearning for Large Language Models](https://arxiv.org/abs/2408.06621) (2024) — Balances adversarial robustness and compute efficiency in factual knowledge deletion.
- [Towards Robust Knowledge Unlearning: An Adversarial Framework for Assessing and Improving Unlearning Robustness in Large Language Models](https://arxiv.org/abs/2408.10682) (2024) — Uses adversarial probing both to evaluate factual deletion and to train stronger unlearning methods.
- [To Forget or Not? Towards Practical Knowledge Unlearning for Large Language Models](https://arxiv.org/abs/2407.01920) (2024) — Emphasizes practical decision-making about when factual deletion is worth its cost and utility trade-offs. [[code](https://github.com/zjunlp/KnowUnDo)]
- [Unveiling Entity-Level Unlearning for Large Language Models: A Comprehensive Analysis](https://arxiv.org/abs/2406.15796) (2024) — Dissects entity-level forgetting across prompt types, targets, and evaluation settings.
- [SNAP: Unlearning Selective Knowledge in Large Language Models with Negative Instructions](https://arxiv.org/abs/2406.12329) (2024) — Uses negative instructions to teach the model which facts to suppress and which to preserve. [[code](https://github.com/brightjade/snap-unlearning)]
- [Every Language Counts: Learn and Unlearn in Multilingual LLMs](https://arxiv.org/abs/2406.13748) (2024) — Studies how adding and deleting knowledge interact across multiple languages in multilingual LLMs. [[code](https://github.com/TaiMingLu/learn-unlearn)]
- [Cross-Lingual Unlearning of Selective Knowledge in Multilingual Language Models](https://arxiv.org/abs/2406.12354) (2024) — Tests whether deleting a fact in one language generalizes to semantically equivalent prompts in others. [[code](https://github.com/brightjade/multilingual-unlearning)]
- [Large Scale Knowledge Washing](https://arxiv.org/abs/2405.16720) (2024) — Scales knowledge cleanup beyond toy entities to much broader factual distributions. [[code](https://github.com/wangyu-ustc/LargeScaleWashing)]

- [Concept Unlearning for Large Language Models](https://openreview.net/forum?id=nU7Se8oIPJ) (2024) — Frames deletion at the concept level rather than only by specific training examples, and proposes a gradient-ascent method over generated token sequences.
### Privacy, memorization, copyright, and right-to-be-forgotten

- [MPU: Towards Secure and Privacy-Preserving Knowledge Unlearning for Large Language Models](https://arxiv.org/abs/2602.23798) (2026) — Designs privacy-oriented knowledge deletion with explicit security goals and leakage-resistant evaluation. [[code](https://github.com/Tristan-SHU/MPU)]
- [UnPII: Unlearning Personally Identifiable Information with Quantifiable Exposure Risk](https://arxiv.org/abs/2601.01786) (2026) — Uses a measured exposure-risk signal to decide whether PII remains recoverable after unlearning.
- [Shadow Unlearning: A Neuro-Semantic Approach to Fidelity-Preserving Faceless Forgetting in LLMs](https://arxiv.org/abs/2601.04275) (2026) — Removes identity-bearing information while preserving fidelity of the surrounding semantic content.
- [Data-Free Privacy-Preserving for LLMs via Model Inversion and Selective Unlearning](https://arxiv.org/abs/2601.15595) (2026) — Reconstructs synthetic sensitive examples through inversion when the original private data are unavailable for deletion.
- [REMIND: Input Loss Landscapes Reveal Residual Memorization in Post-Unlearning LLMs](https://arxiv.org/abs/2511.04228) (2025) — Uses input loss landscapes to expose memorized sequences that survive supposedly successful unlearning.
- [ParaPO: Aligning Language Models to Reduce Verbatim Reproduction of Pre-training Data](https://arxiv.org/abs/2504.14452) (2025) — Uses paraphrase-aware preference optimization to reduce verbatim reproduction of pretraining text. [[code](https://github.com/chentong0/ParaPO)]
- [GRAIL: Gradient-Based Adaptive Unlearning for Privacy and Copyright in LLMs](https://arxiv.org/abs/2504.12681) (2025) — Adapts gradient-based deletion to privacy and copyright takedown requests with target-specific intensity.
- [SUV: Scalable Large Language Model Copyright Compliance with Regularized Selective Unlearning](https://arxiv.org/abs/2503.22948) (2025) — Focuses on scalable copyright compliance by selectively regularizing what must remain versus what must disappear.
- [Obliviate: Efficient Unmemorization for Protecting Intellectual Property in Large Language Models](https://arxiv.org/abs/2502.15010) (2025) — Targets memorized proprietary text with a compute-efficient unmemorization procedure.
- [A Lightweight Method to Disrupt Memorized Sequences in LLM](https://arxiv.org/abs/2502.05159) (2025) — Uses a lightweight intervention specifically aimed at breaking exact memorized token sequences.
- [Underestimated Privacy Risks for Minority Populations in Large Language Model Unlearning](https://arxiv.org/abs/2412.08559) (2024) — Shows that standard privacy-oriented unlearning can fail disproportionately for minority-group data.
- [Investigating the Feasibility of Mitigating Potential Copyright Infringement via Large Language Model Unlearning](https://arxiv.org/abs/2412.18621) (2024) — Evaluates whether unlearning can realistically satisfy copyright takedown goals for LLM outputs. [[code](https://github.com/guangyaodou/SSU_Unlearn)]
- [Mitigating Memorization In Language Models](https://arxiv.org/abs/2410.02159) (2024) — Studies the sources of verbatim memorization and methods to reduce it before privacy issues emerge.
- [Forget to Flourish: Leveraging Machine-Unlearning on Pretrained Language Models for Privacy Leakage](https://arxiv.org/abs/2408.17354) (2024) — Applies unlearning to reduce privacy leakage from pretrained models rather than only fine-tuned chat systems.
- [Learning to Refuse: Towards Mitigating Privacy Risks in LLMs](https://arxiv.org/abs/2407.10058) (2024) — Teaches the model to refuse prompts that would elicit private information, complementing deletion-style defenses. [[code](https://github.com/zhliu0106/learning-to-refuse)]
- [Demystifying Verbatim Memorization in Large Language Models](https://arxiv.org/abs/2407.17817) (2024) — Characterizes when LLMs reproduce exact training snippets and how that shapes deletion difficulty.
- [REVS: Unlearning Sensitive Information in Language Models via Rank Editing in the Vocabulary Space](https://arxiv.org/abs/2406.09325) (2024) — Edits low-rank directions in vocabulary space to suppress sensitive memorized strings. [[code](https://github.com/Tomertech/REVS)]
- [Protecting Privacy Through Approximating Optimal Parameters for Sequence Unlearning in Language Models](https://arxiv.org/abs/2406.14091) (2024) — Approximates the optimal parameter update for deleting a specific private sequence from a language model.
- [Evaluating Copyright Takedown Methods for Language Models](https://arxiv.org/abs/2406.18664) (2024) — Compares competing takedown objectives and metrics for copyrighted text in language models.
- [Avoiding Copyright Infringement via Machine Unlearning](https://arxiv.org/abs/2406.10952) (2024) — Uses unlearning as a direct mechanism for reducing copyright-infringing generations. [[code](https://github.com/guangyaodou/SSU/tree/main)]
- [DEPN: Detecting and Editing Privacy Neurons in Pretrained Language Models](https://arxiv.org/abs/2310.20138) (2023) — Locates privacy-relevant neurons and edits them to suppress leakage at the neuron level. [[code](https://github.com/flamewei123/DEPN)]
- [Forgetting Private Textual Sequences in Language Models via Leave-One-Out Ensemble](https://arxiv.org/abs/2309.16082) (2023) — Uses leave-one-out ensembling to approximate retraining for deletion of sensitive textual sequences.
- [Make Text Unlearnable: Exploiting Effective Patterns to Protect Personal Data](https://arxiv.org/abs/2307.00456) (2023) — Perturbs text so personal data are harder for future language models to memorize in the first place.

- [Machine Unlearning of Personally Identifiable Information in Large Language Models](https://aclanthology.org/2025.nllp-1.6/) (2025) — Introduces the UnlearnPII benchmark and the PERMU_tok method for PII unlearning, including obfuscated-prompt and jailbreak evaluations. [[code](https://github.com/pariidanDKE/Toward-Practical-PII-Unlearning)]
### Safety, harmful content, jailbreaks, and backdoors

- [LLMs Can Unlearn Refusal with Only 1,000 Benign Samples](https://arxiv.org/abs/2601.19231) (2026) — Shows that even small benign datasets can erase refusal behavior, exposing how fragile some safety safeguards are. [[code](https://github.com/guoyang9/refusal-unlearning)]
- [JPU: Bridging Jailbreak Defense and Unlearning via On-Policy Path Rectification](https://arxiv.org/abs/2601.03005) (2026) — Uses on-policy path rectification so jailbreak defense and unlearning operate on the model’s own harmful trajectories.
- [Machine Unlearning Meets Adversarial Robustness via Constrained Interventions on LLMs](https://arxiv.org/abs/2510.03567) (2025) — Combines deletion with adversarially constrained interventions so safety gains persist under attack.
- [Leverage Unlearning to Sanitize LLMs](https://arxiv.org/abs/2510.21322) (2025) — Treats unlearning as a post-training sanitization step for removing unsafe or undesirable generations.
- [AntiDote: Bi-level Adversarial Training for Tamper-Resistant LLMs](https://arxiv.org/abs/2509.08000) (2025) — Uses bi-level adversarial training to build safeguards that resist later tampering or hostile fine-tuning.
- [SafeLLM: Unlearning Harmful Outputs from Large Language Models against Jailbreak Attacks](https://arxiv.org/abs/2508.15182) (2025) — Targets jailbreak-generated harmful outputs directly rather than only teaching generic refusal.
- [Reliable Unlearning Harmful Information in LLMs with Metamorphosis Representation Projection](https://arxiv.org/abs/2508.15449) (2025) — Projects away harmful representations with a metamorphosis step designed to preserve benign capabilities.
- [Deep Ignorance: Filtering Pretraining Data Builds Tamper-Resistant Safeguards into Open-Weight LLMs](https://arxiv.org/abs/2508.06601) (2025) — Pushes deletion upstream into data filtering so safeguards are harder to undo after release. [[code](https://github.com/EleutherAI/deep-ignorance)]
- [DUP: Detection-guided Unlearning for Backdoor Purification in Language Models](https://arxiv.org/abs/2508.01647) (2025) — Uses a detector to first localize backdoor behavior and then target unlearning at that trigger-response pathway.
- [Vulnerability-Aware Alignment: Mitigating Uneven Forgetting in Harmful Fine-Tuning](https://arxiv.org/abs/2506.03850) (2025) — Addresses the fact that harmful capabilities are not forgotten uniformly across vulnerability types.
- [Safety Alignment via Constrained Knowledge Unlearning](https://arxiv.org/abs/2505.18588) (2025) — Uses constrained knowledge deletion so safety alignment improves without unnecessarily stripping general competence.
- [From Dormant to Deleted: Tamper-Resistant Unlearning Through Weight-Space Regularization](https://arxiv.org/abs/2505.22310) (2025) — Regularizes weight space so harmful capabilities are removed rather than merely left dormant and recoverable.
- [CTRAP: Embedding Collapse Trap to Safeguard Large Language Models from Harmful Fine-Tuning](https://arxiv.org/abs/2505.16559) (2025) — Uses an embedding-collapse trap to keep harmful fine-tuning from reviving unsafe behavior.
- [Improving LLM Safety Alignment with Dual-Objective Optimization](https://arxiv.org/abs/2503.03710) (2025) — Jointly optimizes safety and utility so alignment does not come solely from broad capability loss. [[code](https://github.com/wicai24/DOOR-Alignment)]
- [Backdoor Token Unlearning: Exposing and Defending Backdoors in Pretrained Language Models](https://arxiv.org/abs/2501.03272) (2025) — Targets token-triggered backdoors embedded during pretraining and studies how to remove them cleanly.
- [Classifier-free guidance in LLMs Safety](https://arxiv.org/abs/2412.06846) (2024) — Adapts classifier-free guidance ideas to steer generation away from unsafe continuations in safety-focused unlearning.
- [Unlearning Backdoor Attacks for LLMs with Weak-to-Strong Knowledge Distillation](https://arxiv.org/abs/2410.14425) (2024) — Uses weak-to-strong distillation to purge backdoors while recovering the clean model’s intended behavior. [[code](https://github.com/shuaizhao95/Unlearning)]
- [Tamper-Resistant Safeguards for Open-Weight LLMs](https://arxiv.org/abs/2408.00761) (2024) — Designs safety safeguards specifically to survive downstream fine-tuning and editing attacks. [[code](https://github.com/rishub-tamirisa/tamper-resistance/)]
- [Targeted Latent Adversarial Training Improves Robustness to Persistent Harmful Behaviors in LLMs](https://arxiv.org/abs/2407.15549) (2024) — Uses latent-space adversarial training to harden against harmful behaviors that keep resurfacing after alignment. [[code](https://github.com/aengusl/latent-adversarial-training)]
- [Safe Unlearning: A Surprisingly Effective and Generalizable Solution to Defend Against Jailbreak Attacks](https://arxiv.org/abs/2407.02855) (2024) — Uses unlearning as a simple but strong jailbreak defense that transfers beyond the training prompts. [[code](https://github.com/thu-coai/SafeUnlearning)]
- [If You Don't Understand It, Don't Use It: Eliminating Trojans with Filters Between Layers](https://arxiv.org/abs/2407.06411) (2024) — Inserts filters between layers to intercept trojan activations before they produce backdoored outputs. [[code](https://github.com/4gatepylon/IfYouDontUnderstandItDontUseIt)]
- [Eraser: Jailbreaking Defense in Large Language Models via Unlearning Harmful Knowledge](https://arxiv.org/abs/2404.05880) (2024) — Targets jailbreak-relevant harmful knowledge rather than only surface refusals.
- [Guardrail Baselines for Unlearning in LLMs](https://arxiv.org/abs/2403.03329) (2024) — Studies how unlearning interacts with refusal behavior and guardrail enforcement.
- [Towards Safer Large Language Models through Machine Unlearning](https://arxiv.org/abs/2402.10058) (2024) — Explores machine unlearning as a general pathway for making open LLMs safer after training. [[code](https://github.com/franciscoliu/SKU)]
- [Soft Prompt Threats: Attacking Safety Alignment and Unlearning in Open-Source LLMs through the Embedding Space](https://arxiv.org/abs/2402.09063) (2024) — Shows that embedding-space soft prompts can bypass both safety alignment and forgetting-based defenses.
- [Making Harmful Behaviors Unlearnable for Large Language Models](https://arxiv.org/abs/2311.02105) (2023) — Directly targets harmful behaviors as the deletion object rather than treating them as a side effect of factual forgetting.

### Skills, reasoning, bias, hallucination, and behavior shaping

- [Explainable LLM Unlearning Through Reasoning](https://arxiv.org/abs/2603.09980) (2026) — Uses explicit reasoning traces to make the deletion process itself more interpretable.
- [STaR: Sensitive Trajectory Regulation for Unlearning in Large Reasoning Models](https://arxiv.org/abs/2601.09281) (2026) — Regulates sensitive reasoning trajectories so the model forgets target chains of thought without losing general reasoning skill.
- [Beyond Forgetting: Machine Unlearning Elicits Controllable Side Behaviors and Capabilities](https://arxiv.org/abs/2601.21702) (2026) — Studies the side behaviors induced by deletion and how they can be turned into controllable capabilities.
- [DRAGON: Guard LLM Unlearning in Context via Negative Detection and Reasoning](https://arxiv.org/abs/2511.05784) (2025) — Detects risky contexts and reasons about when in-context forgetting should activate.
- [Wisdom is Knowing What not to Say: Hallucination-Free LLMs Unlearning via Attention Shifting](https://arxiv.org/abs/2510.17210) (2025) — Shifts attention away from hallucination-inducing cues to suppress false generations.
- [LLM Unlearning with LLM Beliefs](https://arxiv.org/abs/2510.19422) (2025) — Uses the model’s own inferred beliefs as the signal for what should be revised or forgotten.
- [Mitigating Biases in Language Models via Bias Unlearning](https://arxiv.org/abs/2509.25673) (2025) — Treats social bias as the deletion target and studies how bias removal alters model behavior.
- [Inverse IFEval: Can LLMs Unlearn Stubborn Training Conventions to Follow Real Instructions?](https://arxiv.org/abs/2509.04292) (2025) — Tests whether models can forget entrenched instruction-following conventions that block genuine user intent.
- [Intrinsic Meets Extrinsic Fairness: Assessing the Downstream Impact of Bias Mitigation in Large Language Models](https://arxiv.org/abs/2509.16462) (2025) — Links intrinsic bias reduction inside the model to downstream fairness outcomes on real tasks.
- [Standard vs. Modular Sampling: Best Practices for Reliable LLM Unlearning](https://arxiv.org/abs/2509.05316) (2025) — Shows that decoding and sampling choices can materially change apparent unlearning success.
- [Reasoning Model Unlearning: Forgetting Traces, Not Just Answers, While Preserving Reasoning Skills](https://arxiv.org/abs/2506.12963) (2025) — Separates reasoning traces from final answers so a model can forget target chains without losing general reasoning ability. [[code](https://github.com/OPTML-Group/Unlearn-R2MU)]
- [Aligned but Blind: Alignment Increases Implicit Bias by Reducing Awareness of Race](https://arxiv.org/abs/2506.00253) (2025) — Shows that some alignment procedures reduce explicit mention of race while increasing hidden bias.
- [R-TOFU: Unlearning in Large Reasoning Models](https://arxiv.org/abs/2505.15214) (2025) — Extends TOFU-style unlearning to reasoning models where traces matter as much as final answers.
- [Effective Skill Unlearning through Intervention and Abstention](https://arxiv.org/abs/2503.21730) (2025) — Combines targeted interventions with abstention so risky skills are suppressed when they would be invoked.
- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](https://arxiv.org/pdf/2502.14829) (2025) — Deletes individual reasoning steps to test whether chain-of-thought explanations are truly causally used. [[code](https://github.com/%20technion-cs-nlp/parametric-faithfulness)]
- [UnStar: Unlearning with Self-Taught Anti-Sample Reasoning for LLMs](https://arxiv.org/abs/2410.17050) (2024) — Generates self-taught anti-samples through reasoning and uses them to suppress targeted behavior.
- [Towards Transfer Unlearning: Empirical Evidence of Cross-Domain Bias Mitigation](https://arxiv.org/abs/2407.16951) (2024) — Studies whether bias removal in one domain transfers to other domains without retraining from scratch.
- [Mitigating Social Biases in Language Models through Unlearning](https://arxiv.org/abs/2406.13551) (2024) — Applies deletion-style updates to reduce socially biased generations in general-purpose LMs. [[code](https://github.com/VectorInstitute/Bias_in_LMsBias_mitigation)]
- [FairSISA: Ensemble Post-Processing to Improve Fairness of Unlearning in LLMs](https://arxiv.org/abs/2312.07420) (2023) — Uses ensemble post-processing to repair fairness issues introduced by unlearning.
- [Unlearning Bias in Language Models by Partitioning Gradients](https://aclanthology.org/2023.findings-acl.375/) (2023) — Partitions gradients so bias-related directions can be removed without overwriting unrelated abilities. [[code](https://github.com/CharlesYu2000/PCGU-UnlearningBias)]

## Evaluation, Benchmarks, Auditing, and Attacks

### Benchmarks, datasets, and evaluation suites

- [Evaluating Cross-Lingual Unlearning in Multilingual Language Models](https://arxiv.org/abs/2601.06675) (2026) — Proposes evaluation protocols for checking whether deletion transfers across languages and scripts.
- [Behemoth: Benchmarking Unlearning in LLMs Using Fully Synthetic Data](https://arxiv.org/abs/2601.23153) (2026) — Uses fully synthetic data so ground-truth deleted knowledge is precisely controlled. [[code](https://github.com/IST-DASLab/behemoth.git)]
- [RippleBench: Capturing Ripple Effects Using Existing Knowledge Repositories](https://arxiv.org/abs/2512.04144) (2025) — Measures whether forgetting one fact causes the right ripple effects across linked knowledge repositories.
- [MedForget: Hierarchy-Aware Multimodal Unlearning Testbed for Medical AI](https://arxiv.org/abs/2512.09867) (2025) — Builds a medical multimodal testbed with hierarchy-aware deletion tasks and realistic domain constraints.
- [OFFSIDE: Benchmarking Unlearning Misinformation in Multimodal Large Language Models](https://arxiv.org/abs/2510.22535) (2025) — Evaluates multimodal misinformation deletion rather than only textual factual forgetting.
- [Hubble: a Model Suite to Advance the Study of LLM Memorization](https://arxiv.org/abs/2510.19811) (2025) — Releases a model suite designed to make memorization and post-unlearning leakage easier to study systematically.
- [Unlearning as Ablation: Toward a Falsifiable Benchmark for Generative Scientific Discovery](https://arxiv.org/abs/2508.17681) (2025) — Frames forgetting as a falsifiable ablation test for whether models truly relied on specific scientific knowledge.
- [Towards Evaluation for Real-World LLM Unlearning](https://arxiv.org/abs/2508.01324) (2025) — Argues for deployment-realistic scenarios, metrics, and failure cases beyond toy benchmark setups.
- [iShumei-Chinchunmei at SemEval-2025 Task 4: A balanced forgetting and retention multi-task framework using effective unlearning loss](https://arxiv.org/abs/2507.16263) (2025) — SemEval system paper using a multitask loss to balance forget and retain performance.
- [PULSE: Practical Evaluation Scenarios for Large Multimodal Model Unlearning](https://arxiv.org/abs/2507.01271) (2025) — Introduces practical, scenario-based multimodal evaluations instead of narrow synthetic prompts.
- [Automating Evaluation of Diffusion Model Unlearning with (Vision-) Language Model World Knowledge](https://arxiv.org/abs/2507.07137) (2025) — Automates diffusion-model unlearning evaluation by querying world knowledge through language or vision-language models.
- [OpenUnlearning: Accelerating LLM Unlearning via Unified Benchmarking of Methods and Metrics](https://arxiv.org/abs/2506.12618) (2025) — Provides a unified harness for comparing methods, metrics, and settings at scale.
- [Mr. Snuffleupagus at SemEval-2025 Task 4: Unlearning Factual Knowledge from LLMs Using Adaptive RMU](https://arxiv.org/abs/2506.16548) (2025) — SemEval system paper that adapts RMU-style updates for factual deletion.
- [Lacuna Inc. at SemEval-2025 Task 4: LoRA-Enhanced Influence-Based Unlearning for LLMs](https://arxiv.org/abs/2506.04044) (2025) — SemEval system paper combining LoRA with influence estimates for lightweight deletion.
- [BLUR: A Benchmark for LLM Unlearning Robust to Forget-Retain Overlap](https://arxiv.org/abs/2506.15699) (2025) — Designs a benchmark where forget and retain sets overlap semantically, making superficial deletion much harder to fake.
- [Unlearning Sensitive Information in Multimodal LLMs: Benchmark and Attack-Defense Evaluation](https://arxiv.org/abs/2505.01456) (2025) — Pairs a multimodal sensitive-information benchmark with explicit attack and defense protocols. [[code](https://github.com/Vaidehi99/UnLOK-VQA)]
- [SHA256 at SemEval-2025 Task 4: Selective Amnesia -- Constrained Unlearning for Large Language Models via Knowledge Isolation](https://arxiv.org/abs/2504.12996) (2025) — SemEval system paper using constrained knowledge isolation for selective amnesia.
- [ZJUKLAB at SemEval-2025 Task 4: Unlearning via Model Merging](https://arxiv.org/abs/2503.21088) (2025) — SemEval system paper that performs deletion by merging checkpoints rather than optimizing from scratch.
- [SAEBench: A Comprehensive Benchmark for Sparse Autoencoders in Language Model Interpretability](https://arxiv.org/abs/2503.09532) (2025) — Benchmarks sparse autoencoders that are often used as tools in interpretability-driven unlearning.
- [PEBench: A Fictitious Dataset to Benchmark Machine Unlearning for Multimodal Large Language Models](https://arxiv.org/abs/2503.12545) (2025) — Provides a fictitious multimodal dataset with controlled ground-truth forget targets.
- [Cyber for AI at SemEval-2025 Task 4: Forgotten but Not Lost: The Balancing Act of Selective Unlearning in Large Language Models](https://arxiv.org/abs/2503.04795) (2025) — SemEval system paper focused on balancing selective forgetting with retention under shared-task scoring.
- [Atyaephyra at SemEval-2025 Task 4: Low-Rank NPO](https://arxiv.org/abs/2503.13690) (2025) — SemEval system paper implementing a low-rank version of negative preference optimization.
- [AILS-NTUA at SemEval-2025 Task 4: Parameter-Efficient Unlearning for Large Language Models using Data Chunking](https://arxiv.org/abs/2503.02443) (2025) — SemEval system paper that chunks data and uses PEFT to lower deletion cost. [[code](https://github.com/iraklis07/llm-unlearning)]
- [LUME: LLM Unlearning with Multitask Evaluations](https://arxiv.org/abs/2502.15097) (2025) — Evaluates unlearning across multiple task families instead of relying on one scalar score.
- [Beyond Single-Value Metrics: Evaluating and Enhancing LLM Unlearning with Cognitive Diagnosis](https://arxiv.org/abs/2502.13996) (2025) — Uses cognitive-diagnosis ideas to identify exactly which skills or concepts remain after deletion. [[code](https://github.com/lyicheng619/UNCD)]
- [Towards Robust Evaluation of Unlearning in LLMs via Data Transformations](https://arxiv.org/abs/2411.15477) (2024) — Stress-tests deletion with transformed inputs such as paraphrases and rewrites.
- [Benchmarking Vision Language Model Unlearning via Fictitious Facial Identity Dataset](https://arxiv.org/abs/2411.03554) (2024) — Uses fictitious facial identities to benchmark privacy-style forgetting in VLMs. [[code](https://github.com/SaFoLab-WISC/FIUBench)]
- [Protecting Privacy in Multimodal Large Language Models with MLLMU-Bench](https://arxiv.org/abs/2410.22108) (2024) — Introduces a privacy-focused multimodal benchmark for MLLM unlearning. [[code](https://github.com/franciscoliu/MLLMU-Bench)]
- [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://openreview.net/forum?id=TArmA033BU) (2024) — Defines a six-way evaluation protocol covering forgetting, retention, robustness, and side effects. [[code](https://muse-bench.github.io/)]
- [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://arxiv.org/abs/2406.10890) (2024) — Moves beyond fictitious facts to benchmark deletion of real-world knowledge. [[code](https://github.com/jinzhuoran/RWKU)]
- [PISTOL: Dataset Compilation Pipeline for Structural Unlearning of LLMs](https://arxiv.org/abs/2406.16810) (2024) — Builds a dataset pipeline tailored to structural knowledge deletion rather than isolated facts. [[code](https://github.com/bill-shen-BS/PISTOL)]
- [The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning](https://arxiv.org/abs/2403.03218) (2024) — Introduces a benchmark for measuring whether unlearning reduces hazardous or malicious-use capabilities. [[code](https://github.com/centerforaisafety/wmdp)]
- [TOFU: A Task of Fictitious Unlearning for LLMs](https://arxiv.org/abs/2401.06121) (2024) — Introduces a controllable fictitious-facts benchmark that became a standard testbed for targeted LLM unlearning. [[code](https://github.com/locuslab/tofu)]

- [SemEval-2025 Task 4: Unlearning sensitive content from Large Language Models](https://aclanthology.org/2025.semeval-1.329/) (2025) — Shared-task overview paper covering three LLM unlearning subtasks and summarizing lessons from more than 100 submissions.
- [NEKO at SemEval-2025 Task 4: A Gradient Ascent Based Machine Unlearning Strategy](https://aclanthology.org/2025.semeval-1.64/) (2025) — Gradient-ascent-based SemEval system for targeted LLM unlearning.
- [DUTir at SemEval-2025 Task 4: Optimized Fine-Tuning of Linear Layers for Balanced Knowledge Forgetting and Retention](https://aclanthology.org/2025.semeval-1.72/) (2025) — Optimizes linear-layer fine-tuning to balance forgetting and retention in the shared task.
- [NeuroReset: LLM Unlearning via Dual Phase Mixed Methodology](https://aclanthology.org/2025.semeval-1.138/) (2025) — Dual-phase SemEval system for LLM unlearning.
- [GUIR at SemEval-2025 Task 4: Adaptive Weight Tuning with Gradual Negative Matching for LLM Unlearning](https://aclanthology.org/2025.semeval-1.152/) (2025) — SemEval system based on adaptive weight tuning and gradual negative matching.
- [GIL-IIMAS UNAM at SemEval-2025 Task 4: LA-Min(E): LLM Unlearning Approaches Under Function Minimizing Evaluation Constraints](https://aclanthology.org/2025.semeval-1.205/) (2025) — SemEval system paper centered on LA-Min(E) under function-minimizing evaluation constraints.
- [MALTO at SemEval-2025 Task 4: Dual Teachers for Unlearning Sensitive Content in LLMs](https://aclanthology.org/2025.semeval-1.229/) (2025) — Dual-teacher SemEval system for unlearning sensitive content in LLMs.
- [Howard University-AI4PC at SemEval-2025 Task 4: Unlearning Sensitive Content From Large Language Models Using Finetuning and Distillation for Selective Knowledge Removal](https://aclanthology.org/2025.semeval-1.233/) (2025) — Fine-tuning-and-distillation SemEval system for selective knowledge removal.
- [YNU at SemEval-2025 Task 4: Synthetic Token Alternative Training for LLM Unlearning](https://aclanthology.org/2025.semeval-1.264/) (2025) — Synthetic Token Alternative Training (STAT) SemEval system for LLM unlearning.
- [JU-CSE-NLP'25 at SemEval-2025 Task 4: Learning to Unlearn LLMs](https://aclanthology.org/2025.semeval-1.267/) (2025) — SemEval system paper on targeted LLM unlearning.
- [NLPART at SemEval-2025 Task 4: Forgetting is harder than Learning](https://aclanthology.org/2025.semeval-1.304/) (2025) — SemEval system paper on targeted LLM forgetting.
### Auditing, metrics, and verification

- [Auditing Language Model Unlearning via Information Decomposition](https://arxiv.org/abs/2601.15111) (2026) — Decomposes information flow between data, outputs, and model state to audit what knowledge remains.
- [(Token-Level) InfoRMIA: Stronger Membership Inference and Memorization Assessment for LLMs](https://arxiv.org/abs/2510.05582) (2025) — Strengthens membership inference by operating at token level to assess residual memorization after deletion.
- [What Should LLMs Forget? Quantifying Personal Data in LLMs for Right-to-Be-Forgotten Requests](https://arxiv.org/abs/2507.11128) (2025) — Quantifies which categories of personal data are realistic right-to-be-forgotten targets for LLMs.
- [Watch the Weights: Unsupervised monitoring and control of fine-tuned LLMs](https://arxiv.org/abs/2508.00161) (2025) — Monitors weight-space changes to detect hidden unlearning or other post-training interventions without labels.
- [Unlearning Isn't Invisible: Detecting Unlearning Traces in LLMs from Model Outputs](https://arxiv.org/abs/2506.14003) (2025) — Shows that model outputs can contain detectable signatures of prior unlearning interventions.
- [Towards Lifecycle Unlearning Commitment Management: Measuring Sample-level Unlearning Completeness](https://arxiv.org/abs/2506.06112) (2025) — Proposes sample-level completeness metrics for tracking whether a deletion request was fully honored over time.
- [WaterDrum: Watermarking for Data-centric Unlearning Metric](https://arxiv.org/abs/2505.05064) (2025) — Uses watermarking to create a data-centric metric for how well target examples were removed. [[code](https://github.com/lululu008/WaterDrum)]
- [Does Machine Unlearning Truly Remove Model Knowledge? A Framework for Auditing Unlearning in LLMs](https://arxiv.org/abs/2505.23270) (2025) — Builds an auditing framework around whether apparent forgetting corresponds to actual knowledge removal.
- [Tokens for Learning, Tokens for Unlearning: Mitigating Membership Inference Attacks in Large Language Models via Dual-Purpose Training](https://arxiv.org/abs/2502.19726) (2025) — Uses dual-purpose tokens that support training quality while also reducing membership-inference leakage.
- [Soft Token Attacks Cannot Reliably Audit Unlearning in Large Language Models](https://arxiv.org/abs/2502.15836) (2025) — Shows that soft-token attack probes can misdiagnose whether unlearning succeeded.
- [Holistic Audit Dataset Generation for LLM Unlearning via Knowledge Graph Traversal and Redundancy Removal](https://arxiv.org/abs/2502.18810) (2025) — Generates richer audit sets by traversing knowledge graphs and removing redundant probes.
- [Intrinsic Evaluation of Unlearning Using Parametric Knowledge Traces](https://arxiv.org/abs/2406.11614) (2024) — Uses parametric knowledge traces to evaluate deletion intrinsically without depending only on final-text outputs. [[code](https://github.com/yihuaihong/ConceptVectors)]
- [Localizing Paragraph Memorization in Language Models](https://arxiv.org/abs/2403.19851) (2024) — Pinpoints where memorized paragraphs live in the model, aiding targeted auditing and deletion.
- [Unlearning Reveals the Influential Training Data of Language Models](https://arxiv.org/abs/2401.15241) (2024) — Uses deletion behavior to identify which training examples most strongly shaped a model’s outputs.

- [A Fully Probabilistic Perspective on Large Language Model Unlearning: Evaluation and Optimization](https://aclanthology.org/2025.emnlp-main.452/) (2025) — Introduces fully probabilistic evaluation and optimization to avoid overly optimistic deterministic assessments of LLM unlearning.
- [White-Box Auditing of Large Language Model Unlearning](https://openreview.net/forum?id=hPruSo1bEE) (2026) — Proposes a white-box auditing framework and shows that simple inverse-greedy decoding can recover supposedly forgotten fake PII.
### Robustness, recovery, and failure analyses

- [The Unlearning Mirage: A Dynamic Framework for Evaluating LLM Unlearning](https://arxiv.org/abs/2603.11266) (2026) — Uses dynamic interaction-based evaluation to show that one-shot forget scores can overstate true deletion.
- [A Comprehensive Evaluation of LLM Unlearning Robustness under Multi-Turn Interaction](https://arxiv.org/abs/2603.00823) (2026) — Stress-tests deletion under multi-turn dialogue where hidden knowledge can resurface across turns.
- [REBEL: Hidden Knowledge Recovery via Evolutionary-Based Evaluation Loop](https://arxiv.org/abs/2602.06248) (2026) — Uses evolutionary search to iteratively discover prompts that recover supposedly forgotten knowledge. [[code](https://github.com/patryk-rybak/REBEL/)]
- [The Erasure Illusion: Stress-Testing the Generalization of LLM Forgetting Evaluation](https://arxiv.org/abs/2512.19025) (2025) — Shows that success on narrow test prompts often fails to generalize to broader probing distributions.
- [Leak@$k$: Unlearning Does Not Make LLMs Forget Under Probabilistic Decoding](https://arxiv.org/abs/2511.04934) (2025) — Demonstrates that sampling-based decoding can reveal residual target knowledge hidden under greedy decoding.
- [Uncovering the Potential Risks in Unlearning: Danger of English-only Unlearning in Multilingual LLMs](https://arxiv.org/abs/2510.23949) (2025) — Shows that deleting only English evidence can leave target knowledge accessible in other languages.
- [The Limits of Obliviate: Evaluating Unlearning in LLMs via Stimulus-Knowledge Entanglement-Behavior Framework](https://arxiv.org/abs/2510.25732) (2025) — Uses a stimulus–knowledge–behavior framework to analyze where a strong practical method still fails.
- [Reference-Specific Unlearning Metrics Can Hide the Truth: A Reality Check](https://arxiv.org/abs/2510.12981) (2025) — Argues that metrics keyed to a narrow reference answer can miss many genuine leakage paths.
- [Probing Knowledge Holes in Unlearned LLMs](https://arxiv.org/abs/2511.00030) (2025) — Probes the irregular “knowledge holes” that deletion leaves behind in surrounding concepts and prompts.
- [LLM Unlearning Under the Microscope: A Full-Stack View on Methods and Metrics](https://arxiv.org/abs/2510.07626) (2025) — Re-examines the whole stack of methods and metrics to show where current evaluations are misleading.
- [Step-by-Step Reasoning Attack: Revealing 'Erased' Knowledge in Large Language Models](https://arxiv.org/abs/2506.17279) (2025) — Recovers supposedly erased facts by eliciting intermediate reasoning steps rather than direct answers.
- [Keeping an Eye on LLM Unlearning: The Hidden Risk and Remedy](https://arxiv.org/abs/2506.00359) (2025) — Identifies hidden post-unlearning risks and proposes concrete mitigation strategies.
- [Existing Large Language Model Unlearning Evaluations Are Inconclusive](https://arxiv.org/abs/2506.00688) (2025) — Argues that current protocols cannot yet determine whether true deletion has occurred.
- [Does Multimodal Large Language Model Truly Unlearn? Stealthy MLLM Unlearning Attack](https://arxiv.org/abs/2506.17265) (2025) — Introduces a stealthy attack that recovers target content from multimodal LLMs after deletion.
- [Do LLMs Really Forget? Evaluating Unlearning with Knowledge Correlation and Confidence Awareness](https://arxiv.org/abs/2506.05735) (2025) — Uses knowledge correlation and confidence signals to detect lingering target information.
- [Unlearning vs. Obfuscation: Are We Truly Removing Knowledge?](https://arxiv.org/abs/2505.02884) (2025) — Argues that some unlearning methods hide knowledge rather than truly deleting it. [[code](https://github.com/potsawee/unlearning-hallu/tree/mcq)]
- [Unlearning Isn't Deletion: Investigating Reversibility of Machine Unlearning in LLMs](https://arxiv.org/abs/2505.16831) (2025) — Studies how quickly forgotten content can be restored by later fine-tuning or relearning.
- [Layered Unlearning for Adversarial Relearning](https://arxiv.org/abs/2505.09500) (2025) — Uses layered defenses to make adversarial relearning of forgotten knowledge harder. [[code](https://github.com/12tqian/layered-unlearning)]
- [Harry Potter is Still Here! Probing Knowledge Leakage in Targeted Unlearned Large Language Models via Automated Adversarial Prompting](https://arxiv.org/abs/2505.17160) (2025) — Uses automated adversarial prompting to recover entity knowledge thought to be deleted.
- [Breaking the Gold Standard: Extracting Forgotten Data under Exact Unlearning in Large Language Models](https://arxiv.org/abs/2505.24379) (2025) — Shows that even “exact unlearning” claims can fail under stronger extraction attacks.
- [Safety Mirage: How Spurious Correlations Undermine VLM Safety Fine-tuning](https://arxiv.org/abs/2503.11832) (2025) — Shows that VLM safety gains can come from spurious correlations rather than real deletion of unsafe knowledge.
- [Towards LLM Unlearning Resilient to Relearning Attacks: A Sharpness-Aware Minimization Perspective and Beyond](https://arxiv.org/abs/2502.05374) (2025) — Uses sharpness-aware training to make deleted behavior harder to recover with relearning. [[code](https://github.com/OPTML-Group/Unlearn-Smooth)]
- [Model Tampering Attacks Enable More Rigorous Evaluations of LLM Capabilities](https://arxiv.org/abs/2502.05209) (2025) — Uses model tampering as a stronger adversarial lens for evaluating whether capabilities were truly removed.
- [Mitigating Sensitive Information Leakage in LLMs4Code through Machine Unlearning](https://arxiv.org/abs/2502.05739) (2025) — Tests machine unlearning as a defense against secret leakage in code-generation models.
- [RESTOR: Knowledge Recovery through Machine Unlearning](https://arxiv.org/abs/2411.00204) (2024) — Studies how much deleted knowledge can be reconstructed from the model after unlearning. [[code](https://github.com/k1rezaei/restor)]
- [Extracting Unlearned Information from LLMs with Activation Steering](https://arxiv.org/abs/2411.02631) (2024) — Shows that activation steering can resurrect information that standard evaluations deem forgotten.
- [Does Unlearning Truly Unlearn? A Black Box Evaluation of LLM Unlearning Methods](https://arxiv.org/abs/2411.12103) (2024) — Evaluates deletion purely from black-box behavior to test whether hidden leakage survives opaque systems. [[code](https://github.com/JaiDoshi/Knowledge-Erasure)]
- [Evaluating Deep Unlearning in Large Language Models](https://arxiv.org/abs/2410.15153) (2024) — Examines whether deeper deletion strategies actually remove target knowledge more thoroughly. [[code](https://github.com/wrh14/deep_unlearning)]
- [Does your LLM truly unlearn? An embarrassingly simple approach to recover unlearned knowledge](https://arxiv.org/abs/2410.16454) (2024) — Shows that a simple recovery prompt can often revive supposedly deleted content. [[code](https://github.com/zzwjames/FailureLLMUnlearning)]
- [LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet](https://arxiv.org/abs/2408.15221) (2024) — Shows that human multi-turn conversations can still bypass defenses, even after safety-focused deletion.
- [Unlearning or Obfuscating? Jogging the Memory of Unlearned LLMs via Benign Relearning](https://arxiv.org/abs/2406.13356) (2024) — Uses benign relearning to test whether forgotten content was deleted or merely hidden.
- [Textual Unlearning Gives a False Sense of Unlearning](https://arxiv.org/abs/2406.13348) (2024) — Argues that text-only benchmarks can greatly overestimate success on broader deletion goals.
- [Machine Unlearning Fails to Remove Data Poisoning Attacks](https://arxiv.org/abs/2406.17216) (2024) — Shows that poisoned behavior can survive standard deletion methods even when clean-data forgetting looks strong.
- [Inexact Unlearning Needs More Careful Evaluations to Avoid a False Sense of Privacy](https://arxiv.org/abs/2403.01218) (2024) — Warns that weak evaluations can make approximate deletion look safer for privacy than it really is.
- [Can Sensitive Information Be Deleted From LLMs? Objectives for Defending Against Extraction Attacks](https://arxiv.org/abs/2309.17410) (2023) — Compares deletion objectives against direct extraction attacks on memorized sensitive text. [[code](https://github.com/Vaidehi99/InfoDeletionAttacks)]

- [LUSB: Formalizing and Benchmarking Unlearning Attacks and Defenses against Large Language Models](https://openreview.net/forum?id=lk3j87oquF) (2026) — Introduces a benchmark for unlearning attacks and defenses across 13 LLM architectures, 9 unlearning methods, and 12 datasets.
## Theoretical and Analytical Work

### Optimization, generalization, and provable views

- [Anatomy of Unlearning: The Dual Impact of Fact Salience and Model Fine-Tuning](https://arxiv.org/abs/2602.19612) (2026) — Analyzes how fact salience and prior fine-tuning jointly determine how hard a target is to forget.
- [Unlearning Imperative: Securing Trustworthy and Responsible LLMs through Engineered Forgetting](https://arxiv.org/abs/2511.09855) (2025) — Makes a normative case that engineered forgetting is a core requirement for trustworthy LLM deployment.
- [The Realignment Problem: When Right becomes Wrong in LLMs](https://arxiv.org/abs/2511.02623) (2025) — Studies how seemingly corrective updates can induce new forms of misalignment elsewhere in the model.
- [From Narrow Unlearning to Emergent Misalignment: Causes, Consequences, and Containment in LLMs](https://arxiv.org/abs/2511.14017) (2025) — Analyzes how localized deletion can unexpectedly create broader emergent misalignment.
- [On the Impossibility of Retrain Equivalence in Machine Unlearning](https://arxiv.org/abs/2510.16629) (2025) — Argues that exact equivalence to retraining from scratch is impossible in general settings.
- [KnowledgeSmith: Uncovering Knowledge Updating in LLMs with Model Editing and Unlearning](https://arxiv.org/abs/2510.02392) (2025) — Uses editing and unlearning together to reveal how knowledge is inserted, moved, and removed.
- [Understanding the Dilemma of Unlearning for Large Language Models](https://arxiv.org/abs/2509.24675) (2025) — Analyzes why LLM deletion is caught between irreversibility, utility preservation, and scalability.
- [Analyzing and Mitigating Object Hallucination: A Training Bias Perspective](https://arxiv.org/abs/2508.04567) (2025) — Explains hallucination through training bias and connects that view to targeted behavior removal.
- [The Landscape of Memorization in LLMs: Mechanisms, Measurement, and Mitigation](https://arxiv.org/abs/2507.05578) (2025) — Maps the mechanisms of memorization that determine what deletion methods can realistically remove.
- [Model Collapse Is Not a Bug but a Feature in Machine Unlearning for LLMs](https://arxiv.org/abs/2507.04219) (2025) — Argues that controlled collapse on target behaviors can be a useful deletion signal rather than only a failure mode.
- [SoK: Semantic Privacy in Large Language Models](https://arxiv.org/abs/2506.23603) (2025) — Systematizes semantic privacy risks that motivate unlearning beyond exact memorized strings.
- [SoK: Machine Unlearning for Large Language Models](https://arxiv.org/abs/2506.09227) (2025) — Organizes assumptions, guarantees, evaluations, and open problems for LLM unlearning.
- [Not Every Token Needs Forgetting: Selective Unlearning to Limit Change in Utility in Large Language Model Unlearning](https://arxiv.org/abs/2506.00876) (2025) — Argues for token-level selectivity so deletion need not perturb every token in a target sequence.
- [Not All Tokens Are Meant to Be Forgotten](https://arxiv.org/abs/2506.03142) (2025) — Studies token importance and shows some target tokens can be retained without compromising the deletion goal.
- [Invariance Makes LLM Unlearning Resilient Even to Unanticipated Downstream Fine-Tuning](https://arxiv.org/abs/2506.01339) (2025) — Uses invariance arguments to explain when forgotten behavior stays suppressed after later fine-tuning.
- [Losing is for Cherishing: Data Valuation Based on Machine Unlearning and Shapley Value](https://arxiv.org/abs/2505.16147) (2025) — Uses unlearning and Shapley-style data valuation to estimate which examples matter most.
- [When is Task Vector Provably Effective for Model Editing? A Generalization Analysis of Nonlinear Transformers](https://arxiv.org/abs/2504.10957) (2025) — Provides a generalization analysis for when task-vector-style editing and deletion should work.
- [Not All Data Are Unlearned Equally](https://arxiv.org/abs/2504.05058) (2025) — Shows that deletion difficulty varies sharply across examples rather than being uniform. [[code](https://github.com/McGill-NLP/unequal-unlearning)]
- [LLM Unlearning Reveals a Stronger-Than-Expected Coreset Effect in Current Benchmarks](https://arxiv.org/abs/2504.10185) (2025) — Shows that common benchmarks behave as if a small coreset dominates deletion performance. [[code](https://github.com/OPTML-Group/MU-Coreset)]
- [A Neuro-inspired Interpretation of Unlearning in Large Language Models through Sample-level Unlearning Difficulty](https://arxiv.org/abs/2504.06658) (2025) — Interprets deletion through sample-level difficulty using a neuro-inspired view of memory weakening.
- [Rethinking LLM Unlearning Objectives: A Gradient Perspective and Go Beyond](https://arxiv.org/abs/2502.19301) (2025) — Analyzes popular deletion losses through their gradient geometry and where that geometry fails.
- [Provable unlearning in topic modeling and downstream tasks](https://arxiv.org/abs/2411.12600) (2024) — Gives formal unlearning guarantees in topic models and traces how they propagate to downstream tasks.
- [Do Unlearning Methods Remove Information from Language Model Weights?](https://arxiv.org/abs/2410.08827) (2024) — Tests whether successful deletion scores correspond to actual information removal from weights. [[code](https://github.com/aghyad-deeb/unlearning_evaluation)]
- [Dissecting Fine-Tuning Unlearning in Large Language Models](https://arxiv.org/abs/2410.06606) (2024) — Dissects what fine-tuning-based deletion actually changes internally and where it falls short. [[code](https://github.com/yihuaihong/Dissecting-FT-Unlearning)]
- [A Probabilistic Perspective on Unlearning and Alignment for Large Language Models](https://arxiv.org/abs/2410.03523) (2024) — Builds a probabilistic lens on how deletion and alignment objectives interact.
- [A Closer Look at Machine Unlearning for Large Language Models](https://arxiv.org/abs/2410.08109) (2024) — Re-evaluates common baselines and assumptions to separate real progress from benchmark artifacts. [[code](https://github.com/sail-sg/closer-look-LLM-unlearning)]
- [Unforgettable Generalization in Language Models](https://arxiv.org/abs/2409.02228) (2024) — Studies why some generalizable behaviors are intrinsically hard to erase once learned.
- [An Adversarial Perspective on Machine Unlearning for AI Safety](https://arxiv.org/abs/2409.18025) (2024) — Frames safety-oriented deletion as an adversarial game between the unlearner and recovery attacker. [[code](https://github.com/ethz-spylab/unlearning-vs-safety)]
- [On the Limitations and Prospects of Machine Unlearning for Generative AI](https://arxiv.org/abs/2408.00376) (2024) — Gives a realistic appraisal of what generative-model deletion can and cannot promise.
- [UnUnlearning: Unlearning is not sufficient for content regulation in advanced generative AI](https://arxiv.org/abs/2407.00106) (2024) — Argues that content regulation needs stronger tools than deletion alone.
- [Revisiting Who's Harry Potter: Towards Targeted Unlearning from a Causal Intervention Perspective](https://aclanthology.org/2024.emnlp-main.495/) (2024) — Reinterprets targeted entity deletion through causal interventions instead of purely empirical objective design. [[code](https://github.com/UCSB-NLP-Chang/causal_unlearn.git)]
- [Unlearnable Algorithms for In-context Learning](https://arxiv.org/abs/2402.00751) (2024) — Studies whether algorithmic behaviors learned in context can be made resistant to later in-context recovery.
- [Deciphering the Impact of Pretraining Data on Large Language Models through Machine Unlearning](https://arxiv.org/abs/2402.11537) (2024) — Uses deletion as a probe for which pretraining examples most influence later behavior.
- [What can we learn from Data Leakage and Unlearning for Law?](https://arxiv.org/abs/2307.10476) (2023) — Connects leakage and deletion results to legal notions of compliance and remedy.
- [Machine Unlearning: its nature, scope, and importance for a "delete culture"](https://arxiv.org/abs/2305.15242) (2023) — Provides an early conceptual framing for why engineered deletion matters socially and technically.
- [Deletion Inference, Reconstruction, and Compliance in Machine (Un)Learning](https://arxiv.org/abs/2202.03460) (2022) — Formalizes how deletion claims can be inferred, reconstructed, and checked for compliance.

- [The Fundamental Limits of LLM Unlearning: Complexity-Theoretic Barriers and Provably Optimal Protocols](https://openreview.net/forum?id=ot19dneIID) (2025) — Provides a complexity-theoretic account of LLM unlearning, proving hardness results and an optimal recursive sketch-and-freeze protocol.
### Mechanistic, causal, and representation analyses

- [Toward Understanding Unlearning Difficulty: A Mechanistic Perspective and Circuit-Guided Difficulty Metric](https://arxiv.org/abs/2601.09624) (2026) — Uses mechanistic circuit analysis to explain why some deletion targets are harder than others.
- [Beyond Data Filtering: Knowledge Localization for Capability Removal in LLMs](https://arxiv.org/abs/2512.05648) (2025) — Studies whether dangerous capabilities can be removed by localizing and editing the supporting knowledge pathways.
- [Rotation Control Unlearning: Quantifying and Controlling Continuous Unlearning for LLM with The Cognitive Rotation Space](https://arxiv.org/abs/2509.25743) (2025) — Defines a rotation-space geometry for continuously controlling the strength of deletion.
- [Towards Mitigating Excessive Forgetting in LLM Unlearning via Entanglement-Aware Unlearning with Proxy Constraint](https://arxiv.org/abs/2508.20443) (2025) — Uses entanglement-aware proxy constraints to avoid overshooting into excessive forgetting.
- [Reviving Your MNEME: Predicting The Side Effects of LLM Unlearning and Fine-Tuning via Sparse Model Diffing](https://arxiv.org/abs/2507.21084) (2025) — Uses sparse model diffing to predict side effects before they appear in downstream behavior.
- [Learning-Time Encoding Shapes Unlearning in LLMs](https://arxiv.org/abs/2506.15076) (2025) — Shows that how a fact was encoded during learning strongly affects how easily it can later be removed.
- [Does Localization Inform Unlearning? A Rigorous Examination of Local Parameter Attribution for Knowledge Unlearning in Language Models](https://arxiv.org/abs/2505.16252) (2025) — Rigorously tests whether local parameter attribution really helps targeted factual deletion.
- [Rectifying Belief Space via Unlearning to Harness LLMs' Reasoning](https://arxiv.org/abs/2502.20620) (2025) — Uses unlearning to reshape the model’s belief space in ways that can improve reasoning behavior.
- [Mechanistic Unlearning: Robust Knowledge Unlearning and Editing via Mechanistic Localization](https://arxiv.org/abs/2410.12949) (2024) — Localizes circuits supporting a target fact and then edits them for more surgical and robust forgetting.
- [What Makes and Breaks Safety Fine-tuning? A Mechanistic Study](https://arxiv.org/abs/2407.10264) (2024) — Uses mechanistic analysis to pinpoint which internal pathways make safety fine-tuning succeed or fail.

## Applications and Extensions

### Multimodal and vision-language unlearning

- [Relationship-Aware Safety Unlearning for Multimodal LLMs](https://arxiv.org/abs/2603.14185) (2026) — Models cross-modal relationships explicitly so safety unlearning does not break benign visual-language associations.
- [Visual-Guided Key-Token Regularization for Multimodal Large Language Model Unlearning](https://arxiv.org/abs/2601.22020) (2026) — Uses visual cues to identify which language tokens should be regularized during multimodal deletion.
- [Knowledge Vector Weakening: Efficient Training-free Unlearning for Large Vision-Language Models](https://arxiv.org/abs/2601.21794) (2026) — Weakens knowledge vectors directly, enabling training-free deletion in large vision-language models.
- [Beyond Superficial Unlearning: Sharpness-Aware Robust Erasure of Hallucinations in Multimodal LLMs](https://arxiv.org/abs/2601.16527) (2026) — Uses sharpness-aware optimization to robustly erase hallucination-inducing knowledge in multimodal models.
- [Towards Reasoning-Preserving Unlearning in Multimodal Large Language Models](https://arxiv.org/abs/2512.17911) (2025) — Studies how to delete target content while preserving multimodal reasoning ability.
- [MLLM Machine Unlearning via Visual Knowledge Distillation](https://arxiv.org/abs/2512.11325) (2025) — Uses a visually informed teacher to guide what an MLLM should retain versus forget.
- [Towards Benign Memory Forgetting for Selective Multimodal Large Language Model Unlearning](https://arxiv.org/abs/2511.20196) (2025) — Targets selective forgetting of benign multimodal memories instead of broad safety suppression.
- [SineProject: Machine Unlearning for Stable Vision Language Alignment](https://arxiv.org/abs/2511.18444) (2025) — Focuses on preserving stable vision-language alignment while forgetting target data.
- [Cross-Modal Unlearning via Influential Neuron Path Editing in Multimodal Large Language Models](https://arxiv.org/abs/2511.06793) (2025) — Edits influential neuron paths that carry information between modalities.
- [AUVIC: Adversarial Unlearning of Visual Concepts for Multi-modal Large Language Models](https://arxiv.org/abs/2511.11299) (2025) — Uses adversarial training to remove visual concepts from MLLMs under stronger attacks.
- [MLLMEraser: Achieving Test-Time Unlearning in Multimodal Large Language Models through Activation Steering](https://arxiv.org/abs/2510.04217) (2025) — Performs multimodal deletion at test time by steering activations away from target concepts.
- [Cross-Modal Attention Guided Unlearning in Vision-Language Models](https://arxiv.org/abs/2510.07567) (2025) — Uses cross-modal attention maps to find and suppress the associations that support target knowledge.
- [Approximate Domain Unlearning for Vision-Language Models](https://arxiv.org/abs/2510.08132) (2025) — Studies how to approximately forget an entire source domain in a vision-language model.
- [Unlearning the Noisy Correspondence Makes CLIP More Robust](https://arxiv.org/abs/2507.03434) (2025) — Shows that removing noisy image-text pairings can improve CLIP robustness as well as deletion fidelity.
- [Rethinking Post-Unlearning Behavior of Large Vision-Language Models](https://arxiv.org/abs/2506.02541) (2025) — Analyzes the side effects and new failure modes that appear after VLM deletion.
- [Quantifying Cross-Modality Memorization in Vision-Language Models](https://arxiv.org/abs/2506.05198) (2025) — Measures how memorization in one modality can leak through the other after deletion.
- [T2VUnlearning: A Concept Erasing Method for Text-to-Video Diffusion Models](https://arxiv.org/abs/2505.17550) (2025) — Extends concept erasure to text-to-video diffusion rather than only text or image models.
- [SAUCE: Selective Concept Unlearning in Vision-Language Models with Sparse Autoencoders](https://arxiv.org/abs/2503.14530) (2025) — Uses SAE features to selectively remove visual-language concepts without broad model drift.
- [Machine Unlearning in Hyperbolic vs. Euclidean Multimodal Contrastive Learning: Adapting Alignment Calibration to MERU](https://arxiv.org/abs/2503.15166) (2025) — Compares how geometric choice affects deletion in multimodal contrastive models.
- [Hyperbolic Safety-Aware Vision-Language Models](https://arxiv.org/abs/2503.12127) (2025) — Uses hyperbolic geometry to study safety-aware alignment and deletion in VLMs.
- [SAFEERASER: Enhancing Safety in Multimodal Large Language Models through Multimodal Machine Unlearning](https://arxiv.org/abs/2502.12520) (2025) — Applies multimodal deletion specifically to unsafe visual-language behaviors.
- [Modality-Aware Neuron Pruning for Unlearning in Multimodal Large Language Models](https://arxiv.org/abs/2502.15910) (2025) — Prunes neurons associated with specific modalities to localize deletion. [[code](https://github.com/franciscoliu/MANU)]
- [MMUNLEARNER: Reformulating Multimodal Machine Unlearning in the Era of Multimodal Large Language Models](https://arxiv.org/abs/2502.11051) (2025) — Recasts machine unlearning for modern MLLMs with explicit cross-modal constraints.
- [CLEAR: Character Unlearning in Textual and Visual Modalities](https://arxiv.org/abs/2410.18057) (2024) — Studies deletion of the same character identity across both language and vision channels.
- [Can Textual Unlearning Solve Cross-Modality Safety Alignment?](https://aclanthology.org/2024.findings-emnlp.574/) (2024) — Tests whether text-side deletion transfers to visual safety in multimodal models.
- [Single Image Unlearning: Efficient Machine Unlearning in Multimodal Large Language Models](https://arxiv.org/abs/2405.12523) (2024) — Studies how to forget a single visual example without retraining a whole MLLM.
- [EFUF: Efficient Fine-grained Unlearning Framework for Mitigating Hallucinations in Multimodal Large Language Models](https://aclanthology.org/2024.emnlp-main.67/) (2024) — Provides a fine-grained multimodal unlearning framework aimed at hallucination mitigation. [[code](https://github.com/starreeze/efuf)]

### Federated, modular, and systems settings

- [Quantization-Robust LLM Unlearning via Low-Rank Adaptation](https://arxiv.org/abs/2602.13151) (2026) — Uses LoRA updates that remain effective after quantization and low-bit deployment.
- [QUAIL: Quantization Aware Unlearning for Mitigating Misinformation in LLMs](https://arxiv.org/abs/2601.15538) (2026) — Designs deletion objectives that explicitly account for quantization noise in misinformation mitigation.
- [GRIP: Algorithm-Agnostic Machine Unlearning for Mixture-of-Experts via Geometric Router Constraints](https://arxiv.org/abs/2601.16905) (2026) — Constrains MoE routers geometrically so forgetting can be localized to expert-routing decisions.
- [Hierarchical Federated Unlearning for Large Language Models](https://arxiv.org/abs/2510.17895) (2025) — Builds a hierarchical protocol for honoring deletion requests in federated LLM training.
- [Unlearning at Scale: Implementing the Right to be Forgotten in Large Language Models](https://arxiv.org/abs/2508.12220) (2025) — Focuses on the engineering and systems challenges of large-scale right-to-be-forgotten workflows.
- [Oblivionis: A Lightweight Learning and Unlearning Framework for Federated Large Language Models](https://arxiv.org/abs/2508.08875) (2025) — Provides a lightweight federated framework that supports both distributed learning and later deletion.
- [Large Language Model Federated Learning with Blockchain and Unlearning for Cross-Organizational Collaboration](https://arxiv.org/abs/2412.13551) (2024) — Combines federated LLM training, blockchain-style auditability, and deletion across organizations.
- [UOE: Unlearning One Expert Is Enough For Mixture-of-experts LLMS](https://arxiv.org/abs/2411.18797) (2024) — Shows that deleting a single expert can sometimes suffice to remove an unwanted capability in MoE models.
- [Federated TrustChain: Blockchain-Enhanced LLM Training and Unlearning](https://arxiv.org/abs/2406.04076) (2024) — Uses blockchain infrastructure to track, verify, and coordinate federated LLM deletion.

- [UnRe: Zero-Shot LLM Unlearning via Dynamic Contextual Retrieval](https://openreview.net/forum?id=3ZesmvOJ6o) (2026) — Retrieval-augmented, inference-time framework for zero-shot unlearning using only forget data.
### Recommendation, code, biomedical, agents, and other domain settings

- [U-CAN: Utility-Aware Contrastive Attenuation for Efficient Unlearning in Generative Recommendation](https://arxiv.org/abs/2602.23400) (2026) — Tailors deletion to generative recommendation systems with explicit utility-aware contrastive attenuation.
- [Agentic Unlearning: When LLM Agent Meets Machine Unlearning](https://arxiv.org/abs/2602.17692) (2026) — Extends deletion from standalone chat models to agent workflows with planning, memory, and tool use.
- [Towards Fair Large Language Model-based Recommender Systems without Costly Retraining](https://arxiv.org/abs/2601.17492) (2026) — Uses deletion-style updates to improve fairness in LLM recommenders without full retraining. [[code](https://github.com/JinLi-i/FUDLR)]
- [When Forgetting Builds Reliability: LLM Unlearning for Reliable Hardware Code Generation](https://arxiv.org/abs/2512.05341) (2025) — Removes harmful or misleading code patterns to improve reliability in hardware code generation.
- [Delete and Retain: Efficient Unlearning for Document Classification](https://arxiv.org/abs/2512.13711) (2025) — Studies efficient deletion in a classical document-classification setting where retain accuracy remains central.
- [Hierarchical Dual-Strategy Unlearning for Biomedical and Healthcare Intelligence Using Imperfect and Privacy-Sensitive Medical Data](https://arxiv.org/abs/2511.19498) (2025) — Uses a dual-strategy hierarchy to handle imperfect, sensitive medical data in biomedical deletion.
- [Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning](https://arxiv.org/abs/2509.13755) (2025) — Targets memorized secrets and proprietary snippets in code language models.
- [Customized Retrieval-Augmented Generation with LLM for Debiasing Recommendation Unlearning](https://arxiv.org/abs/2511.05494) (2025) — Combines customized RAG with unlearning to debias recommendation outputs.
- [From Learning to Unlearning: Biomedical Security Protection in Multimodal Large Language Models](https://arxiv.org/abs/2508.04192) (2025) — Applies deletion to secure biomedical multimodal models against privacy and safety risks.
- [Agents Are All You Need for LLM Unlearning](https://arxiv.org/abs/2502.00406) (2025) — Uses agentic loops to plan, diagnose, and execute deletion steps rather than relying on one-shot training.
- [Large Language Model Unlearning for Source Code](https://arxiv.org/abs/2506.17125) (2025) — Adapts deletion techniques to code models where syntax, compilation, and secret leakage all matter.
- [AegisLLM: Scaling Agentic Systems for Self-Reflective Defense in LLM Security](https://arxiv.org/abs/2504.20965) (2025) — Builds a self-reflective agentic defense stack that can diagnose and respond to LLM security failures. [[code](https://github.com/zikuicai/aegisllm)]
- [Tool Unlearning for Tool-Augmented LLMs](https://arxiv.org/abs/2502.01083) (2025) — Removes tool-use behaviors or tool-specific traces from models that can call external systems. [[code](https://github.com/CLU-UML/MU-Bench)]
- [ALU: Agentic LLM Unlearning](https://arxiv.org/abs/2502.00406) (2025) — Casts deletion as an agentic pipeline that iteratively plans, critiques, and repairs unlearning failures.
- [Unlearning Trojans in Large Language Models: A Comparison Between Natural Language and Source Code](https://arxiv.org/abs/2408.12416) (2024) — Compares how trojan removal differs between natural-language models and code models.
- [Hotfixing Large Language Models for Code](https://arxiv.org/abs/2408.05727) (2024) — Uses patch-like interventions to quickly remove bad or unsafe behaviors from code LLMs.
- [Unlearning Climate Misinformation in Large Language Models](https://arxiv.org/abs/2405.19563) (2024) — Treats climate misinformation as a domain-specific deletion target.
- [Exact and Efficient Unlearning for Large Language Model-based Recommendation](https://arxiv.org/abs/2404.10327) (2024) — Develops exact and efficient deletion methods tailored to LLM-based recommender systems.
- [Towards Efficient and Effective Unlearning of Large Language Models for Recommendation](https://arxiv.org/abs/2403.03536) (2024) — Explores practical trade-offs for deleting recommendation-relevant data in LLM recommenders. [[code](https://github.com/justarter/E2URec)]

## Frameworks

| Framework                     | Description                                                                                  | Link                                                                                                        |
| ----------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Open Unlearning               | Open-source framework for training, benchmarking, and reproducing LLM unlearning methods.    | [repo](https://github.com/locuslab/open-unlearning)                                                         |
| Vision Unlearning             | Open-source toolkit for machine unlearning experiments in vision and multimodal settings.    | [repo](https://github.com/LeonardoSanBenitez/vision-unlearning)                                             |
| Machine Unlearning Comparator | Comparator framework for standardized side-by-side evaluation of machine unlearning methods. | [paper](https://arxiv.org/abs/2508.12730) · [code](https://github.com/gnueaj/Machine-Unlearning-Comparator) |

## Blog Posts

- [Machine Unlearning in 2024](https://ai.stanford.edu/~kzliu/blog/unlearning) (2024) — Practitioner-friendly overview of definitions, limitations, and open questions in modern machine unlearning.
- [Deep Forgetting & Unlearning for Safely-Scoped LLMs](https://www.alignmentforum.org/posts/mFAvspg4sXkrfZ7FA/deep-forgetting-and-unlearning-for-safely-scoped-llms) (2023) — Alignment-oriented essay on using deep forgetting to scope LLM behavior more safely.

## Datasets and Benchmarks

| Dataset / benchmark | What it contains                                                                          | Primary paper                                      |
| ------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **TOFU**            | Controllable fictitious biographies and facts for targeted LLM unlearning experiments     | [TOFU](https://arxiv.org/abs/2401.06121)           |
| **MUSE**            | Six-way evaluation covering forget quality, utility, robustness, and side effects         | [MUSE](https://openreview.net/forum?id=TArmA033BU) |
| **WMDP**            | Hazardous and malicious-use benchmark for safety-oriented unlearning                      | [WMDP](https://arxiv.org/abs/2403.03218)           |
| **RWKU**            | Real-world knowledge unlearning benchmark beyond fictitious facts                         | [RWKU](https://arxiv.org/abs/2406.10890)           |
| **BLUR**            | Benchmark designed to be robust to forget-retain overlap                                  | [BLUR](https://arxiv.org/abs/2506.15699)           |
| **Behemoth**        | Fully synthetic benchmark for controlled large-scale unlearning studies                   | [Behemoth](https://arxiv.org/abs/2601.23153)       |
| **RippleBench**     | Benchmark for measuring ripple effects of forgetting across linked knowledge repositories | [RippleBench](https://arxiv.org/abs/2512.04144)    |
| **MLLMU-Bench**     | Privacy benchmark for multimodal large language model unlearning                          | [MLLMU-Bench](https://arxiv.org/abs/2410.22108)    |
| **OFFSIDE**         | Benchmark for unlearning misinformation in multimodal LLMs                                | [OFFSIDE](https://arxiv.org/abs/2510.22535)        |
| **PEBench**         | Fictitious multimodal benchmark for machine unlearning in MLLMs                           | [PEBench](https://arxiv.org/abs/2503.12545)        |
| **PULSE**           | Practical multimodal evaluation scenarios for post-unlearning behavior                    | [PULSE](https://arxiv.org/abs/2507.01271)          |
| **MedForget**       | Medical multimodal unlearning testbed with hierarchy-aware tasks                          | [MedForget](https://arxiv.org/abs/2512.09867)      |
| **Hubble**          | Model suite for systematic memorization and residual-leakage studies                      | [Hubble](https://arxiv.org/abs/2510.19811)         |
| **PISTOL**          | Dataset compilation pipeline for structural knowledge unlearning                          | [PISTOL](https://arxiv.org/abs/2406.16810)         |

## Contributing

Contributions welcome! Please open a PR if you know of papers, benchmarks, or tools related to LLM unlearning. See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed criteria, section placement, and formatting guidance.

- **Inclusion criteria:** The work should study deletion, suppression, or controllable forgetting of targeted knowledge, data, or behaviors in LLMs or closely related multimodal and deployment settings, or directly enable evaluation and implementation of unlearning.
- **Entry format:** `[Title](url) (Year) — One-line description.` Add `[[code](url)]` when an official implementation is available.

## Citation

If you find this resource useful, please cite it as:

```bibtex
@software{awesome-llm-unlearning,
  title = {{Awesome Large Language Model Unlearning}},
  author = {Liu, Chris Yuhao},
  year = {2024},
  doi = {10.5281/zenodo.19411433},
  url = {https://github.com/chrisliu298/awesome-llm-unlearning},
  version = {v1.0.0}
}
```

---

*Last updated: 2026-04-10. Coverage: 451 papers, 15 surveys and position papers, 3 frameworks, and 2 blog posts through April 2026.*

<!-- Paper count: source=451, output=451 -->
