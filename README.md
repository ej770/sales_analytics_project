Sales Analytics Project
Overview
This project performs a dynamic analysis of retail sales data, generating insights into:
•	Monthly retail sales trends

•	Top-performing products

•	Regional (supplier) performance
The project is built in Python using pandas and matplotlib. It produces both CSV outputs and visual charts for reporting and dashboards. The analysis is dynamic, so it works with any dataset containing the same core columns.
________________________________________
Project Structure
sales_analytics_project/
├─ data/
│  └─ cleaned_sales.csv          # Raw dataset
├─ scripts/
│  └─ sales_analysis.py          # Analysis script
├─ outputs/
│  ├─ kpi_summary.csv            # Monthly retail sales summary
│  ├─ top_products.csv           # Top 10 products by retail_sales
│  ├─ regional_sales.csv         # Retail sales by supplier
│  └─ charts/
│     ├─ monthly_retail_sales_trend.png
│     ├─ top_products.png
│     └─ regional_sales.png
└─ README.md
________________________________________
Dataset Columns
Column	Description
year	Year of sale
month	Month of sale
supplier	Supplier or region
item_code	Product identifier
item_description	Product name/description
item_type	Product type/category
retail_sales	Sales value (used for all calculations)
retail_transfers	Transfers between locations (optional)
warehouse_sales	Warehouse sales (optional)
order_date	Original order date (not required here)
Note: retail_sales is the primary column used for analysis.
________________________________________
How to Run
1.	Clone the repository:
git clone https://github.com/yourusername/sales_analytics_project.git
cd sales_analytics_project
2.	Install required packages:
pip install pandas matplotlib
3.	Run the analysis script from the project root:
python scripts\sales_analysis.py
4.	Outputs will be generated in outputs/ and outputs/charts/:
•	kpi_summary.csv → monthly retail sales totals

•	top_products.csv → top 10 products by retail_sales

•	regional_sales.csv → supplier performance

•	Charts:
o	monthly_retail_sales_trend.png

o	top_products.png

o	regional_sales.png
________________________________________
Dynamic Analysis Highlights
The project performs a fully dynamic analysis:
1.	Monthly Retail Sales Trend
o	Aggregates retail_sales by year and month.


o	Generates a trend chart showing fluctuations over time.
2.	Top-Performing Products
o	Identifies the top 10 products by retail_sales.


o	Produces a bar chart for visualization.
3.	Regional Performance
o	Aggregates retail_sales by supplier.


Visualizations
You can embed charts directly in your README to showcase results:
Monthly Retail Sales Trend
Top Products
Regional Sales
________________________________________
GitHub Tips
•	Exclude cleaned_sales.csv if it contains sensitive data.

•	Include generated charts in outputs/charts/ for visual presentation.

•	Use the CSVs to create dashboards in Excel, Power BI, or Tableau.
________________________________________
License
This project is for educational and portfolio purposes. You may reuse the code with attribution.
