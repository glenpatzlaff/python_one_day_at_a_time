import asyncio
import threading
import time

# CPU-bound task: Calculate the nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def run_cpu_bound_task(n):
    print(f"Starting CPU-bound task to calculate Fibonacci({n})")
    result = fibonacci(n)
    print(f"Fibonacci({n}) = {result}")
    return result

# I/O-bound task: Asynchronous sleep
async def io_bound_task(delay):
    print(f"Starting I/O-bound task with a delay of {delay} seconds")
    await asyncio.sleep(delay)
    print(f"Finished I/O-bound task after {delay} seconds")
    return f"Result of I/O-bound task with {delay} seconds delay"

async def main():
    # Number for the Fibonacci calculation and delay for the I/O-bound task
    n = 10
    delay = 5

    # Run the CPU-bound task in a separate thread
    cpu_task = threading.Thread(target=run_cpu_bound_task, args=(n,))
    cpu_task.start()

    # Run the I/O-bound task asynchronously
    io_result = await io_bound_task(delay)

    # Wait for the CPU-bound task to complete
    cpu_task.join()

    print(io_result)

# Run the main coroutine
if __name__ == "__main__":
    asyncio.run(main())
