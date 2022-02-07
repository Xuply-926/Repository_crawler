#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# coding: utf-8

"""
Created on Tue Feb  1 15:58:15 2022

@author: wxp
"""
import pandas as pd
import numpy as np  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt  
import seaborn as sns


df = pd.read_excel('301158.xlsx')
fig = plt.figure()
x = df['日期'].str[6:]
plt.bar(x,df['成交量(手)'],0.4,color="blue")
plt.xlabel("date")
plt.ylabel("turnover")
plt.title("chart of turnover")
plt.show()  
plt.savefig("301158.jpg")







