import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df=pd.read_csv('diamonds.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

sns.histplot(df['price'],bins=50,kde=True)
plt.title('Price distribution')
plt.show()

sns.scatterplot(x='carat',y='price',data=df,alpha=0.5)
plt.title('Price vs Carat')
plt.show()

sns.boxplot(x='cut',y='price',data=df)
plt.title('Price by Cut')
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='clarity', y='price', data=df)
plt.title('Price by Clarity')
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='color', y='price', data=df)
plt.title('Price by Color')
plt.show()


corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
