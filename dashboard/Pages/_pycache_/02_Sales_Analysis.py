import streamlit as st
st.metric("Students", 100, -10) ### kpis

col1, col2, col3 = st.columns(3)
col1.metric("Revenue", "$10,000", "10%")
col2.metric("Profit", "$2,000", "5%")
col3.metric("Expenses", "$8,000", "-2%")

dateinput=st.date_input("Select a date")
timeinput=st.time_input("Select a time")
colorpicker=st.color_picker("Pick a color")
st.write("You selected date:", dateinput)
st.write("You selected time:", timeinput)
st.write("You selected color:", colorpicker)
st.download_button("Download CSV", data="Name, Age\nJohn, 30\)nJane, 25", file_name="data.csv", mime="text/csv")


import pandas as pd
df=pd.DataFrame({
    "Name": ["John", "Jane", "Alice", "Bob"],
    "Age": [30, 25, 28, 35],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]})
st.dataframe(df)