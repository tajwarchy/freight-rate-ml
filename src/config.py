from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT / "data"
MODELS_DIR = ROOT / "models"
OUTPUTS_DIR = ROOT / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"

TRAIN_PATH = DATA_DIR / "train_test.csv"
VALIDATION_PATH = DATA_DIR / "validation.csv"
TEMPLATE_PATH = DATA_DIR / "validation_predictions_template.csv"
DECEMBER_PATH = DATA_DIR / "december_chart_inputs.csv"

# Submission file lives at repo root (score.py is run against it)
PREDICTIONS_PATH = ROOT / "validation_predictions.csv"
DECEMBER_PREDICTIONS_PATH = OUTPUTS_DIR / "december_predictions.csv"

TARGET = "posted_rate"
ID_COL = "load_id"
DATE_COL = "date"

SEED = 42
