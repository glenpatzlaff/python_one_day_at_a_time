import matplotlib.pyplot as plt
import numpy as np

# I'll choose the histogram of random data from the 2x2 subplot layout and add annotations for the maximum and minimum values.

# Generate random data
data_hist = np.random.randn(1000)
# Determine the bin edges and histogram data
counts, bins, patches = plt.hist(data_hist, bins=30, color='green', edgecolor='black')

# Calculate the bin centers to identify where to put the annotations
bin_centers = 0.5 * (bins[:-1] + bins[1:])

# Find the maximum and minimum bin heights
max_count = np.max(counts)
min_count = np.min(counts)
max_bin = bin_centers[counts == max_count][0]
min_bin = bin_centers[counts == min_count][0]

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(data_hist, bins=30, color='green', edgecolor='black')

# Add annotations
plt.annotate('Maximum', xy=(max_bin, max_count), xytext=(max_bin, max_count+20),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

plt.annotate('Minimum', xy=(min_bin, min_count), xytext=(min_bin, min_count+20),
             arrowprops=dict(facecolor='red', shrink=0.05),
             horizontalalignment='center')

# Customize the plot
plt.title('Histogram of Random Data with Annotations')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show plot
plt.show()
