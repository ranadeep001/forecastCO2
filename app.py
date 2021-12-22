#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
@Group4 

"""

import streamlit as st
import pandas as pd
import xlrd
import numpy as np
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from matplotlib import pyplot
from matplotlib import pyplot as plt
import time
from time import sleep
#from scipy import stats
#import scipy.stats as st
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings("ignore")

data =pd.read_excel("CO2_dataset.xlsx", sheet_name="Sheet1", parse_dates=True")

final_arima = ARIMA(data['CO2'],order = (3,1,4))
final_arima = final_arima.fit()

data2=data.copy()

st.title("Forecasting CO2 Emission")
nav = st.sidebar.radio("Navigation",["About data","Prediction","Forecast"])
if nav == "About data":
    st.subheader("Data")
    data
    st.subheader("Scatter plot of the data")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.figure(figsize = (10,5))
    plt.scatter(data["Year"],data["CO2"])
    plt.ylim(0)
    plt.xlabel("Years")
    plt.ylabel("CO2 Emission")
    plt.tight_layout()
    st.pyplot()


    st.subheader("Area plot of the data") 
    st.area_chart(data=data.CO2, width=150, height=300, use_container_width=True)
   

    st.subheader("Line plot of the data") 
    st.line_chart(data=data.CO2, width=150, height=300, use_container_width=True)
   

    st.subheader("Histogram of the data") 
    fig= plt.figure(figsize=(10,4))
    plt.hist(data.CO2)
    st.pyplot(fig)
    
    
if nav =="Prediction":
    plt.plot(data.CO2, label='original')
    plt.plot(final_arima.fittedvalues, label='forecast')
    plt.title('Forecast')
    plt.legend(loc='upper left',fontsize=8)
    st.pyplot()
    
    
if nav == "Forecast":
    
    year = st.slider("Select number of Year from 2015",1,100,step = 1)

    st.subheader("Forecasting the data for next few years")
    
    pred = final_arima.forecast(year)

   
    if st.button("Predict"):
        
     with st.spinner('loading data...'):
         time.sleep(5)
     st.subheader(f"Your predicted CO2 emission from year 2015" )
     pred

     fig = go.Figure(data=[go.Table(header=dict(values=['CO2']),cells=dict(values=[pred]))])
     st.write(fig)
     st.subheader("Line plot of the Forecasted data")
     st.line_chart(pred)
     st.subheader("Area plot of the Forecasted data")
     st.area_chart(pred)
     st.subheader("Histogram of the data") 
     fig= plt.figure(figsize=(10,4))
     plt.hist(pred)
     st.pyplot(fig)
     st.subheader("Barchart of the Forecasted data")
     st.bar_chart(pred)

