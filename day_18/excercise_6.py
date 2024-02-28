from functools import reduce

strings = ["Python", "functional", "programming", "is", "awesome"]
concatenated = reduce(lambda x, y: x + ' ' + y, strings)
print(concatenated)  # Output: 'Python functional programming is awesome'
