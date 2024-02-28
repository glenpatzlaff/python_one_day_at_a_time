from functools import reduce

words = ["functional", "programming", "is", "powerful"]
max_value = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(max_value)  # Output: programming
