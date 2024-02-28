import os

def add_log_entry(entry, file_path='log.txt'):
    mode = 'a' if os.path.exists(file_path) else 'w'
    with open(file_path, mode) as file:
        file.write(entry + "\n")

add_log_entry("Log entry 1")
