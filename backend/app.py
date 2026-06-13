import sys
import os

# add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, request, jsonify, render_template
import pandas as pd

from inference.predict import predict_all
from drift.drift_detector import detect_drift
from decision_engine.decision_engine import make_decision

app = Flask(__name__, template_folder="../frontend/templates")

FEATURE_COLS = [
    "transaction_amount",
    "transaction_time",
    "customer_age",
    "account_balance",
    "device_trust_score",
    "location_risk",
    "is_international",
    "num_failed_logins"
]

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/upload_csv", methods=["POST"])
def upload_csv():
    file = request.files["file"]
    df = pd.read_csv(file)

    FEATURE_COLS = [
        "transaction_amount",
        "transaction_time",
        "customer_age",
        "account_balance",
        "device_trust_score",
        "location_risk",
        "is_international",
        "num_failed_logins"
    ]

    X = df[FEATURE_COLS].values

    predictions = predict_all(X)
    drift = detect_drift(X)
    decision = make_decision(drift)

    return jsonify({
        "predictions": predictions,
        "drift": drift,
        "decision": decision
    })


if __name__ == "__main__":
    app.run(debug=True)
