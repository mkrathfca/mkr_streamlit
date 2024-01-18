import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("laptop.csv")

st.write(df) # Display the dataset

# Create a bar chart
fig = px.bar(df, x="Company", y="Price")

# Display the chart
st.plotly_chart(fig)
