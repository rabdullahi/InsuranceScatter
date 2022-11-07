import streamlit as st 
import pandas as pd 
import altair as alt
import numpy as np


#Import the insurance data set 
insurance_data = pd.read_csv('insurance.csv') 


st.write(insurance_data)


st.sidebar.header("Pick two variables for your scatter plot")
x_val= st.sidebar.selectbox("Pick your x-axis", insurance_data.select_dtypes(include=np.number).columns.tolist())
y_val= st.sidebar.selectbox("Pick your y-axis", insurance_data.select_dtypes(include=np.number).columns.tolist())


scatter = alt.Chart(insurance_data, title=f"Correlation between {x_val} and {y_val}").mark_point(size=50, opacity=.7, color="purple").encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val, title=f"{y_val}"),
    tooltip=[x_val,y_val])
st.altair_chart(scatter,use_container_width=True)

#Calculate the correlation 
corr=round(insurance_data[x_val].corr(insurance_data[y_val]),2)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")