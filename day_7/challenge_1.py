temperatures_f = [68, 70, 74, 75, 71, 69, 72]

# Convert to Celsius
temperatures_c = [(f - 32) * 5/9 for f in temperatures_f]

# Calculate average
average_temp = sum(temperatures_c) / len(temperatures_c)

print(f"Average temperature for the week: {average_temp:.2f}°C")
