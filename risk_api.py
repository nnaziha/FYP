from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("risk_model_rf.pkl")

# FastAPI app
app = FastAPI()

# Root route for basic health check
@app.get("/")
def read_root():
    return {"message": "Risk Prediction API is running 🚀"}

# Input schema
class PatientData(BaseModel):
    Age: float
    Gender: int
    Duration_DM: float
    Insulin_Regimen: int
    DDS_1st: float
    HbA1c: float
    Freq_SMBG: float
    Freq_Hypo: float
    Freq_Visits: float
    eGFR: float
    CKD_Stage: int

# Predict endpoint
@app.post("/predict")
def predict_hba1c(data: PatientData):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)[0]
    return {"predicted_hba1c": round(prediction, 3)}
