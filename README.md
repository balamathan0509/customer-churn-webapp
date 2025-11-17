# Customer Churn Prediction Web App

A simple end-to-end data science project that exposes a customer churn prediction model through a FastAPI backend and a minimal HTML/CSS/JS frontend.

## Tech Stack

- Python, FastAPI, Uvicorn
- scikit-learn, pandas, numpy
- HTML, CSS, JavaScript (no framework)

## How It Works

1. `backend/model_training.py` creates synthetic customer data and trains a logistic regression model to predict churn.
2. The trained model is saved as `model.pkl`.
3. `backend/main.py` loads the model and exposes a `/predict` endpoint.
4. The frontend form collects customer details and calls the API to display churn risk.

## Basic Run Instructions

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Train the model:

   ```bash
   cd backend
   python model_training.py
   ```

4. Start the API server:

   ```bash
   uvicorn main:app --reload
   ```

5. Open `frontend/index.html` in your browser (or with a simple static server) and submit the form to see predictions.
