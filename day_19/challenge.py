def cache(func):
    memo = {}
    def wrapper(n):
        if n in memo:
            return memo[n]
        else:
            result = func(n)
            memo[n] = result
            return result
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Testing the performance improvement
import time

# Without the decorator
def fibonacci_plain(n):
    if n <= 1:
        return n
    else:
        return fibonacci_plain(n-1) + fibonacci_plain(n-2)

start_time = time.time()
fibonacci_result = fibonacci(30)  # With caching
end_time = time.time()
print(f"With caching: Fibonacci(30) = {fibonacci_result}, took {end_time - start_time:.6f} seconds.")

start_time_plain = time.time()
fibonacci_result_plain = fibonacci_plain(30)  # Without caching
end_time_plain = time.time()
print(f"Without caching: Fibonacci(30) = {fibonacci_result_plain}, took {end_time_plain - start_time_plain:.6f} seconds.")
