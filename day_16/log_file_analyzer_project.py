import re

def parse_log(log_line):
    pattern = r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}), (?P<level>\w+), (?P<message>.+). IP: (?P<ip>\d+\.\d+\.\d+\.\d+)'
    match = re.match(pattern, log_line)
    if match:
        return match.groupdict()
    else:
        return None

def filter_logs(logs, level=None, ip=None):
    filtered_logs = []
    for log in logs:
        if level and log['level'] != level:
            continue
        if ip and log['ip'] != ip:
            continue
        filtered_logs.append(log)
    return filtered_logs


def analyze_log(file_path, level=None, ip=None):
    with open(file_path, 'r') as file:
        log_lines = file.readlines()

    parsed_logs = [parse_log(line.strip()) for line in log_lines if parse_log(line.strip())]
    filtered_logs = filter_logs(parsed_logs, level, ip)

    return filtered_logs


# Example usage
log_file_path = 'sample.log'
error_logs = analyze_log(log_file_path, level='ERROR')
print("Error Logs:")
for log in error_logs:
    print(log)

def summarize_errors(logs):
    error_summary = {}
    for log in logs:
        message = log['message']
        error_summary[message] = error_summary.get(message, 0) + 1
    return error_summary

# Summarize error messages
error_logs = analyze_log(log_file_path, level='ERROR')
error_summary = summarize_errors(error_logs)
print("\nError Summary:")
for error, count in error_summary.items():
    print(f"{error}: {count} times")
