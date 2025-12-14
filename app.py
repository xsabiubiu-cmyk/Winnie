import streamlit as st
import pandas as pd

data = {'Product': ['A', 'B', 'C', 'D', 'E'], 
        'Sales': [1200, 850, 950, 1100, 1300], 
        'Customers': [300, 400, 350, 450, 500]}
df = pd.DataFrame(data)

st.write("### Sample Data")
st.write(df)
