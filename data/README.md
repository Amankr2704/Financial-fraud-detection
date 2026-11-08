# Dataset

Source: [PaySim synthetic financial dataset on Kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1). The expected file is `PS_20174392719_1491204439457_log.csv`, containing approximately 6.36 million transactions. The CSV is too large for normal GitHub hosting and is intentionally excluded from Git.

Download the dataset from the source page, extract the ZIP, and place the CSV at:

```text
data/raw/PS_20174392719_1491204439457_log.csv
```

Then open `notebooks/01_data_setup.ipynb` and run the cells. A Kaggle sign-in may be required. Do not add credentials or the downloaded data to Git.

SHA-256 of the CSV used in the initial setup: `16910f90577b0d981bf8ff289714510bb89bc71bff7d3f220f024e287e4eea6b`.
