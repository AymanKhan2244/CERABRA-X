# decision_engine/decision_engine.py

def make_decision(drift_result):
    if drift_result["drift_detected"]:
        return {
            "decision": "ALERT_ADMIN",
            "message": "⚠️ Data drift detected. Monitoring required."
        }
    else:
        return {
            "decision": "CONTINUE",
            "message": "✅ System stable. No action needed."
        }

    
