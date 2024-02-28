import time
from functools import wraps

def rate_limiter(max_calls, time_window):
    calls = []

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            current_time = time.time()
            # Remove expired calls
            calls = [call for call in calls if current_time - call < time_window]

            if len(calls) < max_calls:
                calls.append(current_time)
                return func(*args, **kwargs)
            else:
                print("Rate limit exceeded. Try again later.")
        return wrapper
    return decorator

@rate_limiter(max_calls=3, time_window=10)
def mock_api_endpoint(user_id):
    print(f"API called successfully for user {user_id}")

for _ in range(5):
    mock_api_endpoint(123)
    time.sleep(1)
