from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title="🚀 FastAPI Heart Disease",
    description="Heart Disease Model in NTI",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "API WORKING"}


@app.post("/Parameters/")
async def get_parameters():
    pass
    # return parameters