import random

def retry(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Exception caught: {e}. Retrying...")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@retry(3)
def unreliable_operation():
    if random.randint(0, 1) == 0:
        raise ValueError("Random failure!")
    return "Success"

# Testing the decorated function
for _ in range(5):
    print(unreliable_operation())
