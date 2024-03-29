# Awesome Large Language Model Unlearning

This repository tracks the latest research on machine unlearning in large language models (LLMs). The goal is to offer a comprehensive list of papers, datasets, and resources relevant to the topic.

> [!NOTE]
> If you believe your paper on LLM unlearning is not included, or if you find a mistake, typo, or information that is not up to date, please open an issue, and I will address it as soon as possible.
>
> If you want to add a new paper, feel free to either open an issue or create a pull request.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Papers](#papers)
  - [Methods](#methods)
  - [Surveys and Position Papers](#surveys-and-position-papers)
- [Blog Posts](#blog-posts)
- [Datasets](#datasets)

## Papers

### Methods

| Paper                                                                                                                                                   | Author(s)             | Year-Month | Venue                       | Code                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ---------- | --------------------------- | ----------------------------------------------------------- |
| [The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning](https://arxiv.org/abs/2403.03218)                                            | Li et al.             | 2024-03    | -                           | [GitHub](https://github.com/centerforaisafety/wmdp)         |
| [Dissecting Language Models: Machine Unlearning via Selective Pruning](https://arxiv.org/abs/2403.01267)                                                | Pochinkov and Schoots | 2024-03    | -                           |                                                             |
| [Second-Order Information Matters: Revisiting Machine Unlearning for Large Language Models](https://arxiv.org/abs/2403.10557)                           | Gu et al.             | 2024-03    | -                           |                                                             |
| [Ethos: Rectifying Language Models in Orthogonal Parameter Space](https://arxiv.org/abs/2403.08994)                                                     | Gao et al.            | 2024-03    | -                           |                                                             |
| [Towards Efficient and Effective Unlearning of Large Language Models for Recommendation](https://arxiv.org/abs/2403.03536)                              | Wang et al.           | 2024-03    | -                           |                                                             |
| [Guardrail Baselines for Unlearning in LLMs](https://arxiv.org/abs/2403.03329)                                                                          | Thaker et al.         | 2024-03    | ICLR 2024 SeT-LLM Workshop  |                                                             |
| [Deciphering the Impact of Pretraining Data on Large Language Models through Machine Unlearning](https://arxiv.org/abs/2402.11537)                      | Zhao et al.           | 2024-02    | -                           |                                                             |
| [Unmemorization in Large Language Models via Self-Distillation and Deliberate Imagination](https://arxiv.org/abs/2402.10052)                            | Dong et al.           | 2024-02    | -                           |                                                             |
| [Towards Safer Large Language Models through Machine Unlearning](https://arxiv.org/abs/2402.10058)                                                      | Liu et al.            | 2024-02    | -                           |                                                             |
| [Selective Forgetting: Advancing Machine Unlearning Techniques and Evaluation in Language Models](https://arxiv.org/abs/2402.05813)                     | Wang et al.           | 2024-02    | -                           |                                                             |
| [Unlearnable Algorithms for In-context Learning](https://arxiv.org/abs/2402.00751)                                                                      | Muresanu et al.       | 2024-02    | -                           |                                                             |
| [Machine Unlearning of Pre-trained Large Language Models](https://arxiv.org/abs/2402.15159)                                                             | Yao et al.            | 2024-02    | -                           |                                                             |
| [Visual In-Context Learning for Large Vision-Language Models](https://arxiv.org/abs/2402.11574)                                                         | Zhou et al.           | 2024-02    | -                           |                                                             |
| [EFUF: Efficient Fine-grained Unlearning Framework for Mitigating Hallucinations in Multimodal Large Language Models](https://arxiv.org/abs/2402.09801) | Xing et al.           | 2024-02    | -                           |                                                             |
| [Unlearning Reveals the Influential Training Data of Language Models](https://arxiv.org/abs/2401.15241)                                                 | Isonuma and Titov     | 2024-01    | -                           |                                                             |
| [TOFU: A Task of Fictitious Unlearning for LLMs](https://arxiv.org/abs/2401.06121)                                                                      | Maini et al.          | 2024-01    | -                           | [GitHub](https://github.com/locuslab/tofu)                  |
| [Large Language Model Unlearning](https://arxiv.org/abs/2310.10683)                                                                                     | Yao et al.            | 2023-14    | ICLR 2024                   | [GitHub](https://github.com/kevinyaobytedance/llm_unlearn)  |
| [FairSISA: Ensemble Post-Processing to Improve Fairness of Unlearning in LLMs](https://arxiv.org/abs/2312.07420)                                        | Kadhe et al.          | 2023-12    | NeurIPS 2023 SoLaR Workshop |                                                             |
| [Making Harmful Behaviors Unlearnable for Large Language Models](https://arxiv.org/abs/2311.02105)                                                      | Zhou et al.           | 2023-11    | -                           |                                                             |
| [Forgetting before Learning: Utilizing Parametric Arithmetic for Knowledge Updating in Large Language Models](https://arxiv.org/abs/2311.08011)         | Ni et al.             | 2023-11    | -                           |                                                             |
| [Who's Harry Potter? Approximate Unlearning in LLMs](https://arxiv.org/abs/2310.02238)                                                                  | Eldan and Russinovich | 2023-10    | -                           |                                                             |
| [DEPN: Detecting and Editing Privacy Neurons in Pretrained Language Models](https://arxiv.org/abs/2310.20138)                                           | Wu et al.             | 2023-10    | EMNLP 2023                  |                                                             |
| [Unlearn What You Want to Forget: Efficient Unlearning for LLMs](https://aclanthology.org/2023.emnlp-main.738/)                                         | Chen and Yang         | 2023-10    | EMNLP 2023                  | [GitHub](https://github.com/SALT-NLP/Efficient_Unlearning/) |
| [In-Context Unlearning: Language Models as Few Shot Unlearners](https://arxiv.org/abs/2310.07579)                                                       | Pawelczyk et al.      | 2023-10    | -                           |                                                             |
| [Forgetting Private Textual Sequences in Language Models via Leave-One-Out Ensemble](https://arxiv.org/abs/2309.16082)                                  | Liu and Kalinli       | 2023-09    | -                           |                                                             |
| [Can Sensitive Information Be Deleted From LLMs? Objectives for Defending Against Extraction Attacks](https://arxiv.org/abs/2309.17410)                 | Patil et al.          | 2023-09    | -                           |                                                             |
| [Separate the Wheat from the Chaff: Model Deficiency Unlearning via Parameter-Efficient Module Operation](https://arxiv.org/abs/2308.08090)             | Hu et al.             | 2023-08    | AAAI 2024                   |                                                             |
| [Unlearning Bias in Language Models by Partitioning Gradients](https://aclanthology.org/2023.findings-acl.375/)                                         | Yu et al.             | 2023-07    | ACL (Findings) 2023         |                                                             |
| [Make Text Unlearnable: Exploiting Effective Patterns to Protect Personal Data](https://arxiv.org/abs/2307.00456)                                       | Li et al.             | 2023-07    | -                           |                                                             |
| [What can we learn from Data Leakage and Unlearning for Law?](https://arxiv.org/abs/2307.10476)                                                         | Borkar                | 2023-07    | -                           |                                                             |
| [LEACE: Perfect linear concept erasure in closed form](https://arxiv.org/abs/2306.03819)                                                                | Belrose et al.        | 2023-06    | NeurIPS 2023                |                                                             |
| [Composing Parameter-Efficient Modules with Arithmetic Operations](https://arxiv.org/abs/2306.14870)                                                    | Zhang et al.          | 2023-06    | NeurIPS 2023                |                                                             |
| [KGA: A General Machine Unlearning Framework Based on Knowledge Gap Alignment](https://arxiv.org/abs/2305.06535)                                        | Wang et al.           | 2023-05    | -                           |                                                             |
| [Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089)                                                                                 | Ilharco et al.        | 2022-12    | ICLR 2023                   |                                                             |
| [Privacy Adhering Machine Un-learning in NLP](https://arxiv.org/abs/2212.09573)                                                                         | Kumar et al.          | 2022-12    | -                           |                                                             |
| [The CRINGE Loss: Learning what language not to model](https://arxiv.org/abs/2211.05826)                                                                | Adolphs et al.        | 2022-11    | -                           |                                                             |
| [Knowledge Unlearning for Mitigating Privacy Risks in Language Models](https://arxiv.org/abs/2210.01504)                                                | Jang et al.           | 2022-10    | -                           |                                                             |
| [Quark: Controllable Text Generation with Reinforced Unlearning](https://arxiv.org/abs/2205.13636)                                                      | Lu et al.             | 2022-05    | NeurIPS 2022                |                                                             |
| [DExperts: Decoding-Time Controlled Text Generation with Experts and Anti-Experts](https://arxiv.org/abs/2105.03023)                                    | Liu et al.            | 2021-05    | ACL 2021                    |                                                             |

### Surveys and Position Papers

| Paper                                                                                                                                  | Author(s)    | Year-Month | Venue |
| -------------------------------------------------------------------------------------------------------------------------------------- | :----------- | ---------- | ----- |
| [The Frontier of Data Erasure: Machine Unlearning for Large Language Models](https://arxiv.org/abs/2403.15779)                         | Qu et al.    | 2024-03    | -     |
| [Rethinking Machine Unlearning for Large Language Models](https://arxiv.org/abs/2402.08787)                                            | Liu et al.   | 2024-02    | -     |
| [Eight Methods to Evaluate Robust Unlearning in LLMs](https://arxiv.org/abs/2402.16835)                                                | Lynch et al. | 2024-02    | -     |
| [Knowledge Unlearning for LLMs: Tasks, Methods, and Challenges](https://arxiv.org/abs/2311.15766)                                      | Si et al.    | 2023-11    | -     |
| [Right to be Forgotten in the Era of Large Language Models: Implications, Challenges, and Solutions](https://arxiv.org/abs/2307.03941) | Zhang et al. | 2023-07    | -     |

## Blog Posts

| Blog                                                                                                                                                                | Author(s)                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [Deep Forgetting & Unlearning for Safely-Scoped LLMs](https://www.alignmentforum.org/posts/mFAvspg4sXkrfZ7FA/deep-forgetting-and-unlearning-for-safely-scoped-llms) | [Stephen Casper](https://stephencasper.com/) |

## Datasets

| Dataset                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                  | Link                                      |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| [TOFU](https://huggingface.co/datasets/locuslab/TOFU)     | A synthetic QA dataset of fictitious authors generated by GPT-4. The datasets comes with three splits of the retain/forget sets, including 99/1, 95/5, and 90/10 (in percentage). The dataset also includes questions about real authors and world facts to evaluate the loss of general knowledge after unlearning.                                                                         | [arXiv](https://arxiv.org/abs/2401.06121) |
| [WMDP](https://huggingface.co/datasets/cais/wmdp)         | A benchmark for assessing hazardous knowledge in biology, chemistry, and cybersecurity, containing over 4000 multiple-choice questions with similar style to MMLU. It also comes with the corpora in the three domains, and auxiliary corpora in economics, law, and physics as a task to unlearn subsets of MMLU.                                                                           | [arXiv](https://arxiv.org/abs/2403.03218) |
| [MMLU Subsets](https://huggingface.co/datasets/cais/mmlu) | A task proposed along with the WMDP dataset. The goal is to unlearn (retain) three categories in the [MMLU](https://arxiv.org/abs/2009.03300) dataset: economics (econometrics and others), physics (math and others), and law (jurisprudence and others). The task requires high-precision unlearning, because the retain sets are categories closely related to the unlearning categories. | [arXiv](https://arxiv.org/abs/2009.03300) |
