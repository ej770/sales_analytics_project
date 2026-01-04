import pandas as pd

def clean_sales_data(input_path="data/raw_sales.csv", output_path="data/cleaned_sales.csv"):

    df = pd.read_csv(input_path)

    df.columns = df.columns.str.lower().str.replace(" ", "_")

    if "sales" in df.columns:
        df["sales"] = pd.to_numeric(df["sales"], errors="coerce").fillna(0)
        df = df[df["sales"] > 0]  # Keep only positive sales

    if "year" in df.columns and "month" in df.columns:
        df["order_date"] = pd.to_datetime(df["year"].astype(str) + "-" + df["month"].astype(str) + "-01")

    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    clean_sales_data()
