import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Cost Diagnostics",
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

st.title("💰 Cost vs Margin Diagnostics")

product_summary = (
    df.groupby("Product Name")
    .agg({
        "Sales":"sum",
        "Cost":"sum",
        "Gross Profit":"sum",
        "Units":"sum",
        "Gross Margin %":"mean"
    })
    .reset_index()
)

# Sidebar filters 

st.sidebar.header("Diagnostic Filters")

margin_threshold = st.sidebar.slider(
    "Margin Risk Threshold %",
    0,
    100,
    50
)

cost_threshold = st.sidebar.number_input(
    "High Cost Threshold",
    value=5000
)

# KPI cards

avg_cost = product_summary["Cost"].mean()

avg_margin = product_summary[
    "Gross Margin %"
].mean()

high_cost_products = (
    product_summary["Cost"] >
    avg_cost
).sum()

margin_risk_products = (
    product_summary["Gross Margin %"]
    <
    margin_threshold
).sum()
col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Average Cost",
    f"${avg_cost:,.0f}"
)

col2.metric(
    "Average Margin %",
    f"{avg_margin:.2f}"
)

col3.metric(
    "High Cost Products",
    high_cost_products
)

col4.metric(
    "Margin Risk Products",
    margin_risk_products
)

# chart 1 -- cost vs sales scatter 

fig_cost_sales = px.scatter(
    product_summary,
    x="Cost",
    y="Sales",
    size="Gross Profit",
    hover_name="Product Name",
    title="Cost vs Sales Analysis"
)

st.plotly_chart(
    fig_cost_sales,
    use_container_width=True
)

# chart 2 -- cost vs margin

fig_margin = px.scatter(
    product_summary,
    x="Cost",
    y="Gross Margin %",
    size="Gross Profit",
    hover_name="Product Name",
    title="Cost vs Margin Analysis"
)

st.plotly_chart(
    fig_margin,
    use_container_width=True
)

# Table of risk products 

risk_products = product_summary[
    product_summary[
        "Gross Margin %"
    ] < margin_threshold
]
st.subheader(
    "⚠ Margin Risk Products"
)

st.dataframe(
    risk_products.sort_values(
        "Gross Margin %"
    )
)

cost_heavy = product_summary[
    product_summary["Cost"]
    >
    cost_threshold
]

st.subheader(
    "💸 Cost Heavy Products"
)

st.dataframe(
    cost_heavy.sort_values(
        "Cost",
        ascending=False
    )
)

# Now its time of Auto Recommedation engine 

def classify_product(row):

    if (
        row["Cost"] >
        avg_cost
        and
        row["Gross Margin %"] <
        avg_margin
    ):
        return "Reprice"

    elif (
        row["Cost"] <
        avg_cost
        and
        row["Gross Margin %"] >
        avg_margin
    ):
        return "Star Product"

    elif (
        row["Cost"] >
        avg_cost
        and
        row["Gross Margin %"] >
        avg_margin
    ):
        return "Healthy"

    else:
        return "Review"

product_summary[
    "Recommendation"
] = product_summary.apply(
    classify_product,
    axis=1
)

st.subheader(
    "📋 Product Recommendations"
)

st.dataframe(
    product_summary[
        [
            "Product Name",
            "Cost",
            "Gross Margin %",
            "Recommendation"
        ]
    ]
)
# Recommedation Distribution chart 

recommendation_count = (
    product_summary[
        "Recommendation"
    ]
    .value_counts()
    .reset_index()
)

recommendation_count.columns = [
    "Recommendation",
    "Count"
]

fig_rec = px.pie(
    recommendation_count,
    names="Recommendation",
    values="Count",
    title="Recommendation Distribution"
)

st.plotly_chart(
    fig_rec,
    use_container_width=True
)

# Insight section 
st.subheader(
    "Management Insights"
)

st.markdown("""
### Key Recommendations

- Reprice products with high cost and low margin.
- Increase focus on star products.
- Review low-margin products.
- Optimize sourcing for cost-heavy products.
- Consider discontinuation review for weak products.
""")