# 🧠 CEREBRA-X: Intelligent Fraud Detection & Data Drift Monitoring Platform

## Overview

CEREBRA-X is an end-to-end Machine Learning platform designed to detect fraudulent financial transactions while continuously monitoring incoming data for distribution shifts (data drift).

The platform combines multiple machine learning models with a real-time drift detection engine and decision intelligence layer to improve prediction reliability and model trustworthiness in production environments.

---

## Key Features

### Fraud Detection Engine

* Logistic Regression
* Decision Tree Classifier
* XGBoost Classifier
* Ensemble-style multi-model prediction framework

### Data Drift Monitoring

* Reference statistics generation
* Incoming data monitoring
* Feature-level drift detection
* Automated drift reporting

### Decision Intelligence Layer

* Aggregates model predictions
* Provides interpretable fraud risk assessments
* Supports operational decision-making

### Dashboard Interface

* Interactive web interface
* Prediction visualization
* Drift monitoring dashboard
* Model performance insights

---

## System Architecture

```text
                    ┌───────────────────┐
                    │ Incoming Data     │
                    └─────────┬─────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │ Data Preprocessing   │
                  └─────────┬────────────┘
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ Logistic Reg.  │ │ Decision Tree  │ │ XGBoost Model  │
└────────────────┘ └────────────────┘ └────────────────┘
          │                 │                 │
          └─────────┬───────┴───────┬─────────┘
                    ▼               ▼
             ┌────────────────────────┐
             │ Decision Engine        │
             └────────────┬───────────┘
                          ▼
             ┌────────────────────────┐
             │ Fraud Assessment       │
             └────────────────────────┘

                          │

                          ▼

             ┌────────────────────────┐
             │ Drift Detection Module │
             └────────────────────────┘
```

---

## Project Structure

```text
CEREBRA-X/
│
├── backend/
│   └── app.py
│
├── inference/
│   └── predict.py
│
├── decision_engine/
│   └── decision_engine.py
│
├── drift/
│   ├── drift_detector.py
│   └── create_reference_stats.py
│
├── frontend/
│   └── templates/
│       └── dashboard.html
│
├── models/
│   ├── Logistic Regression Model
│   ├── Decision Tree Model
│   ├── XGBoost Model
│   └── reference_stats.pkl
│
└── README.md
```

---

## Dataset Features

The fraud detection models are trained using the following transaction-level features:

| Feature            | Description                     |
| ------------------ | ------------------------------- |
| transaction_amount | Transaction value               |
| transaction_time   | Time of transaction             |
| customer_age       | Customer age                    |
| account_balance    | Customer account balance        |
| device_trust_score | Device trustworthiness score    |
| location_risk      | Geographical risk score         |
| is_international   | International transaction flag  |
| num_failed_logins  | Number of failed login attempts |

---

## Data Drift Detection

CEREBRA-X continuously compares incoming production data against reference statistics generated during model training.

The system evaluates:

* Feature mean shifts
* Relative distribution changes
* Drift thresholds
* Feature-level monitoring reports

Example Output:

```json
{
  "drift_detected": true,
  "details": {
    "transaction_amount": {
      "status": "DRIFT",
      "change": 0.34
    }
  }
}
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/CEREBRA-X.git

cd CEREBRA-X
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the backend server:

```bash
python backend/app.py
```

Open the dashboard:

```text
http://localhost:5000
```

---

## Technology Stack

### Machine Learning

* Scikit-Learn
* XGBoost
* NumPy
* Pandas

### Backend

* Flask

### Frontend

* HTML
* CSS
* JavaScript

### Monitoring

* Custom Drift Detection Engine

---

## Future Enhancements

* Population Stability Index (PSI)
* Evidently AI Integration
* Model Versioning
* MLflow Experiment Tracking
* Docker Containerization
* Cloud Deployment (AWS/Azure)
* Real-time Streaming Inference
* Automated Retraining Pipelines

---

## Learning Outcomes

This project demonstrates:

* Machine Learning Model Deployment
* Multi-Model Prediction Systems
* Data Drift Detection
* Model Monitoring
* Production-Oriented ML Architecture
* End-to-End ML Engineering Practices

---

## Author

Ayman Khan

AI Engineer | Machine Learning Engineer

Focused on building intelligent systems, multimodal AI applications, retrieval-augmented generation (RAG), and production-ready machine learning solutions.
