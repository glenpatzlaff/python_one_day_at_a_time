import matplotlib.pyplot as plt
import numpy as np

# Sample data: GDP growth of different countries over 10 years
years = np.arange(2010, 2020)
gdp_usa = [2.6, 1.6, 2.2, 1.8, 2.5, 2.9, 1.6, 2.2, 3.0, 2.3]
gdp_uk = [1.9, 1.5, 0.7, 1.3, 2.9, 2.3, 1.8, 1.4, 1.0, 1.4]
gdp_china = [10.6, 9.5, 7.9, 7.8, 7.3, 7.0, 6.9, 6.7, 6.6, 6.1]
gdp_india = [10.3, 6.6, 5.5, 6.4, 7.4, 8.2, 7.1, 6.7, 6.8, 6.2]

fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Plotting each country's GDP growth
axs[0, 0].plot(years, gdp_usa, 'r-', label='USA')
axs[0, 0].set_title('GDP Growth - USA')
axs[0, 0].set_ylim(0, 12)
axs[0, 0].set_xticks(np.arange(2010, 2021, 2))
axs[0, 0].set_yticks(np.arange(0, 13, 2))

axs[0, 1].plot(years, gdp_uk, 'g-', label='UK')
axs[0, 1].set_title('GDP Growth - UK')
axs[0, 1].set_ylim(0, 12)
axs[0, 1].set_xticks(np.arange(2010, 2021, 2))
axs[0, 1].set_yticks(np.arange(0, 13, 2))

axs[1, 0].plot(years, gdp_china, 'b-', label='China')
axs[1, 0].set_title('GDP Growth - China')
axs[1, 0].set_ylim(0, 12)
axs[1, 0].set_xticks(np.arange(2010, 2021, 2))
axs[1, 0].set_yticks(np.arange(0, 13, 2))

axs[1, 1].plot(years, gdp_india, 'y-', label='India')
axs[1, 1].set_title('GDP Growth - India')
axs[1, 1].set_ylim(0, 12)
axs[1, 1].set_xticks(np.arange(2010, 2021, 2))
axs[1, 1].set_yticks(np.arange(0, 13, 2))

# Customizing each subplot
for ax in axs.flat:
    ax.set(xlabel='Year', ylabel='GDP Growth (%)')
    ax.label_outer()
    ax.grid(True)

plt.tight_layout()
plt.show()
