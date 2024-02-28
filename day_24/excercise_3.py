import matplotlib.pyplot as plt
import numpy as np

# Generate 1000 random numbers from a normal distribution
data = np.random.randn(1000)

plt.figure(figsize=(10, 6))

# Create histogram
plt.hist(data, bins=30, color='skyblue', edgecolor='black')

# Customize histogram
plt.grid(True)
plt.title('Histogram of 1000 Random Numbers from Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show plot
plt.show()
