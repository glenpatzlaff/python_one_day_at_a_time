import time

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Ended {func.__name__}")
        return result
    return wrapper

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds to execute.")
        return result
    return wrapper

@log_call
@measure_time
def process_data(data):
    print(f"Processing {data}...")
    time.sleep(2)  # Simulating a delay
    print("Processing complete.")

# Testing the decorated function
process_data("sample data")
