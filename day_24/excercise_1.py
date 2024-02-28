import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(-10, 10, 400)
# Calculate y = x^2
y = x ** 2

# Create line plot
plt.figure(figsize=(8, 6))
plt.plot(x, y)

# Title and labels
plt.title('Plot of $y = x^2$')
plt.xlabel('x')
plt.ylabel('$x^2$')

# Show plot
plt.show()
