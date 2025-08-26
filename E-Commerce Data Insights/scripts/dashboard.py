import streamlit as st
import pandas as pd
import plotly.express as px
import os

# -------------------------------
# Page Config & Custom CSS
# -------------------------------
st.set_page_config(
    page_title="E-Commerce Data Insights Dashboard",
    page_icon="📊",
    layout="wide",
)


# -------------------------------
# Title
# -------------------------------
st.title("E-Commerce Data Insights Dashboard")
st.markdown("Gain **actionable insights** into sales, users, and product performance.")

# -------------------------------
# Load Data
# -------------------------------
@st.cache_data
def load_data():
    BASE_DIR = r"H:/PRIVATE/Data Collections/DS Roadmap/Projects/E-Commerce Data Insights"
    products = pd.read_csv(os.path.join(BASE_DIR, "data/raw/products.csv"))
    users = pd.read_csv(os.path.join(BASE_DIR, "data/raw/users.csv"))
    orders = pd.read_csv(os.path.join(BASE_DIR, "data/raw/orders.csv"))
    reviews = pd.read_csv(os.path.join(BASE_DIR, "data/raw/reviews.csv"))
    return products, users, orders, reviews

products, users, orders, reviews = load_data()

# Merge product info
orders = orders.merge(products[['ProductID', 'Price', 'Category']], on='ProductID', how='left')
orders['TotalAmount'] = orders['Quantity'] * orders['Price']
orders['Hour'] = pd.to_datetime(orders['OrderDate']).dt.hour

# -------------------------------
# KPIs
# -------------------------------
col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Revenue", f"₹{orders['TotalAmount'].sum():,.0f}")
col2.metric("📦 Total Orders", f"{len(orders)}")
col3.metric("👥 Active Users", f"{orders['UserID'].nunique()}")
col4.metric("⭐ Avg. Rating", f"{reviews['ReviewRating'].mean():.2f}")

st.markdown("---")

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("🔍 Filters")
category_filter = st.sidebar.multiselect(
    "Select Categories",
    options=products['Category'].unique(),
    default=products['Category'].unique()
)
filtered_orders = orders[orders['Category'].isin(category_filter)]

# -------------------------------
# Top Selling Products
# -------------------------------
st.subheader("Top 10 Selling Products")
top_products = (
    filtered_orders.groupby("ProductID")['Quantity'].sum().reset_index()
    .merge(products[['ProductID','ProductName']], on='ProductID')
    .sort_values(by="Quantity", ascending=False)
    .head(10)
)

fig_top_products = px.bar(
    top_products,
    x="Quantity",
    y="ProductName",
    orientation="h",
    title="Top Selling Products",
    color="Quantity",
    color_continuous_scale=["#4CAF50", "#81C784"],
    template="plotly_white"
)
st.plotly_chart(fig_top_products, use_container_width=True)


col1, col2 = st.columns(2)
with col1:
    # -------------------------------
    # Revenue by Category
    # -------------------------------
    st.subheader("Revenue by Product Category")
    category_sales = filtered_orders.groupby("Category")['TotalAmount'].sum().reset_index()

    fig_category = px.pie(
        category_sales,
        names="Category",
        values="TotalAmount",
        hole=0.4,
        title="Revenue Distribution by Category",
        template="plotly_white"
    )
    st.plotly_chart(fig_category, use_container_width=True)
with col2:
    # -------------------------------
    # Sales by Hour
    # -------------------------------
    st.subheader("Sales by Hour of Day")
    hourly_sales = filtered_orders.groupby('Hour')['TotalAmount'].sum().reset_index()

    fig_hourly = px.line(
        hourly_sales,
        x="Hour",
        y="TotalAmount",
        markers=True,
        title="Sales Trend by Hour",
        template="plotly_white",
        line_shape="spline"
    )
    st.plotly_chart(fig_hourly, use_container_width=True)

# -------------------------------
# -------------------------------
# Create two columns side by side
# -------------------------------
col1, col2 = st.columns(2)

# -------------------------------
# Top Customers
# -------------------------------
with col1:
    st.subheader("Top 10 High-Value Customers")
    customer_value = (
        filtered_orders.groupby("UserID")['TotalAmount'].sum().reset_index()
        .merge(users[['UserID','Name']], on='UserID')
        .sort_values(by="TotalAmount", ascending=False)
        .head(10)
    )

    fig_customers = px.bar(
        customer_value,
        x="TotalAmount",
        y="Name",
        orientation="h",
        title="Top High-Value Customers",
        color="TotalAmount",
        color_continuous_scale="Greens",
        template="plotly_white"
    )
    st.plotly_chart(fig_customers, use_container_width=True)

# -------------------------------
# Top Rated Products
# -------------------------------
with col2:
    st.subheader("Top 10 Products by Rating")
    avg_ratings = (
        reviews.groupby("ProductID")['ReviewRating'].mean().reset_index()
        .merge(products[['ProductID','ProductName']], on='ProductID')
        .sort_values(by="ReviewRating", ascending=False)
        .head(10)
    )

    fig_ratings = px.bar(
        avg_ratings,
        x="ReviewRating",
        y="ProductName",
        orientation="h",
        title="Top Rated Products",
        color="ReviewRating",
        color_continuous_scale="Oranges",
        template="plotly_white"
    )
    st.plotly_chart(fig_ratings, use_container_width=True)

