from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np

from model_training import compute_churn_probability


class CustomerFeatures(BaseModel):
    tenure: int
    monthly_charges: float
    contract: int
    support_calls: int

app = FastAPI(title="Customer Churn Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Customer Churn Prediction API is running"}


@app.post("/predict")
async def predict_churn(features: CustomerFeatures):
    proba = compute_churn_probability(
        tenure=features.tenure,
        monthly_charges=features.monthly_charges,
        contract=features.contract,
        support_calls=features.support_calls,
    )
    label = "High risk" if proba >= 0.5 else "Low risk"

    return {
        "churn_probability": float(proba),
        "churn_label": label,
    }
