import pickle
from pydantic import BaseModel

def load_model():
# Load the trained model
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

class HeartFeatures(BaseModel):
    size: float
    bedrooms: int
    age: int

def preprocessing(HeartFeatures:HeartFeatures):
    pass