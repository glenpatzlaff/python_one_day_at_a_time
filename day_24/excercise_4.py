import matplotlib.pyplot as plt
import numpy as np

# Create a 2x2 subplot layout
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Top left: Line plot of y = x
x = np.linspace(-10, 10, 100)
y = x
axs[0, 0].plot(x, y)
axs[0, 0].set_title('Line Plot of $y = x$')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('y')

# Top right: Scatter plot with random data
x_rand = np.random.rand(50)
y_rand = np.random.rand(50)
axs[0, 1].scatter(x_rand, y_rand, color='red')
axs[0, 1].set_title('Scatter Plot with Random Data')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('y')

# Bottom left: Bar chart with three categories
categories = ['Category 1', 'Category 2', 'Category 3']
values = [10, 20, 15]
axs[1, 0].bar(categories, values, color='skyblue')
axs[1, 0].set_title('Bar Chart')
axs[1, 0].set_xlabel('Category')
axs[1, 0].set_ylabel('Value')

# Bottom right: Histogram of random data
data_hist = np.random.randn(1000)
axs[1, 1].hist(data_hist, bins=30, color='green', edgecolor='black')
axs[1, 1].set_title('Histogram of Random Data')
axs[1, 1].set_xlabel('Value')
axs[1, 1].set_ylabel('Frequency')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
