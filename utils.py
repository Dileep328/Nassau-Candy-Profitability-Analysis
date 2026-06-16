import pandas as pd
import streamlit as st

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
        df["Gross Profit"] /
        df["Sales"]
    ) * 100

    df["Profit Per Unit"] = (
        df["Gross Profit"] /
        df["Units"]
    )

    return df