import pickle
import numpy as np
from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

app = FastAPI(
    title="Crop Recommendation API",
    description="Predicts the most suitable crop based on soil and climate parameters.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# ---------- Pydantic models (JSON API) ----------

class CropFeatures(BaseModel):
    N: float = Field(..., description="Ratio of Nitrogen content in soil", examples=[90])
    P: float = Field(..., description="Ratio of Phosphorous content in soil", examples=[42])
    K: float = Field(..., description="Ratio of Potassium content in soil", examples=[50])
    temperature: float = Field(..., description="Temperature in Celsius", examples=[20.8])
    humidity: float = Field(..., description="Relative humidity in %", examples=[80])
    ph: float = Field(..., description="pH value of the soil", examples=[6.0])
    rainfall: float = Field(..., description="Rainfall in mm", examples=[20])


class PredictionResponse(BaseModel):
    crop: str
    message: str


# ---------- Helpers ----------

def load_model():
    with open("checkpoints/pickle_model.pkl", "rb") as f:
        return pickle.load(f)


def run_prediction(N, P, K, temperature, humidity, ph, rainfall) -> str:
    model = load_model()
    x = np.array([N, P, K, temperature, humidity, ph, rainfall]).reshape(1, -1)
    return model.predict(x)[0]


# ---------- HTML routes (frontend) ----------

@app.get("/", response_class=HTMLResponse, tags=["Frontend"])
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/result", response_class=HTMLResponse, tags=["Frontend"])
def result(
    request: Request,
    N: float = Form(...),
    P: float = Form(...),
    K: float = Form(...),
    Temp: float = Form(...),
    Hum: float = Form(...),
    pH: float = Form(...),
    rain: float = Form(...),
):
    prediction = run_prediction(N, P, K, Temp, Hum, pH, rain)
    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={"prediction": prediction.upper()},
    )


# ---------- JSON API route ----------

@app.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
def predict(features: CropFeatures):
    prediction = run_prediction(
        features.N,
        features.P,
        features.K,
        features.temperature,
        features.humidity,
        features.ph,
        features.rainfall,
    )
    return PredictionResponse(
        crop=prediction.upper(),
        message=f"The recommended crop for the given conditions is {prediction.upper()}.",
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
