import pandas as pd
import matplotlib.pyplot as plt
import os

# === CONFIG ===
RAW_FILE = "data/cleaned_sales.csv"
OUTPUT_CHART = "outputs/charts/monthly_sales_trend.png"

# Ensure output folder exists
os.makedirs("outputs/charts", exist_ok=True)

# Load data
df = pd.read_csv(RAW_FILE)

# Create a period column for plotting: YYYY-MM
df["period"] = df["year"].astype(str) + "-" + df["month"].astype(str).str.zfill(2)

# Aggregate monthly retail_sales
monthly_sales = df.groupby("period")["retail_sales"].sum()

# Plot
plt.figure(figsize=(12,6))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Retail Sales Trend")
plt.xlabel("Month")
plt.ylabel("Retail Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_CHART)
print(f"Chart saved to {OUTPUT_CHART}")
