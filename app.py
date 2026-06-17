import streamlit as st
import pandas as pd
import plotly.express as px
from ai_insights import ask_ai #AI Insights
from chatbot import data_chat  #AI ChatBot
from config import get_connection

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="AI Data Analyst Dashboard",
    layout="wide"
)

st.title("📊 AI Data Analyst Dashboard")
st.write("Powered by Snowflake + Python")

# -------------------------
# Connect to Snowflake
# -------------------------

conn = get_connection()

# -------------------------
# Load Data
# -------------------------

query = "SELECT * FROM SALES"

df = pd.read_sql(query, conn)

# -------------------------
# KPI Metrics
# -------------------------

total_sales = df["SALES_AMOUNT"].sum()

total_orders = len(df)

top_product = (
    df.groupby("PRODUCT")["SALES_AMOUNT"]
    .sum()
    .idxmax()
)

best_region = (
    df.groupby("REGION")["SALES_AMOUNT"]
    .sum()
    .idxmax()
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Sales", f"₹{total_sales:,.0f}")

with col2:
    st.metric("📦 Total Orders", total_orders)

with col3:
    st.metric("🏆 Top Product", top_product)

with col4:
    st.metric("🌍 Best Region", best_region)

# -------------------------
# Sales By Region Chart
# -------------------------

st.subheader("📈 Sales By Region")

region_sales = (
    df.groupby("REGION")["SALES_AMOUNT"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    region_sales,
    x="REGION",
    y="SALES_AMOUNT",
    title="Sales by Region"
)

st.plotly_chart(fig1, width="stretch")

# -------------------------
# Product Contribution Chart
# -------------------------

st.subheader("🥧 Product Contribution")

product_sales = (
    df.groupby("PRODUCT")["SALES_AMOUNT"]
    .sum()
    .reset_index()
)

fig2 = px.pie(
    product_sales,
    names="PRODUCT",
    values="SALES_AMOUNT",
    title="Product Contribution"
)

st.plotly_chart(fig2, width="stretch")

# -------------------------
# Data Table
# -------------------------

st.subheader("📋 Sales Data")

st.dataframe(df, width="stretch")





#AI code(teja 3rd or 4th phase)

st.header("🤖 AI Business Insights")

if st.button("Generate AI Insights"):

    sales_summary = df.to_string()

    prompt = f"""
    You are a Senior Data Analyst.

    Analyze the following sales data and provide:

    1. Total sales summary
    2. Best performing product
    3. Best performing region
    4. Business recommendations
    5. Growth opportunities

    Data:

    {sales_summary}
    """

    response = ask_ai(prompt)

    st.write(response)
    
    
# -------------------------
# AI Chatbot
# -------------------------

st.header("💬 Chat With Your Data")

user_question = st.text_input(
    "Ask a question about your sales data"
)

if st.button("Ask AI"):

    data_text = df.to_string()

    answer = data_chat(
        user_question,
        data_text
    )

    st.success(answer)
# -------------------------
# Close Connection
# -------------------------


conn.close()