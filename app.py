from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load model + columns
model = joblib.load("fraud_model.pkl")
model_columns = joblib.load("model_columns.pkl")


# 🔹 Feature engineering function (IMPORTANT)
def preprocess_input(data):
    df = pd.DataFrame([data])

    # Example features (must match training)
    df['amt_to_mean_card1'] = df['TransactionAmt'] / (df['TransactionAmt'] + 1)
    df['tx_count_card1'] = 1  # fallback (no history in API)

    # Fill missing columns
    for col in model_columns:
        if col not in df:
            df[col] = 0

    df = df[model_columns]

    return df


# 🔹 Prediction API
@app.post("/predict")
def predict(data: dict):
    df = preprocess_input(data)

    prob = model.predict_proba(df)[:, 1][0]
    prediction = int(prob > 0.5)

    return {
        "fraud_probability": float(prob),
        "is_fraud": prediction
    }