import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Product Profitability",
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

    df["Profit Per Unit"] = (
        df["Gross Profit"]
        /
        df["Units"]
    )

    return df

df = load_data()

st.title("📈 Product Profitability Dashboard")

st.sidebar.header("Filters")

division_filter = st.sidebar.multiselect(
    "Division",
    options=df["Division"].unique(),
    default=df["Division"].unique()
)

margin_threshold = st.sidebar.slider(
    "Minimum Margin %",
    0,
    100,
    20
)

product_search = st.sidebar.text_input(
    "Search Product"
)

filtered_df = df[
    (df["Division"].isin(division_filter))
    &
    (df["Gross Margin %"] >= margin_threshold)
]

if product_search:

    filtered_df = filtered_df[
        filtered_df["Product Name"]
        .str.contains(
            product_search,
            case=False
        )
    ]

product_summary = (
    filtered_df
    .groupby("Product Name")
    .agg({
        "Sales":"sum",
        "Gross Profit":"sum",
        "Units":"sum",
        "Gross Margin %":"mean"
    })
    .reset_index()
)
best_profit_product = (
    product_summary
    .sort_values(
        "Gross Profit",
        ascending=False
    )
    .iloc[0]
)

best_margin_product = (
    product_summary
    .sort_values(
        "Gross Margin %",
        ascending=False
    )
    .iloc[0]
)

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Top Profit Product",
    best_profit_product["Product Name"]
)

col2.metric(
    "Profit",
    f"${best_profit_product['Gross Profit']:,.0f}"
)

col3.metric(
    "Top Margin Product",
    best_margin_product["Product Name"]
)

col4.metric(
    "Margin %",
    f"{best_margin_product['Gross Margin %']:.2f}"
)

# Chart 1: Top Products by Profit


top_profit = (
    product_summary
    .sort_values(
        "Gross Profit",
        ascending=False
    )
    .head(10)
)

fig_profit = px.bar(
    top_profit,
    x="Gross Profit",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Profit",
    text_auto=True
)

st.plotly_chart(
    fig_profit,
    use_container_width=True
)

# Chart 2: Top Margin Products


top_margin = (
    product_summary
    .sort_values(
        "Gross Margin %",
        ascending=False
    )
    .head(10)
)

fig_margin = px.bar(
    top_margin,
    x="Gross Margin %",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Margin",
    text_auto=True
)

st.plotly_chart(
    fig_margin,
    use_container_width=True
)

# Chart 3: Revenue vs Profit Scatter Plot


fig_scatter = px.scatter(
    product_summary,
    x="Sales",
    y="Gross Profit",
    size="Units",
    hover_name="Product Name",
    title="Revenue vs Profit Analysis"
)

st.plotly_chart(
    fig_scatter,
    use_container_width=True
)

# Chart 4: Profit Contribution

product_summary[
    "Profit Contribution %"
] = (
    product_summary["Gross Profit"]
    /
    product_summary["Gross Profit"].sum()
) * 100

top_contributors = (
    product_summary
    .sort_values(
        "Profit Contribution %",
        ascending=False
    )
    .head(10)
)

fig_contribution = px.pie(
    top_contributors,
    names="Product Name",
    values="Profit Contribution %",
    title="Profit Contribution by Product"
)

st.plotly_chart(
    fig_contribution,
    use_container_width=True
)

# Insights Section

st.subheader("Key Insights")

st.markdown("""
- High-profit products should receive marketing priority.
- High-sales but low-profit products require pricing review.
- Low-sales and low-profit products are candidates for rationalization.
- Margin leaders demonstrate strong financial efficiency.
""")