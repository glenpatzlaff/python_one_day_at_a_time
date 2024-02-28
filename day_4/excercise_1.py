password = input("Enter your password: ")

if len(password) < 8:
    print("Password must be at least 8 characters long.")
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one digit.")
elif password.islower() or password.isupper():
    print("Password must contain both uppercase and lowercase characters.")
else:
    print("Password is valid.")
