import joblib
import pandas as pd

def load_model():
    return joblib.load("models/model.pkl")

def predict(data):
    model = load_model()
    df = pd.DataFrame([data])
    pred = model.predict(df)[0]
    prob = model.predict_proba(df).max()
    return pred, prob
