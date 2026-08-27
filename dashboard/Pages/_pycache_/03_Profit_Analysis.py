import streamlit as st
selectbox1=st.selectbox("Select a store",
              ["Store 1", "Store 2", "Store 3"])
st.write("You selected:", selectbox1)

selectbox2=st.selectbox("Select a category",
              ["Electronics", "Clothing", "Books"])
st.write("You selected:", selectbox2)

selectbox3=st.multiselect("Select multiple Products",
                ["Product A", "Product B", "Product C"])
st.write("You selected:", selectbox3[1])


radiooptions=st.radio("Select a payment method",
         ["Credit Card", "Debit Card", "PayPal"])
st.write("You selected:", radiooptions)