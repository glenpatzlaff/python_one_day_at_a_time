import threading
import time

# Define three separate functions
def print_numbers_function1():
    for i in range(1, 6):
        print(f"Function 1: {i}")
        time.sleep(1)

def print_numbers_function2():
    for i in range(1, 6):
        print(f"Function 2: {i}")
        time.sleep(1)

def print_numbers_function3():
    for i in range(1, 6):
        print(f"Function 3: {i}")
        time.sleep(1)

# Create threads for each function
thread1 = threading.Thread(target=print_numbers_function1)
thread2 = threading.Thread(target=print_numbers_function2)
thread3 = threading.Thread(target=print_numbers_function3)

# Start the threads
thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to complete
thread1.join()
thread2.join()
thread3.join()

print("All threads have completed.")
