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
    return {"message": "API WORKING"}


@app.post("/predict")
async def predict(features: HeartFeatures):
    data = np.array([[features.size, features.bedrooms, features.age]])
    preprocessed = preprocessing(data)
    model = load_model()
    prediction = model.predict(preprocessed)
    return {"Predicted Price": prediction[0]}