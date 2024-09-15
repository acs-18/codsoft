# -*- coding: utf-8 -*-
"""Task _01.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vW4mKUVunrT5zCKtHJCRroDFUszs5sST
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/content/Titanic-Dataset.csv')

df.info()

df.isnull().sum()

df.head(10)

df.dropna(subset=['Age'],inplace=True)
df.dropna(subset=['Embarked'],inplace=True)
df.dropna(subset=['Cabin'],inplace=True)

df.isnull().sum()

# AGE DISTRIBUTION

plt.figure(figsize=(10,6))
sns.histplot(df['Age'],color='red',bins=35)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

#SURVIVAL PREDICTION

df['Survived'].value_counts()
df['Survived'].unique()
df['Not Survived']=0
df.loc[df['Survived']==1,'Not Survived']=0
df.head()

df['Survived'].value_counts()
df['Not Survived'].value_counts()

plt.figure(figsize=(10,6))
sns.countplot(x='Survived',data=df)
plt.title('Survival Prediction')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.xticks([0,1],['Not Survived','Survived'])
plt.show()

#SURVIVAL BY GENDER

plt.figure(figsize=(10,6))
sns.countplot(x='Survived',hue='Sex',data=df)
plt.title('Survival By Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks([0,1],['Not Survived','Survived'])
plt.show()

# SURVIVAL RATE BY CLASS

plt.figure(figsize=(10,6))
sns.barplot(x='Pclass',y='Survived',data=df)
plt.title('Survival Rate By Class')
plt.xlabel('Class')
plt.ylabel('Survival Rate')
plt.show()

# SURVIVAL RATE BY CABIN
plt.figure(figsize=(8, 6))
sns.barplot(x='Cabin', y='Survived', data=df)
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.show()
