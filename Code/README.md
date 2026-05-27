This folder provides a high-level illustration of the implementation for PerGent and the baseline used in the paper.

# Contents

- `pergent.py` — PerGent end-to-end orchestration (generator + critic + orchestrator).
- `pergent_no_res.py` — PerGent variant without the external resources (PerGentNoRes baseline).
- `oneshot.py` — OneShot baseline generator.
- `oneshot_res.py` — OneShot+Res baseline (OneShot with external resources).
- `pergent_generator.txt`, `pergent_critic.txt`, `oneshot_generator.txt` — prompt files used by the scripts.
- `api.txt` — local placeholder for your OpenAI API key (one line, the key only).

# Quick start

1. Make sure you have Python 3 installed.

2. Place your OpenAI (or compatible) API key in `api.txt` inside this folder. The file should contain only the key text.

3. Run any script using Python. Examples:

```bash
python pergent.py
python pergent_no_res.py
python oneshot.py
python oneshot_res.py
```

# Notes

- The scripts use the prompt files in this directory. Edit the `*_generator.txt` and `*_critic.txt` files to adjust behavior or to reproduce experiments.
- See the repository root `Readme.md` for pointers to the `Experiments/` folder and the evaluation materials.
- If your environment requires additional packages, install them as needed (this repo does not include an exhaustive requirements file).
