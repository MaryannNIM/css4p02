# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:25:08 2024

@author: User
"""
import streamlit as st
import pandas as pd
 
st.write("""
# My first app
""")
 
df = pd.read_csv("Motor_Theft/locations.csv")
x = df['population']
y = df['density']
st.title("Population verse density")
st.xlabel("Population")
st.ylabel("Density")
st.plot(x, y)

st.line_chart(df)
