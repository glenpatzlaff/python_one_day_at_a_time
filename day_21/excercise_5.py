import threading

# Shared resource
shared_list = []

# Lock for synchronizing access to the shared resource
lock = threading.Lock()

# Function that modifies the shared resource
def modify_shared_list(item):
    global shared_list
    with lock:
        print(f"Adding {item} to the list...")
        shared_list.append(item)
        print(f"List now: {shared_list}")

# Creating threads that modify the shared list
threads = [threading.Thread(target=modify_shared_list, args=(i,)) for i in range(5)]

# Starting the threads
for thread in threads:
    thread.start()

# Waiting for all threads to complete
for thread in threads:
    thread.join()

print("Final state of shared list:", shared_list)
