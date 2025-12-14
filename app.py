import streamlit as st

st.title("Basic Web Calculator")

num1=st.number_input("Enter the first number:",value=0.0,format="%.1f")
num2=st.number_input("Enter the second number:",value=0.0,format="%.1f")

operation=st.selectbox("Choose operation",["Add","Subtract","Multiply","Division"])

if st.button("Calculate"):
    if operation=="Add":
        result=num1+num2
    elif operation=="Subtract":
        result=num1-num2
    elif operation=="Multiply":
        result=num1*num2
    elif operation=="Division":
        if num2!=0:
            result=num1/num2 
        else:
            st.error("Error: Division by zero")
            st.stop()
    st.success(f"Result:{result}")
