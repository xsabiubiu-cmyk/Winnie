import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Business Sales Dashboard")
st.write("Analyze monthly sales data interactively!")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = np.random.randint(5000, 20000, size=12)
expenses = np.random.randint(3000, 15000, size=12)

data=pd.DataFrame({
    "Month":months,
    "Sales":sales,
    "Expenses":expenses
})

st.sidebar.header("Filters")
selected_months = st.sidebar.multiselect("Select Months", months, default=months)
show_expenses = st.sidebar.checkbox("Show Expenses", value=True)

filtered_data = data[data["Month"].isin(selected_months)]

st.subheader("Filtered Data")
st.dataframe(filtered_data)

st.subheader("Key Metrics")
col1,col2,col3=st.columns(3)
col1.metric("Total Sales",f"${filtered_data['sales'].sum():,.0f}")
col2.metric("Total Expenses",f"${filtered_data['Expenses'].sum():,.0f}")
col3.metric("Profit",f"${(filtered_data['Sales'].sum() - filtered_data['Expenses'].sum()):,.0f}")

