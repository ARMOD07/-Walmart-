# backend_api/app.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="backend_api/static"), name="static")

model = joblib.load("sales_model.pkl")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou spécifie "http://localhost:5500" par exemple
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class SalesInput(BaseModel):
    Store: int
    Dept: int
    Temperature: float
    Fuel_Price: float
    CPI: float
    Unemployment: float
    IsHoliday: bool
    Date: str

def preprocess_input(data: SalesInput):
    df = pd.DataFrame([data.model_dump()])  # Utilise model_dump() pour Pydantic v2
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['Week'] = df['Date'].dt.isocalendar().week
    df['Holiday_Flag'] = df['IsHoliday'].astype(int)
    df.drop(columns=['Date', 'Dept', 'IsHoliday'], inplace=True)
    return df

@app.get("/")
def root():
    return {"message": "Bienvenue dans l'API Walmart Sales Predictor!"}

@app.post("/predict")
def predict(data: SalesInput):
    try:
        processed = preprocess_input(data)
        print(f"Processed input data: {processed}")

        # Si nécessaire
        prediction = model.predict(processed.values)

        predicted_sales = round(float(prediction[0]), 2)
        response = {"Weekly_Sales_Predicted": predicted_sales}
        print(f"Response being sent: {response}")
        return response

    except Exception as e:
        print(f"Prediction error: {str(e)}")  # <-- Affiche l’erreur
        return {"error": str(e)}


