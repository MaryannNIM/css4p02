# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:25:08 2024

@author: User
"""
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st

st.write("""
 # My first streamlit app.
 """)
 
 
file1 = pd.read_csv('C:/Users/User/css2024_day2/Motor_Theft/locations.csv')
print(file1)


x = file1['population']
y = file1['density']
plt.title("Population verse density")
plt.xlabel("Population")
plt.ylabel("Density")
plt.plot(x, y)
plt.show()

st.line_chart(file1)