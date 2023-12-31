# -*- coding: utf-8 -*-
"""Iris Flower Cloassification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XvZl3NaNns9YehMjBVkXlyIXCHqE1kZ8
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

df = pd.read_csv('Iris.csv')

df.head()

df.isnull().sum()

df.duplicated().sum()

df.shape

df.corr()

df = df.drop(columns = ['Id'])

df.describe()

df.info()

df["Species"].value_counts()

df['SepalLengthCm'].hist()

color = ['red', 'orange', 'blue']
species = ["Iris-setosa", "Iris-versicolor", "Iris-virginica" ]

for i in range(3):
  x = df[df['Species'] == species[i]]
  plt.scatter(x['SepalLengthCm'], x['SepalWidthCm'], c = color[i], label=species[i])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.legend()

for i in range(3):
  x = df[df['Species'] == species[i]]
  plt.scatter(x['PetalLengthCm'], x['PetalWidthCm'], c = color[i], label=species[i])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.legend()

corr = df.corr()
fig, ax = plt.subplots(figsize = (12,7))
sn.heatmap(corr,annot=True, ax=ax)

from sklearn.preprocessing import LabelEncoder
l = LabelEncoder()

df['Species'] = l.fit_transform(df["Species"])
df.head()

from sklearn.model_selection import train_test_split
x = df.drop(columns=['Species'])
y=df['Species']
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=4)

print(x.shape, x_train.shape,x_test.shape)

y_train

y_test

"""#LogisticRegression"""

from sklearn.linear_model import LogisticRegression
m = LogisticRegression()

m.fit(x_train,y_train)

print("Accuracy: ",m.score(x_test,y_test))

"""#KNN"""

from sklearn.neighbors import KNeighborsClassifier
mm = KNeighborsClassifier()

mm.fit(x_train,y_train)

print("Accuracy: ",mm.score(x_test,y_test))

"""#Decision Tree"""

from sklearn.tree import DecisionTreeClassifier
mmm  = DecisionTreeClassifier()

mmm.fit(x_train,y_train)

print("Accuracy: ",mmm.score(x_test,y_test))

