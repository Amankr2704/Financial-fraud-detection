# Financial Fraud Detection Using Machine Learning and Deep Learning

A notebook-first project using the synthetic PaySim dataset. The planned work compares six machine learning models and an artificial neural network, emphasizing fraud detection under severe class imbalance. Logistic-regression, decision-tree, Gaussian Naive Bayes, Random Forest and XGBoost baselines have been compared on validation data; KNN, the neural network and final evaluation are pending.

## Project structure

- `data/raw/` - original PaySim CSV, excluded from Git.
- `data/processed/` - locally generated data, excluded from Git.
- `notebooks/01_data_setup.ipynb` - dataset setup and initial checks.
- `notebooks/02_exploratory_analysis.ipynb` - exploratory analysis.
- `notebooks/03_logistic_regression_baseline.ipynb` - fixed split, baseline training and validation.
- `notebooks/04_model_comparison.ipynb` - class-weighting ablation and decision-tree comparison on the same split.
- `notebooks/05_random_forest_naive_bayes.ipynb` - Random Forest and Naive Bayes comparison on the same split.
- `notebooks/06_xgboost_comparison.ipynb` - XGBoost training and validation comparison.
- `models/logistic_regression_baseline.joblib` - small baseline checkpoint with preprocessing, model and configuration.
- `models/weighted_logistic_regression.joblib` and `models/decision_tree_baseline.joblib` - checkpoints from notebook 04.
- `models/gaussian_naive_bayes.joblib` and `models/random_forest_baseline.joblib` - checkpoints from notebook 05.
- `models/xgboost_baseline.joblib` - XGBoost pipeline checkpoint; `models/xgboost_baseline.ubj` - native booster only, requiring the pipeline preprocessing.
- `src/` - reusable project code, to be added during development.
- `results/figures/` and `results/metrics/` - generated results.
- `reports/` - report materials.

See [data/README.md](data/README.md) for dataset download and placement. Never load a joblib checkpoint from an untrusted source; loading it can execute code.

## Environment and running the baseline

The current working environment is Windows 64-bit, Python 3.15.2, and the pinned packages in `requirements.txt`. From an existing matching environment, install with `python -m pip install -r requirements.txt`. To create a new environment on this computer, first confirm the Python 3.15.2 executable location, then run in PowerShell from the repository root:

```powershell
& "$env:LOCALAPPDATA\Python\pythoncore-3.15-64\python.exe" -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

On another computer, use that computer's Python 3.15.2 executable instead. In VS Code, open a notebook, select the matching `.venv` kernel and click **Run All**. If `.venv` already exists, use it rather than recreating it; the commands above create an environment only when needed.

Running `03_logistic_regression_baseline.ipynb` reads the original CSV, verifies its SHA-256, trains the model, displays validation metrics and charts, and writes or replaces the baseline checkpoint. It does not evaluate the model on the reserved test partition.

Running `04_model_comparison.ipynb` retrains the unweighted and class-weighted logistic models and a decision tree using the same split, compares validation results and writes the two additional checkpoints. The test partition remains unscored.

Running `05_random_forest_naive_bayes.ipynb` verifies and loads the earlier trusted logistic and decision-tree checkpoints, trains Gaussian Naive Bayes and a resource-limited Random Forest, reports validation results, and saves two more checkpoints. The forest uses 20 trees and a 10% bootstrap sample per tree; the test partition remains unscored.

Running `06_xgboost_comparison.ipynb` trains CPU XGBoost, compares validation results with the stored tree and forest baselines, and saves and verifies the XGBoost checkpoint and native booster. It does not score the test partition.

## Reproducibility status and limitations

The baseline notebook records package versions, the input fingerprint, feature choices and the seed and procedure for a stratified 70/15/15 split. It fits preprocessing on the training partition and selects a decision threshold using validation data. Results may vary across platforms and library versions; a clean-environment reproduction and the full project reproducibility declaration are still pending.

The preceding exploratory notebook examined aggregate properties of the complete dataset, so the reserved test partition has been included in that aggregate exploration even though it has not been used to fit or score the baseline. The transaction-level random split is not a chronological or account-disjoint evaluation. PaySim is synthetic and these results do not establish real-world performance.
