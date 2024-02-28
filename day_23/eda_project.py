import pandas as pd

url = "https://github.com/brendanpshea/data-science/raw/main/data/titanic_train.csv"
df = pd.read_csv(url)
#df = pd.read_csv('titanic_stlearn.csv')

print(df.isnull().sum())

df['Age'].fillna(df['Age'].median(), inplace=True)
df.dropna(subset=['Embarked'], inplace=True)

df['Fare'] = df['Fare'].astype(float)

print(df.describe())

print(df.groupby('Pclass')['Survived'].mean())

import matplotlib.pyplot as plt

df.groupby('Pclass')['Survived'].mean().plot(kind='bar', title='Survival Rates by Passenger Class')
plt.show()

df['Age'].plot(kind='hist', bins=20, title='Age Distribution of Passengers')
plt.show()
