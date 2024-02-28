P = 1000  # Principal amount
r = 0.05  # Annual interest rate (as a decimal)
n = 4     # Compounded quarterly
t = 5     # Time in years

A = P * (1 + r/n)**(n*t)
print(f"The amount after {t} years is: ${A:.2f}")
