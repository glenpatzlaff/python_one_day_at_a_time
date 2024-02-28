questions = [
    "1. What is the capital of France?\nA. London\nB. Berlin\nC. Paris\nD. Madrid",
    "2. Which language is primarily used for Android development?\nA. Java\nB. Swift\nC. Kotlin\nD. Ruby",
    "3. What does HTML stand for?\nA. Hyper Trainer Marking Language\nB. Hyper Text Markup Language\nC. Hyper Texts Markets Language\nD. None of the above"
]

answers = ['C', 'C', 'B']  # Correct answers

score = 0  # Initialize score

for i in range(len(questions)):
    print(questions[i])  # Display the question
    user_answer = input("Enter your answer (A/B/C/D): ").upper()  # Get user answer

    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print(f"You scored {score} out of {len(questions)}.")

# Provide different feedback based on the score
if score == len(questions):
    print("Excellent! You got all questions right!")
elif score >= len(questions) / 2:
    print("Good job! You've passed the quiz.")
else:
    print("You didn't pass this time. Keep studying and try again!")
