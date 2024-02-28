import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Make a guess: "))
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1
        if guess < target_number:
            print("Too low.")
        elif guess > target_number:
            print("Too high.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break  # Exit the loop when the guess is correct

        # Optional: Add a way to exit the game early
        if input("Try again? (yes/no): ").lower() != 'yes':
            print(f"The number was {target_number}.")
            break

    # Offer to restart the game
    if input("Play again? (yes/no): ").lower() == 'yes':
        start_game()
    else:
        print("Thanks for playing!")

start_game()
