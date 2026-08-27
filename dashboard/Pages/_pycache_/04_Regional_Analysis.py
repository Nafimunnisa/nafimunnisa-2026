import streamlit as st
# varaiable=st.file_uploader("Upload a file", type=["pdf", "xlsx"],max_upload_size=20)
# st.write(varaiable)


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.DataFrame({
    "Sales": [100, 200, 150, 300, 250],
    "Profit": [20, 40, 30, 70, 50]
})
st.line_chart(df)
st.bar_chart(df)
st.scatter_chart(df,x="Sales",y="Profit")

figure=plt.plot(df["Sales"], df["Profit"]   )
st.pyplot(figure)

figure=sns.scatterplot(data=df,x='sales',y='profit')
st.pyplot(figure)    
