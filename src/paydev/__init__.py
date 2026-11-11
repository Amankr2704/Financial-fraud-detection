"""Shared helpers for the PaySim fraud-detection notebooks.

Notebooks import from here instead of repeating dataset discovery,
hash verification and validation logic in every notebook.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np
import pandas as pd

# ---------------------------------------------------------------- paths ----
_CSV_NAME = "PS_20174392719_1491204439457_log.csv"

# ---------------------------------------------------------------- config ---
EXPECTED_SHA256 = "16910f90577b0d981bf8ff289714510bb89bc71bff7d3f220f024e287e4eea6b"
SEED = 42
NUMERIC = ["step", "amount", "oldbalanceOrg", "oldbalanceDest"]
CATEGORICAL = ["type"]
FEATURES = NUMERIC + CATEGORICAL
DTYPES = {"step": "int16", "type": "category", "amount": "float32",
          "oldbalanceOrg": "float32", "oldbalanceDest": "float32", "isFraud": "int8"}
SPLIT = "stratified 70/15/15, two train_test_split calls"


def find_root(start: Path | None = None) -> Path:
    """Walk up from ``start`` (default: cwd) to the project folder."""
    cwd = (start or Path.cwd()).resolve()
    root = next((p for p in (cwd, *cwd.parents) if (p / "data" / "README.md").is_file()), None)
    if root is None:
        raise FileNotFoundError("Open the notebook from inside the project folder.")
    return root


def data_path(root: Path) -> Path:
    return root / "data" / "raw" / _CSV_NAME


def sha256_file(path: Path, block_size: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(block_size), b""):
            digest.update(block)
    return digest.hexdigest()


def load_dataset(root: Path, *, verify_hash: bool = True) -> tuple[pd.DataFrame, str]:
    """Load the PaySim CSV with the project dtype map and validate it.

    Returns ``(df, actual_sha256)``. Raises ``ValueError`` when the
    fingerprint differs from ``EXPECTED_SHA256``, when values are
    missing, or when the target is not binary {0, 1}.
    """
    path = data_path(root)
    if not path.is_file():
        raise FileNotFoundError(f"Dataset not found: {path}. See data/README.md.")

    actual_sha256 = sha256_file(path)
    if verify_hash and actual_sha256 != EXPECTED_SHA256:
        raise ValueError("Dataset SHA-256 differs from the project copy; "
                         "verify the input before comparing results.")

    df = pd.read_csv(path, usecols=FEATURES + ["isFraud"], dtype=DTYPES)
    if df[FEATURES + ["isFraud"]].isna().any().any():
        raise ValueError("Missing inputs found; inspect data and add a train-fitted imputation strategy.")
    if set(df["isFraud"].unique()) != {0, 1}:
        raise ValueError("Expected binary target values 0 and 1.")
    return df, actual_sha256


def stratified_splits(y: np.ndarray, seed: int = SEED):
    """Deterministic stratified 70/15/15 split of row ids."""
    from sklearn.model_selection import train_test_split

    row_ids = np.arange(len(y))
    train_ids, holdout_ids = train_test_split(row_ids, test_size=0.30, random_state=seed, stratify=y)
    val_ids, test_ids = train_test_split(holdout_ids, test_size=0.50, random_state=seed, stratify=y[holdout_ids])
    assert len(train_ids) + len(val_ids) + len(test_ids) == len(y)
    assert len(np.intersect1d(train_ids, val_ids)) == 0
    assert len(np.intersect1d(train_ids, test_ids)) == 0
    assert len(np.intersect1d(val_ids, test_ids)) == 0
    return train_ids, val_ids, test_ids


def environment_banner(dataset: Path) -> str:
    import sys
    import sklearn

    return (f"Python {sys.version.split()[0]} | pandas {pd.__version__} | "
            f"NumPy {np.__version__} | scikit-learn {sklearn.__version__}")
