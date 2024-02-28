numbers = [1, 2, 3, 4, 5]
even_squares = (num**2 for num in numbers if num % 2 == 0)

for square in even_squares:
    print(square)
