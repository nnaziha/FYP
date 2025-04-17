from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PatientProfile(BaseModel):
    age: int
    bmi: float
    hba1c: float

@app.post("/recommend-treatment")
def recommend(patient: PatientProfile):
    h = patient.hba1c
    b = patient.bmi

    if h > 8 and b > 30:
        plan = "Metformin + Low-Carb Diet + 45min/day exercise"
    elif h > 8 and b <= 30:
        plan = "Sulfonylurea + Moderate Diet + 30min/day exercise"
    elif 6.5 <= h <= 8:
        plan = "Lifestyle change only + 20min/day activity"
    else:
        plan = "Maintain routine + checkup every 3 months"

    return {
        "recommendation": plan
    }
