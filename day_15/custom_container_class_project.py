class CustomList:
    def __init__(self, initial_data=None):
        self._data = initial_data if initial_data is not None else []

    def extend(self, iterable):
        for item in iterable:
            self._data.append(item)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __str__(self):
        return str(self._data)

    def add(self, item):
        self._data.append(item)

    # Alternatively, use magic method for '+=' operator
    def __iadd__(self, other):
        if isinstance(other, (list, CustomList)):
            self.extend(other)
        else:
            self.add(other)
        return self

# Creating and using the CustomList
my_list = CustomList([1, 2, 3])
print(my_list)  # Output: [1, 2, 3]

# Indexing
print(my_list[0])  # Output: 1

# Adding elements
my_list.add(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Extending with another list
my_list.extend([5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Using '+=' operator
my_list += [7, 8]
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Iteration
for item in my_list:
    print(item, end=' ')  # Output: 1 2 3 4 5 6 7 8
