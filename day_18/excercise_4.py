from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to compute the square of each number
squares = map(lambda x: x**2, numbers)

# Use reduce() to sum up the squares
sum_of_squares = reduce(lambda x, y: x + y, squares)

print(sum_of_squares)
