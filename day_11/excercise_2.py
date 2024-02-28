def process_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        print(content)  # Placeholder for actual processing
    except IOError:
        print(f"Failed to read '{filename}'.")
    finally:
        file.close()
        print(f"File '{filename}' is now closed.")

process_file("example.txt")
