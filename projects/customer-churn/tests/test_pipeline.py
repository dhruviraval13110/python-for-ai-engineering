from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))
from pipeline import build_pipeline, make_dataset

def test_dataset_shape_and_target():
    df = make_dataset(100)
    assert df.shape == (100, 7)
    assert set(df["churned"].unique()) <= {0, 1}

def test_pipeline_fits():
    df = make_dataset(120)
    model = build_pipeline()
    model.fit(df.drop(columns="churned"), df["churned"])
    assert len(model.predict(df.drop(columns="churned"))) == 120
