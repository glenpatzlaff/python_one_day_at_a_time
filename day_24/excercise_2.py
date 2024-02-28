import matplotlib.pyplot as plt
import numpy as np

# Generate random data
x = np.random.rand(100)
y = np.random.rand(100)

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='red', marker='^', label='Data points')

# Customizations
plt.title('Scatter Plot with Random Data')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show plot
plt.show()
