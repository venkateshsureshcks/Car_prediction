from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load model and scalers
with open("Car_predict.pkl", "rb") as f:
    clf = pickle.load(f)

with open("feature_scaler.pkl", "rb") as f:
    feature_scaler = pickle.load(f)

with open("target_scaler.pkl", "rb") as f:
    target_scaler = pickle.load(f)

@app.route("/")
def home():
    return {"message": "Hi, Welcome to Car prediction!"}

@app.route("/predict", methods=["POST"])
def Predict():
    loan_req = request.get_json()

    year = float(loan_req.get("year", 0))
    mileage = float(loan_req.get("mileage", 0))
    engine = float(loan_req.get("engine", 0))
    max_power = float(loan_req.get("max_power", 0))
    Car_age = int(loan_req.get("age", 0))
    Diesel = 1 if loan_req.get("Diesel", 0) == 1 else 0
    Petrol = 1 if loan_req.get("Petrol", 0) == 1 else 0

    input_df = pd.DataFrame([{
        "year": year,
        "mileage": mileage,
        "engine": engine,
        "max_power": max_power,
        "age": Car_age,
        "Diesel": Diesel,
        "Petrol": Petrol
    }])

    # Scale input
    input_scaled = feature_scaler.transform(input_df)

    # Predict (scaled output)
    scaled_pred = clf.predict(input_scaled).reshape(-1, 1)

    # Inverse transform prediction
    final_pred = target_scaler.inverse_transform(scaled_pred)

    return jsonify({"Prediction": float(final_pred[0][0])})
