import matplotlib.pyplot as plt
import numpy as np

# Change plot style
plt.style.use('ggplot')

# Generate data for line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Generate data for scatter plot
x_scatter = np.random.rand(50) * 10
y_scatter = np.sin(x_scatter) + np.random.normal(0, 0.1, 50)
colors = x_scatter  # Color by position

# Create line plot
plt.plot(x, y, label='Sine Wave')

# Create scatter plot with colormap
scatter = plt.scatter(x_scatter, y_scatter, c=colors, cmap='viridis', label='Data Points')

# Customize tick labels
plt.xticks(ticks=np.arange(0, 11, 2), labels=[f"{i}π" for i in range(6)])
plt.yticks(ticks=np.linspace(-1, 1, 5), labels=[f"{i} units" for i in np.linspace(-1, 1, 5)])

# Add colorbar for scatter plot
plt.colorbar(scatter, label='Position')

# Add custom legend
plt.legend(title='Legend', loc='upper right')

# Add titles and labels
plt.title('Advanced Customization Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()
