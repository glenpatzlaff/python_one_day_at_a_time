import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example synthetic data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Total Sales': [1000, 1500, 1200, 1700, 1600, 2000],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Food', 'Food'],
    'Product': ['Laptop', 'Jacket', 'Smartphone', 'T-shirt', 'Pizza', 'Burger'],
    'Sales': [1000, 500, 700, 200, 400, 600]
}

df = pd.DataFrame(data)

# Adding 'Total Sales' to 'df' for each product to simulate the data needed for the bar chart
df['Total Sales'] = df['Sales'] * np.random.randint(1, 5, df.shape[0])

# Step 4.1: Monthly Sales Trends (Line Plot)
plt.figure(figsize=(12, 8))  # Sets the figure size

# Creating a subplot for the monthly sales trend
plt.subplot(2, 2, 1)  # 2 rows, 2 columns, 1st subplot
plt.plot(df['Month'], df['Total Sales'])
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Sales')

# Step 4.2: Sales Distribution Across Product Categories (Pie Chart)
plt.subplot(2, 2, 2)  # 2nd subplot
categories = df.groupby('Category')['Total Sales'].sum()
plt.pie(categories, labels=categories.index, autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution by Category')

# Step 4.3: Top-Performing Products (Bar Chart)
plt.subplot(2, 1, 2)  # 3rd subplot spans the second row
top_products = df.groupby('Product')['Total Sales'].sum().nlargest(5)
plt.bar(top_products.index, top_products.values)
plt.title('Top-Performing Products')
plt.xlabel('Product')
plt.ylabel('Total Sales')

plt.tight_layout()  # Adjusts the subplots to fit into the figure area
plt.show()
