user_input = input("Enter an integer: ")
while not user_input.isdigit():
    print("That's not an integer!")
    user_input = input("Enter an integer: ")
print(f"Thank you for entering the integer: {user_input}")
