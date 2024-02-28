students_grades = [("Alice", 58), ("Bob", 76), ("Charlie", 89), ("Diana", 48)]

for student, grade in students_grades:
    result = "passed" if grade >= 60 else "failed"
    print(f"{student} has {result}.")
