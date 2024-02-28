import pandas as pd

# 1. Create a pandas Series from a list of temperatures
temperatures_celsius = [23, 20, 25, 18, 30, 25]
dates = pd.date_range(start='1/1/2024', periods=len(temperatures_celsius))
temperatures_series = pd.Series(temperatures_celsius, index=dates)

# 2. Convert the temperatures from Celsius to Fahrenheit
temperatures_fahrenheit = temperatures_series.apply(lambda x: (x * 9/5) + 32)

temperatures_series, temperatures_fahrenheit

merged_temps = pd.concat([temperatures_series.rename('Celsius'), temperatures_fahrenheit.rename('Fahrenheit')], axis=1)

print(merged_temps)