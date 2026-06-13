import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

reference_stats = joblib.load(
    os.path.join(BASE_DIR, "models", "reference_stats.pkl")
)

def detect_drift(new_data, threshold=0.2):
    """
    Detect drift by comparing current feature means
    against reference feature means.

    Args:
        new_data (numpy.ndarray): New incoming data.
        threshold (float): Percentage change threshold.

    Returns:
        dict: Drift report.
    """

    drift_detected = False
    report = {}

    for i, feature in enumerate(reference_stats.keys()):

        ref_mean = float(reference_stats[feature]["mean"])
        new_mean = float(np.mean(new_data[:, i]))

        # Prevent division by zero and instability
        denominator = max(abs(ref_mean), 1.0)

        change = abs(new_mean - ref_mean) / denominator

        status = "DRIFT" if change > threshold else "STABLE"

        if status == "DRIFT":
            drift_detected = True

        report[feature] = {
            "reference_mean": round(ref_mean, 2),
            "new_mean": round(new_mean, 2),
            "percent_change": round(change * 100, 2),
            "status": status
        }

    return {
        "drift_detected": drift_detected,
        "threshold": threshold,
        "details": report
    }