# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:28:48 2024

@author: User
"""

import pandas as pd
import streamlit as st

st.write("""
 # My first streamlit app.
 """)
 
 
file1 = pd.read_csv('C:/Users/User/css2024_day2/Motor_Theft/locations.csv')
print(file1)


x = file1['population']
y = file1['density']
st.title("Population verse density")
st.xlabel("Population")
st.ylabel("Density")
st.plot(x, y)
st.show()

st.line_chart(file1)