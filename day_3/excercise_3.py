user_input = input("Enter some text: ")
print("Choose a transformation:\n1. Reverse\n2. Reverse and Uppercase\n3. Reverse and Replace Spaces")
choice = input("Your choice (1, 2, 3): ")

reversed_input = user_input[::-1]

if choice == '1':
    transformed = reversed_input
elif choice == '2':
    transformed = reversed_input.upper()
elif choice == '3':
    transformed = reversed_input.replace(' ', '-')
else:
    transformed = "Invalid choice."

print("Transformed text:", transformed)
