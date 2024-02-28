def write_user_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    occupation = input("Enter your occupation: ")

    with open('user_info.txt', 'w') as file:
        file.write(f"Name: {name}\nAge: {age}\nOccupation: {occupation}")


write_user_info()
