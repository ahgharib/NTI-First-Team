import joblib
from pydantic import BaseModel
import pandas as pd

def load_model():
    model = joblib.load("logistic_regression_model.joblib")
    return model



class HeartFeatures(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int



def preprocessing(features: HeartFeatures):

    data_dict = features.dict()
    
    # Create a single-row DataFrame
    df = pd.DataFrame([data_dict])

    return df


 
# # Example input
# input_data = HeartFeatures(
#     age=63, sex=1, cp=3, trestbps=145, chol=233,
#     fbs=1, restecg=0, thalach=150, exang=0,
#     oldpeak=2.3, slope=0, ca=0, thal=1
# )

# # Preprocess
# X = preprocessing(input_data)

# # Load model
# model = load_model()

# # Make prediction
# prediction = model.predict(X)
# probability = model.predict_proba(X)

# print("Prediction:", prediction[0])
# print("Probability:", probability[0])
