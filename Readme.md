<p align="center">
  <img src="Figures/PerGent.jpg" alt="PerGent Approach Overview" width="90%"/>
</p>

<h1 align="center">Agentic Persona Generation with Critique-Refinement: An Industrial Evaluation</h1>

<p align="center">
  <b>
    <a href="https://github.com/mhamini">Mohammad Hossein Amini</a><sup>1,2</sup> &nbsp;·&nbsp;
    <a href="https://github.com/">David Dewar</a><sup>2</sup> &nbsp;·&nbsp;
    <a href="https://github.com/">Shiva Nejati</a><sup>1</sup> &nbsp;·&nbsp;
    <a href="https://github.com/">Mehrdad Sabetzadeh</a><sup>1</sup>
  </b>
</p>

<p align="center">
  <sup>1</sup> University of Ottawa, Canada &nbsp;&nbsp;
  <sup>2</sup> Kinaxis, Canada
</p>

<p align="center">
  <code>{mh.amini, snejati, m.sabetzadeh}@uottawa.ca</code> &nbsp;&nbsp;
  <code>ddewar@kinaxis.com</code>
</p>

---

## 📄 Abstract

Personas are widely used in software engineering to support requirements elicitation, design, and validation, but their manual creation is costly, time-consuming, and hard to scale. Recent LLM-based approaches automate persona generation from textual data; however, they typically rely on single-shot generation and subjective evaluations, limiting practical reliability. We present PerGent, an industry-grade method for persona generation built around an iterative critique-refinement loop. Specifically, PerGent uses a generator and a critic LLM agent, coordinated by an orchestrator, to iteratively refine personas using external resources such as interviews, surveys, and job postings through a critique-refinement loop with a user-defined maximum number of rounds. We deploy and evaluate PerGent in an industrial setting at Kinaxis, comparing it with three baselines, including state-of-the-art one-shot methods. In an expert in-situ evaluation, PerGent achieved the highest expert approval rate (96.9%), exceeding all baselines. We further compare PerGent-generated personas with best-practice personas manually created by domain experts prior to the adoption of LLMs. Compared to baselines, PerGent reproduces a larger proportion of expert content while also contributing substantial new content beyond the pre-LLM personas. We conclude with lessons learned from deploying and evaluating PerGent at Kinaxis.

## 🏗️ Repository Structure

```
.
├── Code/                           # Runnable demos for PerGent and baseline scripts
│   ├── pergent.py                  # PerGent orchestration entry point
│   ├── pergent_no_res.py           # PerGent without external resources (PerGentNoRes baseline)
│   ├── oneshot.py                  # OneShot baseline
│   ├── oneshot_res.py              # OneShot+Res baseline
│   ├── pergent_generator.txt       # PerGent generator prompt/template
│   ├── pergent_critic.txt          # PerGent critic prompt/template
│   ├── oneshot_generator.txt       # OneShot prompt/template
│   ├── api.txt                     # API key placeholder (local only)
│   └── README.md                   # Usage notes and setup steps
├── Experiments/                    # Data and scripts for research questions
│   ├── RQ1/                        # Edit rates for generated personas
│   ├── RQ2/                        # Similarity metrics and statistical tests
│   ├── RQ3/                        # Token and API usage statistics
│   └── README.md                   # RQ data and script descriptions
├── Figures/                        # Plots and figures from the paper
│   └── ...                         # Figures illustrating methodology and evaluation results
├── Prompts/                        # Prompt outlines for PerGent agents & baselines
│   └── ...
├── Sample Personas/                # Generated example personas (illustration only)
│   ├── README.md                   # Notes about persona provenance and purpose
│   ├── demand_planner.md           # Example persona: Demand Planner
│   └── supply_planner.md           # Example persona: Supply Planner
├── Edit Examples/                  # Expert edits applied to generated personas
│   └── README.md                   # Describes edit examples and provenance
├── Supplementary Materials/        # Additional resources and detailed documentation
│   └── ...
└── Readme.md                       # This file
```

