import streamlit as st
import pandas as pd

def get_sample_df() -> pd.DataFrame:
    data = [
        {"Date":"2025-10-01","Category":"Food","Amount":35.5,"Description":"Lunch","PaymentMethod":"Octopus"},
        {"Date":"2025-10-02","Category":"Transport","Amount":18.0,"Description":"MTR","PaymentMethod":"Octopus"},
        {"Date":"2025-10-03","Category":"Study","Amount":120.0,"Description":"Textbook","PaymentMethod":"Card"},
        {"Date":"2025-10-04","Category":"Entertainment","Amount":80.0,"Description":"Movie","PaymentMethod":"Card"},
        {"Date":"2025-10-05","Category":"Food","Amount":52.0,"Description":"Dinner","PaymentMethod":"Cash"},
        {"Date":"2025-10-06","Category":"Other","Amount":15.0,"Description":"Snacks","PaymentMethod":"Cash"},
        {"Date":"2025-10-07","Category":"Transport","Amount":25.0,"Description":"Bus","PaymentMethod":"Octopus"},
        {"Date":"2025-10-08","Category":"Food","Amount":28.0,"Description":"Breakfast","PaymentMethod":"Cash"},
        {"Date":"2025-10-09","Category":"Study","Amount":60.0,"Description":"Printing","PaymentMethod":"Card"},
        {"Date":"2025-10-10","Category":"Entertainment","Amount":200.0,"Description":"Concert","PaymentMethod":"Alipay"},
        {"Date":"2025-10-11","Category":"Other","Amount":40.0,"Description":"","PaymentMethod":"WeChat"},
        {"Date":"2025-10-12","Category":"Food","Amount":90.0,"Description":"Hotpot","PaymentMethod":"Card"},
    ]
    return pd.DataFrame(data)

st.title("Student Spending Analyzer")
st.write("You can upload a csv file and we will give you a comprehensive analysis.")

uploaded=st.file_uploader("Upload your file here.",type=["csv"])
REQUIRED_COLS = {"Date", "Category", "Amount", "Description", "PaymentMethod"}



if uploaded is None:
    df = get_sample_df()
    st.write("No file uploaded. Using sample data.")
else:
    df = pd.read_csv(uploaded)

    missing = REQUIRED_COLS - set(df.columns)
    if missing:
        st.write("Your file is missing required columns:")
        st.write(sorted(list(missing)))
        st.write("Please fix your CSV and upload again.")
        st.stop()
if "df" not in st.session_state:
    st.session_state.df = df
df = st.session_state.df

tab1,tab2,tab3=st.tabs(["Data","Insight","Add Record"])
with tab1:
    st.write(df.info())
    st.dataframe(df)
    
    categories=list(df["Category"].unique())
    select_list=["All"]+categories
    selected=st.selectbox("Select a category",select_list)
    keyword=st.text_input("Search keyword in Description:")
    filtered_df=df.copy()
    if selected!="All":
        filtered_df=filtered_df[filtered_df["Category"]==selected]
    keyword=keyword.strip()
    if keyword!="":
        mask = filtered_df["Description"].astype(str).str.contains(keyword, case=False, na=False)
        filtered_df = filtered_df[mask]
    st.write(f"Filtered rows:{len(filtered_df)}")
    st.dataframe(filtered_df)

    with st.expander("数据诊断区域"):
        df.info()
        df.describe()

with tab2:
    col1,col2,col3=st.columns(3)
    with col1:
        st.header("Total  Spending")
        st.write(f"${df['Amount'].sum():.2f}")
    with col2:
        st.header("Avg Spending")
    with col3:
        st.header("Max Single Expense")
        maxamount=df["Amount"].max()
    selectedbar=st.number_input("Enter the amount:")
    if st.button("View the result"):
        filtered_df2=df[df["Amount"]>=selectedbar]
        display_df=filtered_df2[["Date","Category","Amount","Description"]]
        if len(filtered_df2)!=0:
            st.dataframe(display_df)
        elif len(filtered_df2)==0:
            st.write("No entry fullfill the requirement.")

with tab3:
    with st.form(key="Add Record"):
        date=st.text_input("Enter the Date(Format:YYYY-MM-DD):")
        category=st.selectbox("What is the category:",df["Category"].unique())
        amount=st.number_input("Enter the amount",min_value=0.0)
        description=st.text_input("Write the description")
        paymentmethod=st.selectbox("Select your payment method:",df["PaymentMethod"].unique())
        add_button=st.form_submit_button("Add")
    if add_button:
        errors=[]

        if date.strip()=="":
            errors.append("Date cannot be empty")
        if amount==0:
            errors.append("Amount cannot be zero.")

        if len(errors)>0:
            for msg in errors:
                st.write(msg)
        else:
            new_row=pd.DataFrame([{
                "Date":date,
                "Category":category,
                "Amount":amount,
                "Description":description,
                "PaymentMethod":paymentmethod,
            }])
            st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
            st.success("Record added!")
            st.dataframe(st.session_state.df.tail(5))
