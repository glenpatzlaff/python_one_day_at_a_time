def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Ended {func.__name__}")
        return result
    return wrapper

@log_call
def say_hello(name):
    print(f"Hello, {name}!")

# Testing the decorated function
say_hello("Alice")
