import streamlit as st
import pandas as pd

# 1. Dashboard Title and Objective
# TODO: Add title and description

# 2. Columns Layout
# TODO: Display Q1, Q2, Q3 revenue in columns
Q1,Q2,Q3=st.columns(3)
with Q1:
    st.header("Q1")
    st.write("$1.2M")
with Q2:
    st.header("Q2")
    st.write("$1.5M")
with Q3:
    st.header("Q3")
    st.write("$1.3M")
    
# TODO: Create tabs for Sales Data, Customer Insights, Market Trends
tab1,tab2,tab3=st.tabs(["sales Data","Customer Insights","Market Trends"])
with tab1:
    st.write("### Sales Data")
    sales_data={
        "Q1 2024": "$1.2M",
        "Q2 2024": "$1.5M",
        "Q3 2024": "$1.3M",
        "Q4 2024": "$1.6M"
    }
    for quarter,revenue in sales_data.items():
        st.write(f"{quarter}：{revenue}")
    df=pd.DataFrame({
        "Quarter":["Q1","Q2","Q3","Q4"],
        "Revenue(in M$)":[1.2,1.5,1.3,1.6]}).set_index("Quarter")
    st.bar_chart(df,height=200)
with tab2:
    st.write("### Customer Insights")
    customer_feedback=[
        "Great service!",
        "Very satisfied with the product quality.",
        "Quick delivery and excellent support."
    ]
    for feedback in customer_feedback:
        st.write(f"-{feedback}")
with tab3:
    st.write("###Market Trends")
    market_trends={
        "Eco-friendly products": "Increasing demand",
        "Online shopping": "Continued growth",
        "Subscription services": "Rising popularity"
    }
    for trend,status in market_trends.items():
        st.write(f"{trend}:{status}")

# 4. Expander
# TODO: Add expander for additional info
with st.expander("More Information"):
    st.write("Data collected via surveys and reports.")

# 5. Dynamic Loading
# TODO: Simulate loading and display insights

# 6. Interactivity
# TODO: Add selectbox and slider for revenue adjustment

# 7. Bonus
# TODO: Add bar chart and motivational button
