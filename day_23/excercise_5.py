import pandas as pd

# Given time series DataFrame representing the daily closing prices of a stock
dates = pd.date_range(start='2023-01-01', periods=5, freq='D')
prices = [100, 101, 103, 102, 105]

df_stock = pd.DataFrame({'Closing Price': prices}, index=dates)

# Calculate the daily percentage change in closing prices
df_stock['Daily % Change'] = df_stock['Closing Price'].pct_change() * 100

# Compute a 3-day moving average of the closing prices
df_stock['3-Day MA'] = df_stock['Closing Price'].rolling(window=3).mean()

# Display the updated DataFrame
print(df_stock)
