
# E-Commerce Data Insights Dashboard

  Gain comprehensive, actionable insights into your e-commerce platform’s sales, user behavior, product performance, and review ratings. This project uses a robust data analysis workflow to power an interactive Streamlit dashboard and data visualizations.

## Project Overview


This project involves end-to-end data exploration, cleaning, analysis, and visualization of an e-commerce dataset containing information about users, products, orders, and reviews. It culminates in an interactive Streamlit dashboard that presents:

- Sales trends and patterns
- Product category performance
- Customer purchase behavior
- Ratings and reviews insights

## 📂 Project Structure
``` bash
E-Commerce-Data-Insights/
│
├── data/
│   ├── raw/
│   │   ├── products.csv
│   │   ├── users.csv
│   │   ├── orders.csv
│   │   └── reviews.csv
│   └── cleaned_orders.csv (generated)
│
├── E_Commerce_Data_Insights.ipynb # Data cleaning and EDA in Jupyter Notebook
│
├── scripts/
│   ├── dashboard.py
│   ├── .streamlit/
│       ├── config.toml  # Custom theming for Streamlit app
│
├── requirements.txt # Python dependencies
├── README.md # Project overview and documentation
├── output_images/ # Visualizations from analysis
└── dashboard_images/ # Screenshots of the Streamlit dashboard
```

## Features

- **Clean & Explore Raw Data:** Preprocessing, merging, and basic statistics.

- **Sales Analysis:**
  -  Top-selling products and their quantities

  - Revenue breakdown by product category

  - Identifying peak hours of sales activity

- **User Insights:**
  - Repeat purchase rate calculation

  - High-value customer ranking

  - Most highly rated products
- **Review Analysis:** Aggregate and visualize customer review ratings.

- **Interactive Dashboard:** Filter, drill down, and visualize KPIs using Streamlit and Plotly.

- **Custom Theming:** Visually appealing layout and color scheme via config.toml.

## 1. Data Exploration & Cleaning

- Handled missing values and duplicates.
- Merged product price into order details.
- Calculated `TotalAmount = Quantity × Price`.
- Converted datetime columns to proper `datetime` formats.
- Created derived features like `Hour` of sale.

The cleaned dataset is saved as cleaned_orders.csv for further analysis and dashboard integration.

## 2. Exploratory Data Analysis (EDA)

Key analyses and visualizations include:

- Top 10 Best-Selling Products: Horizontal bar chart.

- Revenue Distribution by Category: Pie chart.

- Hourly Sales Trend: Line chart.

- Repeat Customer Rate: Percentage of users with >1 purchase.

- Top High-Value Customers: Bar chart by total spend.

- Product Review Ratings: Top 10 products by customer rating.

### Sample Output Visualizations
Here are a few visualizations from the analysis:

![Top Products](https://github.com/Hariharan-T27/shopper-insights/blob/main/E-Commerce%20Data%20Insights/output%20images/Top%20Products.png?raw=true)
![Category Sales](https://github.com/Hariharan-T27/shopper-insights/blob/main/E-Commerce%20Data%20Insights/output%20images/Pie%20Chart.png)
![Hourly Sales](output_images/hourly_sales.png)
![Top Customers](output_images/top_customers.png)
![Top Ratings](output_images/top_ratings.png)

## 3. Interactive Dashboard (script.py)

Built with **Streamlit** and Plotly for instant interactivity.

**KPIs:** Revenue, orders, unique users, average product rating.

**Filters:** Segment analyses by product category.

**Visualizations:** All EDA insights available interactively.

**Dark & Light Mode:** Based on theme settings in config.toml.

### Dashboard Preview

Check out the interactive Streamlit dashboard:

![Dashboard KPIs](dashboard_images/dashboard_kpis.png)
![Dashboard Trends](dashboard_images/dashboard_trends.png)
![Dashboard Customers](dashboard_images/dashboard_customers.png)

##  4. Dashboard Customization (config.toml)
Change the app's appearance (colors, font) using this config file. Example settings:
```bash
[theme]
primaryColor = "#D2691E"
backgroundColor = "#FFF8DC"
secondaryBackgroundColor = "#F5DEB3"
textColor = "#2C3E50"
font = "sans serif"
```

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/Hariharan-T27/shopper-insights.git
cd E-Commerce_Data_Insights
```

### 2. Install Dependencies
Install required libraries:
```bash
pip install -r requirements.txt
```
### 3. Add your data files to data/raw/.
### 4. (Optional) Review/Run notebook.ipynb for full EDA or to regenerate charts.

### 5. Launch the Streamlit dashboard:
```bash
streamlit run dashboard.py
```
### 6. Visit the app at the local URL provided after launch.

## Tech Stack
- **Python** (Pandas, NumPy)

- **Matplotlib & Seaborn** – static visualizations

- **Plotly Express** – interactive charts

- **Streamlit** – interactive dashboard

- **Jupyter Notebook** – data exploration

### requirements.txt:
```bash
Python 3.7+

pandas

numpy

plotly

seaborn

matplotlib

streamlit
```
## Future Improvements
- Add time-based filtering (e.g., by month/year).

- Integrate machine learning to predict sales or churn.

- Enable user login for personalized insights.

## Example Use Cases
- Sales optimization for e-commerce managers

- Marketing campaign analysis

- Product management and QA

- Reporting and executive dashboards

## Contact

For questions or collaboration:

**Name:** Hariharan Thirunagari

**Email:** thariharan76@gmail.com

**GitHub:** https://github.com/Hariharan-T27
