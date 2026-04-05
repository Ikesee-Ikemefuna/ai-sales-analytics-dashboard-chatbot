# 📊 AI-Powered Sales Analytics Pipeline & Chatbot

## 🚀 Overview

This project demonstrates an end-to-end data analytics workflow combining cloud data processing (AWS S3 & Athena), relational data modeling, business intelligence dashboards (Power BI), and an AI-powered chatbot for natural language querying.

It showcases how modern data tools can be integrated to transform raw data into actionable business insights.

---

## 🧱 Architecture

1. **Data Ingestion**

   * Multiple datasets (Sales, Returns, Shipping, Regional data)
   * Stored and managed in AWS S3

2. **Cloud Query Layer**

   * Data queried using SQL via AWS Athena
   * Enables scalable and serverless data analysis

3. **Data Transformation (ETL)**

   * Cleaned and transformed using Power Query and Python (Pandas)
   * Feature engineering:

     * Customer full name
     * Shipping duration
     * Date hierarchies (Year, Month, Day)
     * Sales classification

4. **Relational Data Modeling**

   * Integrated multiple datasets using keys such as `Order ID`
   * Enabled cross-table analysis across:

     * Sales transactions
     * Returns
     * Shipping modes
     * Regional performance

5. **Business Intelligence Layer**

   * Built interactive dashboards in Power BI
   * Key KPIs:

     * Total Sales
     * Total Profit
     * Total Orders
     * Profit by Product Category
     * Maximumum Days to Ship
     * Profit by Region
   * Visual insights:

     * Sales by region
     * Profit trends
     * Shipping performance
     * Returns analysis

6. **AI Query Layer**

   * Developed using Streamlit + LangChain + OpenAI
   * Enables natural language queries such as:

     * "What is total sales?"
     * "Which region has highest profit?"
     * "What is the total profit?"

---

## ☁️ Cloud Data Pipeline

This project simulates a cloud-based data workflow:

* Data stored in AWS S3
* Queried using SQL through AWS Athena
* Processed data used for BI and analytics
* Integrated into Power BI dashboards
* Connected to an AI chatbot for conversational querying

This reflects real-world modern data architecture used in industry.

---

## 🧠 Business Metrics

* **Total Sales** → sum of Sales
* **Total Profit** → sum of Profits
* **Total Orders** → total number of transactions (row count)
* **Distinct Orders** → unique Order IDs
* **Profit by Product Category** → sum of profit of categories of product
* **Maximumum Days to Ship** → Longest day it took to ship a product
* **Profit by Region** → Profit from each geographical location

---

## 🛠️ Tech Stack

**Programming & Data Processing**

* Python (Pandas)
* SQL

**Cloud & Data Pipeline**

* AWS S3
* AWS Athena

**Business Intelligence**

* Power BI
* Excel

**AI & Application Layer**

* Streamlit
* LangChain
* OpenAI API

**Data Sources**

* Excel / CSV

---

## 💡 Example Queries

* What is the total sales?
* What is the total profit?
* What is the total order?
* Which region has the highest sales?
* What is the maximum days to ship?
* What is the profit by product category?

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## 📸 Screenshots
*Screenshots of Natural Language Querying.
<img width="1572" height="809" alt="Total_Sales_Streamlit_Query" src="https://github.com/user-attachments/assets/c2c0876b-3d26-451f-bcfa-16b4cd6bdf58" />
<img width="1562" height="806" alt="Profit_by_Product_Category_Streamlit_Query" src="https://github.com/user-attachments/assets/7abfe5c2-dc09-4124-af06-87614fcaf6a2" />

*Screenshots of Data Visualizations.
<img width="1019" height="547" alt="Total_Sales_Total_Profit_Visuals" src="https://github.com/user-attachments/assets/dbe0d014-4aff-4155-8f79-4a66d45d0544" />
<img width="1029" height="566" alt="Profit_by_Product_Category_Visuals" src="https://github.com/user-attachments/assets/16a4a534-55b0-43c6-98b7-76753f58cec7" />
<img width="1019" height="564" alt="Total_profit_Total_Shipping_Visuals" src="https://github.com/user-attachments/assets/1cb3d983-2bac-411e-b399-282fe817080f" />










---

## 🎯 What This Project Demonstrates

* End-to-end data pipeline design
* Cloud-based data querying using SQL
* Relational data modeling
* Business intelligence dashboarding
* AI-powered data interaction
* Real-world analytics workflow

---

## 📌 Future Improvements

* Deploy chatbot on cloud (AWS / Azure)
* Connect directly to live database
* Add real-time data ingestion
* Enhance AI accuracy with structured query generation
