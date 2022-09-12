import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title('Streamlit dashboard')
df = pd.read_csv('data\Healthcare-Stroke-Data.csv')
n_rows = st.number_input('Number of rows',step=1)
st.write(df.sample(n_rows))
st.write(df.isnull().sum())
# default_column = st.radio('pick default column',options=df.columns)

plot_attr = st.radio('Choose a column to see distribution',index=1,options=df.columns)
val_counts = df[plot_attr].value_counts()
st.pyplot(val_counts.plot(kind='pie').figure)