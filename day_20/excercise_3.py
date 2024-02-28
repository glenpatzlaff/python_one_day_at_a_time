import itertools

# Creating two lists
list1 = [1, 2, 3]
list2 = ['a', 'b']

# Using itertools.chain() and itertools.cycle() to create an infinite loop over the two lists
chained_cycle = itertools.cycle(itertools.chain(list1, list2))

# Breaking the loop after a specified number of iterations (e.g., 10 iterations)
for i, value in enumerate(chained_cycle, 1):
    print(value)
    if i == 10:
        break
