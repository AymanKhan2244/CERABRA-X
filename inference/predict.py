import joblib
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dt = joblib.load(os.path.join(BASE_DIR, "models", "dt_joblib (1)"))
xgb = joblib.load(os.path.join(BASE_DIR, "models", "xgb_joblib"))
lr = joblib.load(os.path.join(BASE_DIR, "models", "lr_joblib (1)"))

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

def predict_all(X):

    # Convert numpy array to DataFrame if needed
    if not isinstance(X, pd.DataFrame):
        X = pd.DataFrame(X, columns=FEATURE_COLS)

    return {
        "DecisionTree": dt.predict(X).tolist(),
        "XGBoost": xgb.predict(X).tolist(),
        "LogisticRegression": lr.predict(X).tolist()
    }