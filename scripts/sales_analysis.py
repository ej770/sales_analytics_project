import pandas as pd
import matplotlib.pyplot as plt
import os

# === CONFIG ===
RAW_FILE = "data/cleaned_sales.csv"
OUTPUT_FOLDER = "outputs"
OUTPUT_CHARTS = os.path.join(OUTPUT_FOLDER, "charts")


SALES_COLUMN = "retail_sales"
YEAR_COLUMN = "year"
MONTH_COLUMN = "month"
PRODUCT_CODE_COLUMN = "item_code"
PRODUCT_DESC_COLUMN = "item_description"
REGION_COLUMN = "supplier"

# ------------------------------

# ------------------------------
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_CHARTS, exist_ok=True)

# ------------------------------
# Load data
# ------------------------------
df = pd.read_csv(RAW_FILE)

# ------------------------------
# 1. KPI: Total Retail Sales per Year/Month
# ------------------------------
kpis = df.groupby([YEAR_COLUMN, MONTH_COLUMN])[SALES_COLUMN].sum().reset_index()
kpis.rename(columns={SALES_COLUMN: "Total_Retail_Sales"}, inplace=True)
kpis.to_csv(os.path.join(OUTPUT_FOLDER, "kpi_summary.csv"), index=False)
print("KPI summary saved to kpi_summary.csv")

# Create period column for plotting
kpis["period"] = kpis[YEAR_COLUMN].astype(str) + "-" + kpis[MONTH_COLUMN].astype(str).str.zfill(2)

# Plot total retail sales trend
plt.figure(figsize=(12,6))
plt.plot(kpis["period"], kpis["Total_Retail_Sales"], marker="o")
plt.title("Monthly Retail Sales Trend")
plt.xlabel("Month")
plt.ylabel("Retail Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_CHARTS, "monthly_retail_sales_trend.png"))
plt.close()
print("Monthly retail sales trend chart saved")

# ------------------------------
# 2. Top-performing Products
# ------------------------------
top_products = df.groupby([PRODUCT_CODE_COLUMN, PRODUCT_DESC_COLUMN])[SALES_COLUMN].sum().reset_index()
top_products = top_products.sort_values(by=SALES_COLUMN, ascending=False).head(10)
top_products.to_csv(os.path.join(OUTPUT_FOLDER, "top_products.csv"), index=False)
print("Top 10 products saved to top_products.csv")

# Plot top products
plt.figure(figsize=(12,6))
plt.bar(top_products[PRODUCT_DESC_COLUMN], top_products[SALES_COLUMN])
plt.title("Top 10 Products by Retail Sales")
plt.xlabel("Product")
plt.ylabel("Retail Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_CHARTS, "top_products.png"))
plt.close()
print("Top products chart saved")

# ------------------------------
# 3. Regional Performance (using supplier)
# ------------------------------
regional_sales = df.groupby(REGION_COLUMN)[SALES_COLUMN].sum().reset_index()
regional_sales = regional_sales.sort_values(by=SALES_COLUMN, ascending=False)
regional_sales.to_csv(os.path.join(OUTPUT_FOLDER, "regional_sales.csv"), index=False)
print("Regional sales saved to regional_sales.csv")

# Plot regional sales
plt.figure(figsize=(12,6))
plt.bar(regional_sales[REGION_COLUMN], regional_sales[SALES_COLUMN])
plt.title("Retail Sales by Supplier")
plt.xlabel("Supplier")
plt.ylabel("Retail Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_CHARTS, "regional_sales.png"))
plt.close()
print("Regional sales chart saved")
