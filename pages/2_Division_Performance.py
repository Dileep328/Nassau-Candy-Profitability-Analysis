import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Division Performance",
    layout="wide"
)

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/Nassau Candy Distributor.csv"
    )

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        dayfirst=True
    )

    df["Gross Margin %"] = (
        df["Gross Profit"]
        /
        df["Sales"]
    ) * 100

    return df

df = load_data()

st.title("🏭 Division Performance Dashboard")

st.sidebar.header("Filters")

selected_divisions = st.sidebar.multiselect(
    "Division",
    options=df["Division"].unique(),
    default=df["Division"].unique()
)

filtered_df = df[
    df["Division"].isin(
        selected_divisions
    )
]

# Deivision Agregation 

division_summary = (
    filtered_df
    .groupby("Division")
    .agg({
        "Sales":"sum",
        "Gross Profit":"sum",
        "Units":"sum",
        "Gross Margin %":"mean"
    })
    .reset_index()
)

# KPI Cards

best_revenue_division = (
    division_summary
    .sort_values(
        "Sales",
        ascending=False
    )
    .iloc[0]
)

best_profit_division = (
    division_summary
    .sort_values(
        "Gross Profit",
        ascending=False
    )
    .iloc[0]
)

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Top Revenue Division",
    best_revenue_division["Division"]
)

col2.metric(
    "Revenue",
    f"${best_revenue_division['Sales']:,.0f}"
)

col3.metric(
    "Top Profit Division",
    best_profit_division["Division"]
)

col4.metric(
    "Profit",
    f"${best_profit_division['Gross Profit']:,.0f}"
)

# Chart 1 -- Revenvue by devision 

fig_sales = px.bar(
    division_summary,
    x="Division",
    y="Sales",
    title="Revenue by Division",
    text_auto=True
)

st.plotly_chart(
    fig_sales,
    use_container_width=True
)

# Chart 2 -- Profit by devision 

fig_profit = px.bar(
    division_summary,
    x="Division",
    y="Gross Profit",
    title="Profit by Division",
    text_auto=True
)

st.plotly_chart(
    fig_profit,
    use_container_width=True
)

# Margin Comparison

fig_margin = px.bar(
    division_summary,
    x="Division",
    y="Gross Margin %",
    title="Average Margin by Division",
    text_auto='.2f'
)

st.plotly_chart(
    fig_margin,
    use_container_width=True
)

# Chart 4-- Revenue vs Profit 

fig_compare = px.scatter(
    division_summary,
    x="Sales",
    y="Gross Profit",
    size="Units",
    color="Division",
    hover_name="Division",
    title="Revenue vs Profit by Division"
)

st.plotly_chart(
    fig_compare,
    use_container_width=True
)

# Chart 5-- Revenue Share 

fig_pie = px.pie(
    division_summary,
    names="Division",
    values="Sales",
    title="Revenue Share by Division"
)

st.plotly_chart(
    fig_pie,
    use_container_width=True
)

# Charrt 6 -- Profit share 

fig_profit_share = px.pie(
    division_summary,
    names="Division",
    values="Gross Profit",
    title="Profit Share by Division"
)

st.plotly_chart(
    fig_profit_share,
    use_container_width=True
)

# Insight section

st.subheader("Division Insights")

st.markdown("""
### Key Findings

- Chocolate division generates the highest profit.
- Revenue and profit contribution are not evenly distributed.
- Margin differences indicate varying operational efficiency.
- Low-margin divisions should undergo pricing and cost review.
- High-performing divisions should receive strategic investment.
""")