# -*- coding: utf-8 -*-
"""CIE1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gYF1TCP6p0AtVrnGnkJ6tlSUSlqvbV0a
"""

import pandas as pd
Series_A=pd.Series([1,2,3,4,5])
Series_B=pd.Series([2,4,6,8,10])
common_items=Series_A[Series_A.isin(Series_B)]
print(common_items)

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('mtcars.csv')
df.head()

plt.hist(df['mpg'],bins=10)
plt.title('frequency distribution')
plt.xlabel('frequency')
plt.ylabel(['mpg'])
plt.show()

plt.scatter(df['wt'],df['mpg'])
plt.title("scatter plot")
plt.xlabel("weight")
plt.ylabel("mpg")
plt.show()

plt.scatter(df['wt'],df['mpg'])
plt.xlabel('weigth')
plt.ylabel('mpg')
plt.title('scatter plot')
plt.show()

trans=df['am'].value_counts()
plt.figure(figsize=[7,7])
trans.plot(kind='bar',color='green')
plt.title('frequency distribution type of cars')
plt.xlabel('transmission of cars')
plt.ylabel('transmission type of cars')
plt.show()

plt.figure(figsize=[6,6])
plt.boxplot(data['mpg'],vert=True,notch=False,patch_artist=True)
plt.show()