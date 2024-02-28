def calculate_average(numbers):
    # Bug 1: Division by zero when numbers is empty
    # Bug 2: Incorrect calculation of total_sum
    total_sum = 0
    for number in numbers:
        total_sum += numbers  # This is incorrect
    average = total_sum / len(numbers)
    return average