| Folder                                                   | Description                                                                                                                         |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| [`Code/`](Code/)                                         | Minimal runnable demo of the PerGent agent orchestration with setup notes.                                                          |
| [`Experiments/`](Experiments/)                           | Data and scripts organized by research question (RQ1-RQ3).                                                                          |
| [`Figures/`](Figures/)                                   | Contains plots and figures illustrating our methodology, tools architecture, and evaluation results.                                |
| [`Prompts/`](Prompts/)                                   | Contains the prompt outlines used in the **PerGent** agentic pipeline and the baseline approaches described in the paper.           |
| [`Supplementary Materials/`](Supplementary%20Materials/) | Contains a PDF with supplementary materials, plus a sample persona artifact generated by PerGent as an illustration.                |
| [`Sample Personas/`](Sample%20Personas/)                 | Contains two example personas generated from public job postings for illustration only; no proprietary partner resources were used. |
| [`Edit Examples/`](Edit%20Examples/)                     | Contains examples of edits that domain experts applied to generated personas, demonstrating typical corrections and refinements.    |

---

## 🔍 Overview

This repository hosts the artifacts accompanying the paper **"Agentic Persona Generation with Critique-Refinement: An Industrial Evaluation"**. We present **PerGent**, an agentic framework for automated persona generation, evaluated in an industrial in-situ setting. The repository provides the prompt templates, evaluation materials, and supplementary documentation to support reproducibility and transparency of our research.

---

## 📂 Contents

### Code

The [`Code/`](Code/) directory contains runnable scripts for the PerGent pipeline and the baselines used in the experiments:

- `pergent.py` — PerGent end-to-end orchestration (generator + critic + orchestrator).
- `pergent_no_res.py` — PerGent variant without the external resources (PerGentNoRes baseline).
- `oneshot.py` — OneShot baseline.
- `oneshot_res.py` — OneShot+Res baseline (OneShot with external resources).
- Prompt/template files: `pergent_generator.txt`, `pergent_critic.txt`, `oneshot_generator.txt`.
- `api.txt` — local placeholder for your API key.

See usage notes and quick examples in [`Code/README.md`](Code/README.md).

### Experiments

The [`Experiments/`](Experiments/) directory contains the data and scripts for each research question:

- **RQ1**: Edit percentages for persona items (see `log_percentages.csv`).
- **RQ2**: Similarity measurements, averages, and statistical tests (`measurements.csv`, `avg.csv`, `stat.csv`, `average.py`, `stat.py`).
- **RQ3**: Token and API usage statistics (`tokens.csv`, `avg.csv`, `average.py`).

See the details in [`Experiments/README.md`](Experiments/README.md).

### Prompts

The [`Prompts/`](Prompts/) directory contains the prompt outlines used by:

- **PerGent Agents** — the agentic persona generation pipeline.
- **Baselines** — the baseline approaches compared against PerGent in our evaluation.

### Figures

The [`Figures/`](Figures/) directory includes:

- Architectural diagrams of the PerGent framework.
- Methodology illustrations.
- Evaluation result plots.

### Supplementary Materials

The [`Supplementary Materials/`](Supplementary%20Materials/) directory includes:

- A PDF document detailing the **LLM-as-Judge** calibration process.
- Complete prompt outlines for PerGent's agents.
- Baseline prompt templates.
- A sample persona artifact generated by PerGent from five public job postings (`sample_persona.html`).

---

<!-- ## 📖 Citation

If you find this work useful, please cite our paper:

```bibtex
@inproceedings{amini2025pergent,
  title     = {Agentic Persona Generation in Industry: An In-Situ Evaluation and Lessons Learned},
  author    = {Amini, Mohammad Hossein and Dewar, David and Nejati, Shiva and Sabetzadeh, Mehrdad},
  booktitle = {Proceedings of [Conference Name]},
  year      = {2026}
}
``` -->

<!-- --- -->

## 📜 License

This repository is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

For questions or discussions about this work, please open an [issue](../../issues) or contact us at:

- **Mohammad Hossein Amini** — [mh.amini@uottawa.ca](mailto:mh.amini@uottawa.ca)
- **David Dewar** — [ddewar@kinaxis.com](mailto:ddewar@kinaxis.com)
- **Shiva Nejati** — [snejati@uottawa.ca](mailto:snejati@uottawa.ca)
- **Mehrdad Sabetzadeh** — [m.sabetzadeh@uottawa.ca](mailto:m.sabetzadeh@uottawa.ca)
