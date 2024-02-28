from itertools import groupby


def group_consecutive(lst):
    # Function to calculate the difference between each number and its index
    # This helps in grouping consecutive numbers together
    key_func = lambda x: x[1] - x[0]

    # Pairing each number with its index
    indexed_lst = list(enumerate(lst))

    # Using groupby with the key function to group consecutive numbers
    grouped = [list(map(lambda x: x[1], group)) for key, group in groupby(indexed_lst, key_func)]

    return grouped


# Example list
lst = [1, 2, 3, 5, 6, 8, 9, 10]

# Grouping consecutive integers
grouped_consecutive = group_consecutive(lst)
print(grouped_consecutive)
