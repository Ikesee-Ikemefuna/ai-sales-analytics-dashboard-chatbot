import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import streamlit as st
from langchain_openai import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent

# -----------------------------
# PAGE SETUP
# -----------------------------
st.set_page_config(page_title="AI-Powered Sales Analytics Chatbot", page_icon="📊")
st.title("📊 AI-Powered Sales Analytics Chatbot")
st.markdown("Ask questions about sales, profit, orders, region performance, returns, and shipping.")

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("sales_transaction_final.csv", encoding="latin1")
df.columns = df.columns.str.strip()

# -----------------------------
# CLEAN DATA
# -----------------------------
numeric_cols = [
    "Sales",
    "Profit",
    "Order Quantity",
    "Discount",
    "Unit Price",
    "Shipping Cost",
    "Product Base Margin",
    "10% Discount",
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

date_cols = ["Order Date", "Main_Ship_Date", "Ship_Date", "Main_Birthdate"]

for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce", dayfirst=True)

if "Order Date" in df.columns and "Main_Ship_Date" in df.columns:
    df["Days_to_Ship"] = (df["Main_Ship_Date"] - df["Order Date"]).dt.days

# -----------------------------
# OPTIONAL DATA PREVIEW
# -----------------------------
with st.expander("Preview dataset"):
    st.write("Row count:", len(df))
    if "Order ID" in df.columns:
        st.write("Distinct Order IDs:", df["Order ID"].nunique())
    st.dataframe(df.head())

# -----------------------------
# SAFE BUSINESS LOGIC
# -----------------------------
def handle_query(query: str):
    q = query.lower().strip()

    # SALES / PROFIT
    if "total sales" in q:
        return f"Total sales: {df['Sales'].sum():,.2f}"

    if "total profit" in q:
        return f"Total profit: {df['Profit'].sum():,.2f}"

    if "total loss" in q or "overall loss" in q:
        if "Profit" in df.columns:
            total_loss = df.loc[df["Profit"] < 0, "Profit"].sum()
            return f"Total loss: {abs(total_loss):,.2f}"
        return "Profit column is not available."

    if "total positive profit" in q or "gross profit" in q:
        if "Profit" in df.columns:
            total_positive_profit = df.loc[df["Profit"] > 0, "Profit"].sum()
            return f"Total positive profit: {total_positive_profit:,.2f}"
        return "Profit column is not available."

    # ORDERS
    if (
        "total order" in q
        or "total orders" in q
        or "number of orders" in q
        or "how many orders" in q
    ):
        return f"Total orders: {len(df):,}"

    if "distinct orders" in q or "unique orders" in q:
        if "Order ID" in df.columns:
            return f"Distinct orders: {df['Order ID'].nunique():,}"
        return "Order ID column is not available."

    if "total order quantity" in q or "sum of order quantity" in q:
        if "Order Quantity" in df.columns:
            return f"Total order quantity: {df['Order Quantity'].sum():,.0f}"
        return "Order Quantity column is not available."

    # REGION
    if "highest sales region" in q or "which region has highest sales" in q:
        if "Region" in df.columns:
            s = df.groupby("Region", dropna=False)["Sales"].sum().sort_values(ascending=False)
            return f"{s.index[0]} has the highest sales: {s.iloc[0]:,.2f}"
        return "Region column is not available."

    if "highest profit region" in q or "which region has highest profit" in q:
        if "Region" in df.columns:
            s = df.groupby("Region", dropna=False)["Profit"].sum().sort_values(ascending=False)
            return f"{s.index[0]} has the highest profit: {s.iloc[0]:,.2f}"
        return "Region column is not available."

    # CATEGORY / PRODUCT
    if "highest sales category" in q or "which category has highest sales" in q:
        if "Product Category" in df.columns:
            s = df.groupby("Product Category", dropna=False)["Sales"].sum().sort_values(ascending=False)
            return f"{s.index[0]} has the highest sales: {s.iloc[0]:,.2f}"
        return "Product Category column is not available."

    if "highest profit category" in q or "which category has highest profit" in q:
        if "Product Category" in df.columns:
            s = df.groupby("Product Category", dropna=False)["Profit"].sum().sort_values(ascending=False)
            return f"{s.index[0]} has the highest profit: {s.iloc[0]:,.2f}"
        return "Product Category column is not available."

    # SHIPPING
    if "maximum days to ship" in q or "max days to ship" in q:
        if "Days_to_Ship" in df.columns:
            max_days = df["Days_to_Ship"].dropna().max()
            return f"Maximum days to ship: {int(max_days)} days"
        return "Days_to_Ship is not available in this dataset."

    if "average days to ship" in q:
        if "Days_to_Ship" in df.columns:
            avg_days = df["Days_to_Ship"].dropna().mean()
            return f"Average days to ship: {avg_days:.2f} days"
        return "Days_to_Ship is not available in this dataset."

    if "most used ship mode" in q or "most common ship mode" in q:
        if "Ship Mode" in df.columns:
            s = df["Ship Mode"].dropna().value_counts()
            return f"The most used ship mode is {s.index[0]} with {s.iloc[0]:,} orders."
        return "Ship Mode column is not available."

    if "which ship mode has highest sales" in q or "ship mode has highest sales" in q:
        if "Ship Mode" in df.columns:
            s = df.groupby("Ship Mode", dropna=False)["Sales"].sum().sort_values(ascending=False)
            return f"{s.index[0]} has the highest total sales among ship modes: {s.iloc[0]:,.2f}"
        return "Ship Mode column is not available."

    # RETURNS
    if "total returned orders" in q or "how many returned items" in q or "returned items" in q:
        if "Main_Order_Status" in df.columns:
            returned = df["Main_Order_Status"].astype(str).str.lower().str.contains("returned", na=False).sum()
            return f"Total returned orders: {returned:,}"
        return "Return status column is not available."

    return None

# -----------------------------
# AI FALLBACK
# -----------------------------
llm = OpenAI(temperature=0)

agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=False,
    allow_dangerous_code=True,
    max_iterations=6,
    prefix="""
You are a professional business data analyst.
Use the dataset exactly as provided.
Do not guess.

Business definitions:
- total orders = number of rows / transactions
- distinct orders = count of unique Order ID
- total order quantity = sum of Order Quantity
- total sales = sum of Sales
- total profit = sum of Profit

Answer clearly and briefly.
""",
)

# -----------------------------
# USER INPUT
# -----------------------------
query = st.text_input("Ask a question about the sales data:")

if query:
    with st.spinner("Analyzing data..."):
        result = handle_query(query)

        if result:
            st.success(result)
        else:
            try:
                response = agent.invoke({"input": query})
                st.info(response["output"])
            except Exception:
                st.error("AI could not answer this question reliably.")