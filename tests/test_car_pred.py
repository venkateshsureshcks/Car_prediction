import sys
import os

# Add project root to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from Prediction.Car_pred import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.get_json()

def test_predict():
    client = app.test_client()

    sample_data = {
        "year": 2015,
        "mileage": 18.5,
        "engine": 1200,
        "max_power": 80,
        "age": 5,
        "Diesel": 0,
        "Petrol": 1
    }

    response = client.post(
        "/predict",
        data=json.dumps(sample_data),
        content_type="application/json"
    )

    assert response.status_code == 200
    result = response.get_json()

    assert "Prediction" in result, "Key 'Prediction' missing in response"
    assert isinstance(result["Prediction"], float), "Prediction must be a float"