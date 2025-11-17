import joblib

def load_model(path: str = "app/model/model.pkl"):
    with open(path, "rb") as f:
        model = joblib.load(path)
    return model
