# Financial Fraud Detection Using Machine Learning and Deep Learning

A notebook-first project using the synthetic PaySim dataset. The planned work compares six machine learning models and an artificial neural network, emphasizing fraud detection under severe class imbalance. This repository is currently at the initial setup stage; experiments and results are not yet available.

## Project structure

- `data/raw/` - place the original PaySim CSV here (not uploaded to Git).
- `data/processed/` - locally generated data (not uploaded to Git).
- `notebooks/` - Jupyter notebooks, beginning with a dataset check.
- `src/` - reusable project code, to be added during development.
- `models/` - locally generated model files.
- `results/figures/` and `results/metrics/` - generated results.
- `reports/` - report materials.

See [data/README.md](data/README.md) for dataset download and placement.

## Open the starter notebook

Open this folder in VS Code, install the Microsoft Python and Jupyter extensions if prompted, and open `notebooks/01_data_setup.ipynb`. Select a Python 3.10 kernel with the packages in `requirements.txt`. To create an isolated environment in PowerShell from the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Then select the `.venv` interpreter as the notebook kernel. The requirements describe the initial inspection environment; additional training dependencies and exact experiment settings will be recorded when they are implemented.

## Reproducibility status

This initial setup contains no trained models or experimental results. A full reproducibility declaration, dataset fingerprint, experiment settings, commands and checkpoints will be added after the experiments are implemented and verified.
