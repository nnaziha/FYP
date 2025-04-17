from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    message: str

@app.post("/chatbot")
def chatbot_response(user: UserInput):
    msg = user.message.lower()

    if "skip" in msg and "medication" in msg:
        return {"response": "Try not to skip medication. Set daily reminders and inform your doctor if you're having trouble."}
    elif "fried" in msg or "junk" in msg:
        return {"response": "Fried and junk food can raise your blood sugar. Choose grilled or steamed options and hydrate more."}
    elif "no exercise" in msg or "didn't exercise" in msg or "lazy" in msg:
        return {"response": "Try to get at least 20–30 minutes of light activity daily. Even walking helps!"}
    elif "stress" in msg or "anxious" in msg:
        return {"response": "Try relaxation exercises like deep breathing or a short walk. Stress can affect blood sugar too."}
    elif "missed meal" in msg or "skip meal" in msg or "didn't eat" in msg:
        return {"response": "Try to eat regular meals to keep your blood sugar stable."}
    elif "cake" in msg or "dessert" in msg or "sweets" in msg or "sugar" in msg:
        return {"response": "Too much sugar can spike your levels. Try fresh fruits or sugar-free snacks instead."}
    elif "sleep" in msg or "insomnia" in msg or "can't sleep" in msg:
        return {"response": "Poor sleep affects your health. Aim for 7–8 hours per night and unwind before bed."}
    elif "water" in msg or "dehydrated" in msg or "thirsty" in msg:
        return {"response": "Make sure to drink plenty of water throughout the day. Dehydration affects energy and sugar levels."}
    elif "tired" in msg or "fatigue" in msg or "low energy" in msg:
        return {"response": "Feeling tired? It could be your diet or stress. Try light movement and healthy snacks."}
    elif "ate healthy" in msg or "took medication" in msg or "exercised" in msg:
        return {"response": "Great job! You're building excellent habits. Keep it up!"}
    else:
        return {"response": "Thanks for sharing. Keep tracking your health and ask me anything!"}
