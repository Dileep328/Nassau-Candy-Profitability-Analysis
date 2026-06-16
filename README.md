# 🍫 Nassau Candy Distributor - Product Line Profitability & Margin Performance Analysis

## 📌 Project Overview

This project analyzes product profitability, gross margins, division performance, cost efficiency, and profit concentration for Nassau Candy Distributor.

The goal is to identify:

- High-profit products
- High-margin products
- Underperforming divisions
- Cost-heavy products
- Margin-risk products
- Revenue and profit concentration risks

The project was developed using Python, Pandas, Plotly, and Streamlit.

---

## 🎯 Business Problem

Sales volume alone does not determine business success.

Some products:

- Generate high revenue but low profit
- Consume excessive manufacturing cost
- Create margin pressure
- Reduce overall profitability

The organization requires a data-driven framework to identify:

- Which products drive profit
- Which divisions are financially efficient
- Where pricing improvements are needed
- Which products require review or discontinuation

---

## 📊 Dataset Information

Dataset contains:

| Feature | Description |
|----------|-------------|
| Order ID | Unique Order Identifier |
| Order Date | Order Placement Date |
| Ship Date | Shipment Date |
| Division | Product Division |
| Product Name | Product Name |
| Sales | Revenue Generated |
| Units | Quantity Sold |
| Cost | Manufacturing Cost |
| Gross Profit | Sales - Cost |
| Region | Customer Region |
| State | Customer State |

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Matplotlib
- Seaborn

---

## 📈 Key Performance Indicators (KPIs)

### Financial KPIs

- Total Revenue
- Total Profit
- Gross Margin %
- Profit Per Unit

### Product KPIs

- Revenue Contribution %
- Profit Contribution %
- Margin Ranking

### Division KPIs

- Division Revenue
- Division Profit
- Division Margin %

### Risk KPIs

- Margin Risk Products
- Cost Heavy Products
- Dependency Risk %

---

## 📂 Project Structure

```text
Nassau_Candy_Project/
│
├── data/
│   └── Nassau Candy Distributor.csv
│
├── pages/
│   ├── 1_Product_Profitability.py
│   ├── 2_Division_Performance.py
│   ├── 3_Cost_Diagnostics.py
│   ├── 4_Pareto_Analysis.py
│   └── 5_Factory_Analysis.py
│
├── app.py
├── utils.py
├── requirements.txt
├── README.md
└── notebooks/
    └── EDA.ipynb
```

---

## 📊 Dashboard Modules

### 1. Executive Overview

Provides:

- Revenue Overview
- Profit Overview
- Gross Margin %
- Units Sold
- Revenue Trend
- Profit Trend

---

### 2. Product Profitability Dashboard

Provides:

- Top Profit Products
- Top Margin Products
- Product Leaderboard
- Revenue vs Profit Analysis
- Profit Contribution Analysis

---

### 3. Division Performance Dashboard

Provides:

- Revenue by Division
- Profit by Division
- Margin Comparison
- Revenue Share
- Profit Share

---

### 4. Cost Diagnostics Dashboard

Provides:

- Cost vs Sales Analysis
- Cost vs Margin Analysis
- Margin Risk Detection
- Cost Heavy Product Detection
- Product Recommendation Engine

Recommendations:

- Star Product
- Healthy Product
- Reprice Product
- Review Product

---

### 5. Pareto Analysis Dashboard

Provides:

- Revenue Pareto Analysis
- Profit Pareto Analysis
- Dependency Risk Analysis
- Top Revenue Drivers
- Top Profit Drivers

Uses the 80/20 Pareto Principle.

---

### 6. Factory Analysis Dashboard

Provides:

- Factory Revenue
- Factory Profit
- Factory Margin
- Factory Product Distribution
- Factory Performance Comparison

---

## 🔍 Analytical Methodology

### Data Cleaning

- Removed invalid records
- Validated sales and profit values
- Handled missing unit values
- Standardized labels

### Feature Engineering

Created:

- Gross Margin %
- Profit Per Unit
- Revenue Contribution %
- Profit Contribution %

### Product Analysis

Identified:

- High-Profit Products
- High-Margin Products
- Low-Margin Products

### Division Analysis

Compared:

- Revenue
- Profit
- Margin

### Cost Diagnostics

Detected:

- Cost Heavy Products
- Pricing Inefficiencies
- Margin Risks

### Pareto Analysis

Identified:

- Products generating 80% Revenue
- Products generating 80% Profit

---

## 📌 Key Insights

- A small number of products contribute the majority of company profit.
- Revenue and profitability are not always aligned.
- Certain products generate high sales but low margins.
- High-margin products represent strategic growth opportunities.
- Profit concentration creates dependency risk.
- Chocolate division acts as the primary profit engine.

---

## 🚀 How to Run

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

## 📷 Dashboard Screenshots

Add screenshots here after deployment.

- Executive Overview
- Product Profitability
- Division Performance
- Cost Diagnostics
- Pareto Analysis
- Factory Analysis

---

## 👨‍💻 Author

Dileep Maurya

Data Science Intern | Unified Mentor

---

## 📜 License

This project is developed for educational and portfolio purposes.