import asyncio

async def simulated_network_operation(duration):
    await asyncio.sleep(duration)
    print(f"Operation with duration {duration} seconds is done.")

async def main():
    # Define different durations for the simulated network operations
    durations = [1, 5, 2, 4, 3]

    # Use asyncio.gather to run the coroutines concurrently
    await asyncio.gather(*(simulated_network_operation(duration) for duration in durations))

if __name__ == "__main__":
    asyncio.run(main())
