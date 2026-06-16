import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Pareto Analysis",
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

    return df

df = load_data()

st.title("📊 Pareto Analysis Dashboard")

pareto_revenue = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(
        ascending=False
    )
    .reset_index()
)

pareto_revenue[
    "Revenue %"
] = (
    pareto_revenue["Sales"]
    /
    pareto_revenue["Sales"].sum()
) * 100

pareto_revenue[
    "Cumulative Revenue %"
] = (
    pareto_revenue["Revenue %"]
).cumsum()

fig = go.Figure()

fig.add_bar(
    x=pareto_revenue["Product Name"],
    y=pareto_revenue["Revenue %"],
    name="Revenue %"
)

fig.add_scatter(
    x=pareto_revenue["Product Name"],
    y=pareto_revenue["Cumulative Revenue %"],
    mode="lines+markers",
    name="Cumulative %"
)

fig.add_hline(
    y=80,
    line_dash="dash"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# KPI 1

products_80_revenue = (
    pareto_revenue[
        pareto_revenue[
            "Cumulative Revenue %"
        ] <= 80
    ]
)

st.metric(
    "Products Driving 80% Revenue",
    len(products_80_revenue)
)

# Profit Pareto Analysis
pareto_profit = (
    df.groupby("Product Name", as_index=False)
    ["Gross Profit"]
    .sum()
    .sort_values("Gross Profit", ascending=False)
)

pareto_profit["Profit %"] = (
    pareto_profit["Gross Profit"]
    /
    pareto_profit["Gross Profit"].sum()
) * 100

pareto_profit["Cumulative Profit %"] = (
    pareto_profit["Profit %"]
).cumsum()

print(pareto_profit.columns)



# Graph of this 

import plotly.graph_objects as go

fig2 = go.Figure()

# Profit Contribution Bars
fig2.add_trace(
    go.Bar(
        x=pareto_profit["Product Name"],
        y=pareto_profit["Profit %"],
        name="Profit Contribution %",
        marker_color="royalblue"
    )
)

# Cumulative Profit Line
fig2.add_trace(
    go.Scatter(
        x=pareto_profit["Product Name"],
        y=pareto_profit["Cumulative Profit %"],
        mode="lines+markers",
        name="Cumulative Profit %",
        yaxis="y2"
    )
)

# 80% Reference Line
fig2.add_hline(
    y=80,
    line_dash="dash",
    annotation_text="80% Threshold"
)

fig2.update_layout(
    title="Pareto Analysis - Profit Contribution",
    xaxis_title="Products",
    yaxis_title="Profit Contribution %",
    height=600,
    hovermode="x unified"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)


# Final Insight Section 

st.subheader(
    "Executive Insights"
)

st.markdown("""
### Key Findings

- A small number of products generate the majority of company revenue.
- Profit contribution is concentrated among a limited set of products.
- Heavy dependence on a few products creates business risk.
- High-profit products should receive strategic focus.
- Revenue contribution and profit contribution are not always aligned.
""")