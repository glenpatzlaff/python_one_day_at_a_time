matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
search_value = 5
found = False

for row in matrix:
    if search_value in row:
        found = True
        break

if found:
    print(f"{search_value} found in the matrix.")
else:
    print(f"{search_value} not found in the matrix.")
