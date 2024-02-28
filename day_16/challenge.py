import re

log_entry = "2021-05-01 14:33:45, INFO, Application started successfully."

pattern = r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}), (?P<level>INFO|ERROR|DEBUG), (?P<message>.*)'

match = re.search(pattern, log_entry)
if match:
    print(f"Timestamp: {match.group('timestamp')}")
    print(f"Level: {match.group('level')}")
    print(f"Message: {match.group('message')}")
