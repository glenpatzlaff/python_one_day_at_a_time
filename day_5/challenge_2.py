limit = int(input("Find prime numbers up to: "))
number = 2
while number <= limit:
    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(number, "is a prime number.")
    number += 1
