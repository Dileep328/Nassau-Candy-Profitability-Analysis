import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Nassau Candy Dashboard",
    page_icon="🍫",
    layout="wide"
)

# ----------------------
# Load Data
# ----------------------

@st.cache_data
def load_data():
    df = pd.read_csv("data/Nassau Candy Distributor.csv")

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        dayfirst=True
    )

    df["Gross Margin %"] = (
        df["Gross Profit"] /
        df["Sales"]
    ) * 100

    df["Profit Per Unit"] = (
        df["Gross Profit"] /
        df["Units"]
    )

    return df

df = load_data()

# ----------------------
# Sidebar
# ----------------------

st.sidebar.header("Filters")

division = st.sidebar.multiselect(
    "Select Division",
    options=df["Division"].unique(),
    default=df["Division"].unique()
)

filtered_df = df[
    df["Division"].isin(division)
]

# ----------------------
# KPI Calculations
# ----------------------

total_revenue = filtered_df["Sales"].sum()

total_profit = filtered_df["Gross Profit"].sum()

avg_margin = filtered_df[
    "Gross Margin %"
].mean()

total_units = filtered_df[
    "Units"
].sum()

# ----------------------
# Dashboard Title
# ----------------------

st.title(
    "🍫 Nassau Candy Profitability Dashboard"
)

st.markdown(
    "Executive Overview of Product Line Profitability"
)

# ----------------------
# KPI Cards
# ----------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Revenue",
    f"${total_revenue:,.0f}"
)

col2.metric(
    "Profit",
    f"${total_profit:,.0f}"
)

col3.metric(
    "Margin %",
    f"{avg_margin:.2f}%"
)

col4.metric(
    "Units Sold",
    f"{total_units:,.0f}"
)

monthly_sales = (
    filtered_df.groupby(
        pd.Grouper(
            key="Order Date",
            freq="ME"
        )
    )["Sales"]
    .sum()
    .reset_index()
)

fig_sales = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    title="Monthly Revenue Trend",
    markers=True
)

st.plotly_chart(
    fig_sales,
    use_container_width=True
)

monthly_profit = (
    filtered_df.groupby(
        pd.Grouper(
            key="Order Date",
            freq="ME"
        )
    )["Gross Profit"]
    .sum()
    .reset_index()
)

fig_profit = px.line(
    monthly_profit,
    x="Order Date",
    y="Gross Profit",
    title="Monthly Profit Trend",
    markers=True
)

st.plotly_chart(
    fig_profit,
    use_container_width=True
)

division_sales = (
    filtered_df.groupby("Division")["Sales"]
    .sum()
    .reset_index()
)

fig_division = px.bar(
    division_sales,
    x="Division",
    y="Sales",
    title="Revenue by Division",
    text_auto=True
)

st.plotly_chart(
    fig_division,
    use_container_width=True
)