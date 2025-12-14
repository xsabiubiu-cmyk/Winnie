import streamlit as st
import pandas as pd

data = {'Product': ['A', 'B', 'C', 'D', 'E'], 
        'Sales': [1200, 850, 950, 1100, 1300], 
        'Customers': [300, 400, 350, 450, 500]}
df = pd.DataFrame(data)

st.write("### Sample Data")
st.dataframe(df)
sales_range = st.slider("Select Sales Range", min_value=0, max_value=1500, value=(500, 1000))
filtered_df = df[(df['Sales'] >= sales_range[0]) & (df['Sales'] <= sales_range[1])]
product_choice=st.selectbox("Select Product",filtered_df["Product"])

with st.form(key="Feedback_form"):
        product_id=st.text_input("Enter Product ID:")
        feedback=st.text_area("Enter your feedback:")
        submit_button=st.form_submit_button("Submit Feedback")

def submit_feedback():
        st.write("### Submitted Feedback")
        st.write(f"**Product:** {product_choice}")
        st.write(f"**Sales Range:** {sales_range}")
        st.write(f"**Product ID:** {product_id}")
        st.write(f"**Feedback:** {feedback}")
if submit_button:
        submit_feedback()
        
