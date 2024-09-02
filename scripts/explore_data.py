import pandas as pd
from sklearn.datasets import fetch_california_housing

california = fetch_california_housing()

df = pd.DataFrame(california.data, columns=california.feature_names)

df['PRICE'] = california.target

print(f"First N rows:")
print(df.head())

print("Summary stats:")
print(df.describe())

print("Missing values in each column:")
print(df.isnull().sum())

print("Data types:")
print(df.dtypes)