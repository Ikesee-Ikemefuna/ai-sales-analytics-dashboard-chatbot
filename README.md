# 📊 AI-Powered Sales Analytics Pipeline & Chatbot

## 🚀 Live Demo

🔗 **[Open App](https://ai-sales-analytics-dashboard-chatbot-cavzpbqyp6sdvmrtng8tci.streamlit.app/)**

## 🚀 Overview

## 🚀 Overview

This project demonstrates an end-to-end data analytics workflow combining cloud data processing (AWS S3 & Athena), relational data modeling, business intelligence dashboards (Power BI), and an AI-powered chatbot for natural language querying.

It showcases how modern data tools can be integrated to transform raw data into actionable business insights.

**Note:** The app uses an exported final analytical table derived from the relational Power BI/Athena workflow.

---

## 🧱 Architecture

1. **Data Ingestion**

   * Multiple datasets (Sales, Returns, Shipping, Regional data)
   * Stored and managed in AWS S3

2. **Cloud Query Layer**

   * Data queried using SQL via AWS Athena
   * Enables scalable and serverless data analysis
     
## 📊 Key Insights Delivered

This project generates business-critical insights from sales data through both dashboards and AI-powered querying:

- **Total Sales:** ~$14.9M across all transactions  
- **Total Profit:** ~$1,52. Aggregated net profit from all orders  
- **Total Orders:** ~8.3K orders processed  
- **Profit by Product Category:** Identifies highest and lowest performing categories  
- **Profit by Region:** Highlights top-performing geographical regions  
- **Maximum Days to Ship:** 92 days. Detects delivery delays and shipping inefficiencies  

These insights are accessible through:
- 📊 Power BI dashboards (visual analytics)
- 🤖 AI chatbot (natural language queries)

These insights support data-driven decision-making in areas such as sales optimization, logistics efficiency, and regional performance analysis.

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
     * Maximum Days to Ship
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
* What is the category with the highest sales and how much?

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py

### 🔐 Set your OpenAI API Key

Before running the app, you must set your OpenAI API key as an environment variable.

#### Windows (PowerShell)
```bash
$env:OPENAI_API_KEY="your_api_key_here"

#### Mac/Linux
export OPENAI_API_KEY="your_api_key_here"
```

---

## 📸 Screenshots
*Screenshots of Natural Language Querying.
<img width="1553" height="815" alt="Total_Sales_Query" src="https://github.com/user-attachments/assets/9f02158d-155d-44ef-bb06-1b6d15ed8115" />
<img width="1588" height="816" alt="Profit_by_Category_Query" src="https://github.com/user-attachments/assets/d80b9e74-78fa-4ca3-8257-e95d44ec8709" />

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
* AI-powered interaction with business data
* Real-world analytics workflow and business business insights

## 🔗 Links
* Live App: https://your-app-link.streamlit.app
* GitHub Repo: https://github.com/Ikesee-Ikemefuna/ai-sales-analytics-dashboard-chatbot

---

## 📌 Future Improvements

    Deploy chatbot on cloud (AWS / Azure)
    Connect directly to live database
    Add real-time data ingestion
    Enhance AI accuracy with structured query generation

