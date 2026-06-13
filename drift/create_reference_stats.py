import pandas as pd
import joblib

df = pd.read_csv("data/raw/cerebrax_fraud_dataset.csv")

stats = {}

for col in df.columns:
    if col != "fraud":
        stats[col] = {
            "mean": df[col].mean(),
            "std": df[col].std()
        }

joblib.dump(stats, "models/reference_stats.pkl")

print("✅ reference_stats.pkl created")
