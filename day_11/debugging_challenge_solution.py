# Fixed version
def calculate_average(numbers):
    assert len(numbers) > 0, "The list cannot be empty."  # Handling Bug 1
    total_sum = sum(numbers)  # Correcting Bug 2
    average = total_sum / len(numbers)
    return average
