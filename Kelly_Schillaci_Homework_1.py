# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:23:21 2019

@author: kdoyl
"""

import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style="white", color_codes=True)

data = pd.read_csv("master.csv")
data.describe()
data.info()
data.isnull().sum()
data=data.drop(['HDI for year','country-year'],axis=1)

data_suicide_mean = data['suicides/100k pop'].groupby(data.country).mean().sort_values(ascending=False)
f,ax = plt.subplots(1,1,figsize=(10,5))
ax = sns.barplot(data_suicide_mean.head(8).index,data_suicide_mean.head(8),palette='rainbow')

def decade_mapping(data):
    if 1987<= data <= 1996:
        return "1987-1996"
    elif 1997<= data <= 2006:
        return "1997-2006"
    else:
        return "2007-2016"
data.year = data.year.apply(decade_mapping)

plt.figure(figsize=(10,5))
sns.barplot(x = "year", y = "suicides/100k pop", hue = "sex",data = data.groupby(["year","sex"]).sum().reset_index()).set_title("Decades vs Suicides")


test = data.as_matrix()
myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(test)

