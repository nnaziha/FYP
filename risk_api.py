from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

from sklearn.linear_model import LinearRegression
import pandas as pd

np.random.seed(1)
n = 100

data = pd.DataFrame({
    'age': np.random.randint(30, 70, size=n),
    'bmi': np.random.normal(25, 5, size=n),
    'exercise_minutes': np.random.randint(0, 60, size=n),
    'diet_score': np.random.randint(1, 10, size=n),
    'hba1c': np.random.normal(7, 1, size=n)
})

X = data[['age', 'bmi', 'exercise_minutes', 'diet_score']]
y = data['hba1c']

model = LinearRegression()
model.fit(X, y)

# === Set up FastAPI app ===
app = FastAPI()

# Input data format
class PatientData(BaseModel):
    age: int
    bmi: float
    exercise_minutes: int
    diet_score: int

# POST endpoint to predict
@app.post("/predict-risk")
def predict_risk(patient: PatientData):
    input_data = np.array([[patient.age, patient.bmi, patient.exercise_minutes, patient.diet_score]])
    prediction = model.predict(input_data)[0]
    return {"predicted_hba1c": round(float(prediction), 2)}
