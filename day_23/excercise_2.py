# Re-import numpy and pandas due to the reset state
import pandas as pd
import numpy as np

# Redefine the DataFrame with given data
data = {
    'Product': ['Apples', 'Oranges', np.nan, 'Bananas', 'Strawberries'],
    'Sales': [100, np.nan, 150, np.nan, 200],
    'Price': [1.2, 0.8, np.nan, 0.5, 1.5]
}
df = pd.DataFrame(data)

# 1. Remove rows with missing values in the 'Product' column
df_cleaned = df.dropna(subset=['Product'])

# 2. Fill missing values in 'Sales' and 'Price' columns with the mean of their respective columns
df_cleaned['Sales'].fillna(df_cleaned['Sales'].mean(), inplace=True)
df_cleaned['Price'].fillna(df_cleaned['Price'].mean(), inplace=True)

print(df_cleaned)

