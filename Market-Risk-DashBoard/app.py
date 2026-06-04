import streamlit as st
import pandas as pd
import numpy as np

st.title("Global Market Risk Analytics Platform")

data = pd.DataFrame({
    "Portfolio": ["Equity", "FX", "Commodities"],
    "VaR": np.random.randint(10000, 50000, 3),
    "Expected Shortfall": np.random.randint(15000, 60000, 3)
})

st.dataframe(data)
st.bar_chart(data.set_index("Portfolio"))
