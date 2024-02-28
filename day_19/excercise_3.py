import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds to execute.")
        return result
    return wrapper

@measure_time
def compute_factorial(n):
    if n == 0:
        return 1
    else:
        return n * compute_factorial(n-1)

# Testing the decorated function with different values of n
print(compute_factorial(5))
print(compute_factorial(10))
print(compute_factorial(15))
