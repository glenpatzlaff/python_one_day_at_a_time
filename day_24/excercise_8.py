import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generating sample data
np.random.seed(0)  # For reproducibility
months = pd.date_range(start='2024-01-01', periods=12, freq='M').month_name()
sales_data = {
    'North': np.random.normal(100, 10, 12).cumsum() + np.linspace(0, 50, 12),
    'South': np.random.normal(120, 15, 12).cumsum() + np.linspace(0, 80, 12),
    'East': np.random.normal(90, 20, 12).cumsum() + np.linspace(0, 30, 12),
    'West': np.random.normal(110, 15, 12).cumsum() + np.linspace(0, 60, 12),
}

df_sales = pd.DataFrame(sales_data, index=months)

# Plot setup
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Impact of Marketing Campaign on Sales by Region', fontsize=16)

# Pre-Campaign Sales Analysis
axs[0, 0].bar(df_sales.index[0], df_sales.iloc[0], color=['blue', 'green', 'red', 'purple'])
axs[0, 0].set_title('Pre-Campaign Sales (January)')
axs[0, 0].set_ylabel('Sales')
axs[0, 0].tick_params(labelrotation=45)

# Monthly Sales Trends
for region in df_sales.columns:
    axs[0, 1].plot(df_sales.index, df_sales[region], marker='o', label=region)
axs[0, 1].axvline(x=1, color='gray', linestyle='--', label='Campaign Start')
axs[0, 1].axvline(x=6, color='black', linestyle='--', label='Campaign End')
axs[0, 1].set_title('Monthly Sales Trends')
axs[0, 1].set_ylabel('Cumulative Sales')
axs[0, 1].legend()
axs[0, 1].tick_params(labelrotation=45)

# Post-Campaign Analysis
for region in df_sales.columns:
    axs[1, 0].plot(df_sales.index[6:], df_sales[region][6:], marker='o', label=region)
axs[1, 0].set_title('Post-Campaign Sales Trends')
axs[1, 0].set_ylabel('Cumulative Sales')
axs[1, 0].legend()
axs[1, 0].tick_params(labelrotation=45)

# Comparative Analysis
percentage_increase = ((df_sales.iloc[6] - df_sales.iloc[1]) / df_sales.iloc[1]) * 100
axs[1, 1].scatter(percentage_increase.index, percentage_increase, color=['blue', 'green', 'red', 'purple'], label='Sales Increase %')
axs[1, 1].set_title('Sales Increase Percentage by Region')
axs[1, 1].set_ylabel('% Increase in Sales')
for i, txt in enumerate(percentage_increase):
    axs[1, 1].annotate(f"{txt:.2f}%", (percentage_increase.index[i], percentage_increase[i]))

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
