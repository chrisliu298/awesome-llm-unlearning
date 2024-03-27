# Awesome Large Language Model Unlearning

This repository tracks the latest research on machine unlearning in large language models (LLMs). The goal is to offer a comprehensive list of papers, datasets, and resources relevant to the topic.

> [!NOTE]
> If you believe your paper on LLM unlearning is not included, or if you find a mistake, typo, or information that is not up to date, please open an issue, and I will address it as soon as possible.

## Papers

### Methods

| Paper                                                                                                                                                   | Venue                       | Year-Month | Author(s)             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ---------- | --------------------- |
| [The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning](https://arxiv.org/abs/2403.03218)                                            | -                           | 2024-03    | Li et al.             |
| [Dissecting Language Models: Machine Unlearning via Selective Pruning](https://arxiv.org/abs/2403.01267)                                                | -                           | 2024-03    | Pochinkov and Schoots |
| [Second-Order Information Matters: Revisiting Machine Unlearning for Large Language Models](https://arxiv.org/abs/2403.10557)                           | -                           | 2024-03    | Gu et al.             |
| [Ethos: Rectifying Language Models in Orthogonal Parameter Space](https://arxiv.org/abs/2403.08994)                                                     | -                           | 2024-03    | Gao et al.            |
| [Towards Efficient and Effective Unlearning of Large Language Models for Recommendation](https://arxiv.org/abs/2403.03536)                              | -                           | 2024-03    | Wang et al.           |
| [Guardrail Baselines for Unlearning in LLMs](https://arxiv.org/abs/2403.03329)                                                                          | ICLR 2024 SeT-LLM Workshop  | 2024-03    | Thaker et al.         |
| [Deciphering the Impact of Pretraining Data on Large Language Models through Machine Unlearning](https://arxiv.org/abs/2402.11537)                      | -                           | 2024-02    | Zhao et al.           |
| [Unmemorization in Large Language Models via Self-Distillation and Deliberate Imagination](https://arxiv.org/abs/2402.10052)                            | -                           | 2024-02    | Dong et al.           |
| [Towards Safer Large Language Models through Machine Unlearning](https://arxiv.org/abs/2402.10058)                                                      | -                           | 2024-02    | Liu et al.            |
| [Selective Forgetting: Advancing Machine Unlearning Techniques and Evaluation in Language Models](https://arxiv.org/abs/2402.05813)                     | -                           | 2024-02    | Wang et al.           |
| [Unlearnable Algorithms for In-context Learning](https://arxiv.org/abs/2402.00751)                                                                      | -                           | 2024-02    | Muresanu et al.       |
| [Machine Unlearning of Pre-trained Large Language Models](https://arxiv.org/abs/2402.15159)                                                             | -                           | 2024-02    | Yao et al.            |
| [Visual In-Context Learning for Large Vision-Language Models](https://arxiv.org/abs/2402.11574)                                                         | -                           | 2024-02    | Zhou et al.           |
| [EFUF: Efficient Fine-grained Unlearning Framework for Mitigating Hallucinations in Multimodal Large Language Models](https://arxiv.org/abs/2402.09801) | -                           | 2024-02    | Xing et al.           |
| [Unlearning Reveals the Influential Training Data of Language Models](https://arxiv.org/abs/2401.15241)                                                 | -                           | 2024-01    | Isonuma and Titov     |
| [Large Language Model Unlearning](https://arxiv.org/abs/2310.10683)                                                                                     | ICLR 2024                   | 2023-14    | Yao et al.            |
| [FairSISA: Ensemble Post-Processing to Improve Fairness of Unlearning in LLMs](https://arxiv.org/abs/2312.07420)                                        | NeurIPS 2023 SoLaR Workshop | 2023-12    | Kadhe et al.          |
| [Making Harmful Behaviors Unlearnable for Large Language Models](https://arxiv.org/abs/2311.02105)                                                      | -                           | 2023-11    | Zhou et al.           |
| [Forgetting before Learning: Utilizing Parametric Arithmetic for Knowledge Updating in Large Language Models](https://arxiv.org/abs/2311.08011)         | -                           | 2023-11    | Ni et al.             |
| [Who's Harry Potter? Approximate Unlearning in LLMs](https://arxiv.org/abs/2310.02238)                                                                  | -                           | 2023-10    | Eldan and Russinovich |
| [DEPN: Detecting and Editing Privacy Neurons in Pretrained Language Models](https://arxiv.org/abs/2310.20138)                                           | EMNLP 2023                  | 2023-10    | Wu et al.             |
| [Unlearn What You Want to Forget: Efficient Unlearning for LLMs](https://aclanthology.org/2023.emnlp-main.738/)                                         | EMNLP 2023                  | 2023-10    | Chen and Yang         |
| [In-Context Unlearning: Language Models as Few Shot Unlearners](https://arxiv.org/abs/2310.07579)                                                       | -                           | 2023-10    | Pawelczyk et al.      |
| [Forgetting Private Textual Sequences in Language Models via Leave-One-Out Ensemble](https://arxiv.org/abs/2309.16082)                                  | -                           | 2023-09    | Liu and Kalinli       |
| [Can Sensitive Information Be Deleted From LLMs? Objectives for Defending Against Extraction Attacks](https://arxiv.org/abs/2309.17410)                 | -                           | 2023-09    | Patil et al.          |
| [Separate the Wheat from the Chaff: Model Deficiency Unlearning via Parameter-Efficient Module Operation](https://arxiv.org/abs/2308.08090)             | AAAI 2024                   | 2023-08    | Hu et al.             |
| [Unlearning Bias in Language Models by Partitioning Gradients](https://aclanthology.org/2023.findings-acl.375/)                                         | ACL (Findings) 2023         | 2023-07    | Yu et al.             |
| [Make Text Unlearnable: Exploiting Effective Patterns to Protect Personal Data](https://arxiv.org/abs/2307.00456)                                       | -                           | 2023-07    | Li et al.             |
| [What can we learn from Data Leakage and Unlearning for Law?](https://arxiv.org/abs/2307.10476)                                                         | -                           | 2023-07    | Borkar                |
| [LEACE: Perfect linear concept erasure in closed form](https://arxiv.org/abs/2306.03819)                                                                | NeurIPS 2023                | 2023-06    | Belrose et al.        |
| [Composing Parameter-Efficient Modules with Arithmetic Operations](https://arxiv.org/abs/2306.14870)                                                    | NeurIPS 2023                | 2023-06    | Zhang et al.          |
| [KGA: A General Machine Unlearning Framework Based on Knowledge Gap Alignment](https://arxiv.org/abs/2305.06535)                                        | -                           | 2023-05    | Wang et al.           |
| [Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089)                                                                                 | ICLR 2023                   | 2022-12    | Ilharco et al.        |
| [Privacy Adhering Machine Un-learning in NLP](https://arxiv.org/abs/2212.09573)                                                                         | -                           | 2022-12    | Kumar et al.          |
| [The CRINGE Loss: Learning what language not to model](https://arxiv.org/abs/2211.05826)                                                                | -                           | 2022-11    | Adolphs et al.        |
| [Knowledge Unlearning for Mitigating Privacy Risks in Language Models](https://arxiv.org/abs/2210.01504)                                                | -                           | 2022-10    | Jang et al.           |
| [Quark: Controllable Text Generation with Reinforced Unlearning](https://arxiv.org/abs/2205.13636)                                                      | NeurIPS 2022                | 2022-05    | Lu et al.             |
| [DExperts: Decoding-Time Controlled Text Generation with Experts and Anti-Experts](https://arxiv.org/abs/2105.03023)                                    | ACL 2021                    | 2021-05    | Liu et al.            |
|                                                                                                                                                         |                             |            |                       |

### Surveys and Position Papers

| Paper                                                                                                                                  | Venue | Year-Month | Author(s)    |
| -------------------------------------------------------------------------------------------------------------------------------------- | ----- | ---------- | :----------- |
| [The Frontier of Data Erasure: Machine Unlearning for Large Language Models](https://arxiv.org/abs/2403.15779)                         | -     | 2024-03    | Qu et al.    |
| [Rethinking Machine Unlearning for Large Language Models](https://arxiv.org/abs/2402.08787)                                            | -     | 2024-02    | Liu et al.   |
| [Eight Methods to Evaluate Robust Unlearning in LLMs](https://arxiv.org/abs/2402.16835)                                                | -     | 2024-02    | Lynch et al. |
| [Knowledge Unlearning for LLMs: Tasks, Methods, and Challenges](https://arxiv.org/abs/2311.15766)                                      | -     | 2023-11    | Si et al.    |
| [Right to be Forgotten in the Era of Large Language Models: Implications, Challenges, and Solutions](https://arxiv.org/abs/2307.03941) | -     | 2023-07    | Zhang et al. |

## Datasets

| Dataset                                               | Description                                                                                                                               | Link to Paper                            |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| [TOFU](https://huggingface.co/datasets/locuslab/TOFU) | A synthetic dataset of fictitious authors generated by GPT-4.                                                                             | [Link](https://arxiv.org/abs/2401.06121) |
| [WMDP](https://huggingface.co/datasets/cais/wmdp)     | An expert-annotated benchmark of harzardous knowledge in biology, chemistry, and cybersecurity, in the form of multiple-choice questions. | [Link](https://arxiv.org/abs/2403.03218) |
