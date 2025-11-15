from fastapi import FastAPI
import uvicorn
from utility import HeartFeatures, load_model, preprocessing
import numpy as np


app = FastAPI(
    title="🚀 FastAPI Heart Disease",
    description="Heart Disease Model in NTI",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "One end point for heart disease model"}


@app.post("/predict")
async def predict(features: HeartFeatures):
    # Preprocess: convert to dataframe
    df = preprocessing(features)

    # Load model
    model = load_model()

    # Predict
    prediction = model.predict(df)

    return {"prediction": int(prediction[0])}