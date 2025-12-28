from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI(title="Heart Disease Prediction API")

model = joblib.load("heart_rf_model.pkl")
scaler = joblib.load("scaler_heart.pkl")

class HeartData(BaseModel):
    age: float
    sex: float
    cp: float
    trestbps: float
    chol: float
    fbs: float
    restecg: float
    thalach: float
    exang: float
    oldpeak: float
    slope: float
    ca: float
    thal: float

def predict_heart(data: HeartData):
    features = np.array([[data.age, data.sex, data.cp, data.trestbps, data.chol,
                          data.fbs, data.restecg, data.thalach, data.exang,
                          data.oldpeak, data.slope, data.ca, data.thal]])
    features_scaled = scaler.transform(features)
    pred = model.predict(features_scaled)[0]
    prob = model.predict_proba(features_scaled)[0][1]
    return {
        "heart_disease": "Yes" if pred==1 else "No",
        "risk_probability": round(prob*100, 2)
    }

@app.post("/analyze_heart")
def analyze_heart(data: HeartData):
    return predict_heart(data)

@app.get("/")
def home():
    return {"message": "Heart Disease API is running"}
