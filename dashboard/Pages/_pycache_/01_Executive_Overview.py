import streamlit as st
st.title("Streamlit test")
st.write("This is a simple Streamlit app to test the setup.")
st.header("Header Example")
st.subheader("Subheader Example")
### Title, for each graph you will have subheader
#### for a section header 
### for insights or important information we use write

name=st.text_input("Enter some text:")
st.write("You entered:", name)



address=st.text_area("Enter some text:")
st.write("You entered:", address)



age=st.number_input("Enter some text:")
st.write("You entered:", int(age))