def accumulator():
    total = 0
    while True:
        add_value = yield total
        if add_value is not None:
            total += add_value

# Creating the generator and starting it
acc = accumulator()
next(acc)  # Prime the generator

# Example interaction
print(acc.send(5))  # Output: 5
print(acc.send(10))  # Output: 15
