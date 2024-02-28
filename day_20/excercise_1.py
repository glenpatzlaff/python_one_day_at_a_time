def countdown(start):
    while start >= 0:
        yield start
        start -= 1

# Testing the generator function
for number in countdown(5):
    print(number)
