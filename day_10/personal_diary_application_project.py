import datetime
import os

def add_diary_entry():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"diary_{timestamp}.txt"
    content = input("Write your diary entry:\n")
    with open(filename, 'w') as file:
        file.write(content)
    print("Diary entry saved.")

def list_diary_entries():
    for filename in os.listdir('.'):
        if filename.startswith("diary_"):
            print(filename)

def read_diary_entry(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("Entry does not exist.")

def run_diary_app():
    while True:
        action = input("Choose an action: [1] Add Entry [2] List Entries [3] Read Entry [4] Exit\n")
        if action == "1":
            add_diary_entry()  # or add_diary_entry_single_file()
        elif action == "2":
            list_diary_entries()  # No equivalent needed for single file approach
        elif action == "3":
            filename = input("Enter the filename of the entry to read: ")
            read_diary_entry(filename)  # Use read_all_entries() for single file approach
        elif action == "4":
            break
        else:
            print("Invalid action.")

run_diary_app()
