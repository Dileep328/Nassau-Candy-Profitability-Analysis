import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Factory Analysis",
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

# -----------------------------------
# Product Factory Mapping
# -----------------------------------

factory_mapping = {
    "Wonka Bar - Nutty Crunch Surprise":"Lot's O' Nuts",
    "Wonka Bar - Fudge Mallows":"Lot's O' Nuts",
    "Wonka Bar -Scrumdiddlyumptious":"Lot's O' Nuts",

    "Wonka Bar - Milk Chocolate":"Wicked Choccy's",
    "Wonka Bar - Triple Dazzle Caramel":"Wicked Choccy's",

    "Laffy Taffy":"Sugar Shack",
    "SweeTARTS":"Sugar Shack",
    "Nerds":"Sugar Shack",
    "Fun Dip":"Sugar Shack",
    "Fizzy Lifting Drinks":"Sugar Shack",

    "Everlasting Gobstopper":"Secret Factory",
    "Lickable Wallpaper":"Secret Factory",
    "Wonka Gum":"Secret Factory",

    "Hair Toffee":"The Other Factory",
    "Kazookles":"The Other Factory"
}

df["Factory"] = df["Product Name"].map(
    factory_mapping
)

st.title("🏭 Factory Performance Dashboard")


# Factory Summary


factory_summary = (
    df.groupby("Factory")
    .agg({
        "Sales":"sum",
        "Gross Profit":"sum",
        "Units":"sum",
        "Gross Margin %":"mean"
    })
    .reset_index()
)


# KPI Cards

top_revenue_factory = (
    factory_summary
    .sort_values(
        "Sales",
        ascending=False
    )
    .iloc[0]
)

top_profit_factory = (
    factory_summary
    .sort_values(
        "Gross Profit",
        ascending=False
    )
    .iloc[0]
)

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Top Revenue Factory",
    top_revenue_factory["Factory"]
)

col2.metric(
    "Revenue",
    f"${top_revenue_factory['Sales']:,.0f}"
)

col3.metric(
    "Top Profit Factory",
    top_profit_factory["Factory"]
)

col4.metric(
    "Profit",
    f"${top_profit_factory['Gross Profit']:,.0f}"
)

# Revenue by factory 

fig_sales = px.bar(
    factory_summary,
    x="Factory",
    y="Sales",
    title="Revenue by Factory",
    text_auto=True
)

st.plotly_chart(
    fig_sales,
    use_container_width=True
)

# Profit by factory 

fig_profit = px.bar(
    factory_summary,
    x="Factory",
    y="Gross Profit",
    title="Profit by Factory",
    text_auto=True
)

st.plotly_chart(
    fig_profit,
    use_container_width=True
)

# Margin by Factory 

fig_margin = px.bar(
    factory_summary,
    x="Factory",
    y="Gross Margin %",
    title="Average Margin by Factory",
    text_auto=".2f"
)

st.plotly_chart(
    fig_margin,
    use_container_width=True
)


# Revenue vs Profit scatter 


fig_scatter = px.scatter(
    factory_summary,
    x="Sales",
    y="Gross Profit",
    size="Units",
    color="Factory",
    hover_name="Factory",
    title="Revenue vs Profit by Factory"
)

st.plotly_chart(
    fig_scatter,
    use_container_width=True
)


# Revenue Share 

fig_pie = px.pie(
    factory_summary,
    names="Factory",
    values="Sales",
    title="Factory Revenue Share"
)

st.plotly_chart(
    fig_pie,
    use_container_width=True
)

# Factory performance Table 

st.subheader("Factory Performance Summary")

st.dataframe(
    factory_summary
    .sort_values(
        "Gross Profit",
        ascending=False
    )
)

# Factory Coordinates Table 

factory_locations = pd.DataFrame({
    "Factory":[
        "Lot's O' Nuts",
        "Wicked Choccy's",
        "Sugar Shack",
        "Secret Factory",
        "The Other Factory"
    ],
    "Latitude":[
        32.881893,
        32.076176,
        48.119140,
        41.446333,
        35.117500
    ],
    "Longitude":[
        -111.768036,
        -81.088371,
        -96.181150,
        -90.565487,
        -89.971107
    ]
})

st.subheader("Factory Locations")

st.dataframe(factory_locations)


# BONUS

st.subheader("🗺 Factory Locations Map")

st.map(
    factory_locations.rename(
        columns={
            "Latitude":"lat",
            "Longitude":"lon"
        }
    )
)

# Final Insight section 

st.subheader("Executive Insights")

st.markdown("""
### Key Findings

- Factory performance differs significantly across revenue and profitability.
- Some factories generate higher profit despite lower sales.
- Margin efficiency varies across manufacturing locations.
- High-performing factories should be prioritized for capacity expansion.
- Low-margin factories require cost optimization initiatives.
""")