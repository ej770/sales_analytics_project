import pandas as pd
import os

# === CONFIG ===
RAW_FILE = "data/cleaned_sales.csv"
OUTPUT_KPI = "outputs/kpi_summary.csv"

# Ensure output folder exists
os.makedirs("outputs", exist_ok=True)

# Load data
df = pd.read_csv(RAW_FILE)

# Use year, month, and retail_sales columns to calculate KPIs
kpis = df.groupby(["year", "month"])["retail_sales"].sum().reset_index()
kpis.rename(columns={"retail_sales": "Total_Retail_Sales"}, inplace=True)

# Save KPI summary
kpis.to_csv(OUTPUT_KPI, index=False)
print(f"KPI summary saved to {OUTPUT_KPI}")
