import time
import random

def data_stream():
    """Simulate a stream of data."""
    while True:
        yield {'timestamp': time.time(), 'value': random.randint(1, 100)}
        time.sleep(0.1)

def filter_data(stream):
    """Filter data points with values greater than 50."""
    for data_point in stream:
        if data_point['value'] > 50:
            yield data_point

def moving_average(stream, window_size=5):
    """Calculate the moving average over a window of data points."""
    values = []
    for data_point in stream:
        values.append(data_point['value'])
        if len(values) > window_size:
            values.pop(0)
        data_point['moving_avg'] = sum(values) / len(values)
        yield data_point

from itertools import islice

def batch(stream, batch_size=10):
    """Batch data points into chunks."""
    iterator = iter(stream)
    while True:
        batch = list(islice(iterator, batch_size))
        if not batch:
            break
        yield batch

stream = data_stream()
filtered_stream = filter_data(stream)
averaged_stream = moving_average(filtered_stream)
batched_stream = batch(averaged_stream)

for batch in batched_stream:
    print(batch)
    # Add aggregation logic here, e.g., summing the moving averages.

def aggregate_batches(batches):
    """Aggregate batches by summing their moving averages."""
    for batch in batches:
        aggregate = sum(data_point['moving_avg'] for data_point in batch)
        print(f"Batch Aggregate: {aggregate}")

# Apply the aggregation function to our batched stream.
aggregate_batches(batched_stream)
