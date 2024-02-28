def summarize_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            word_count = sum(len(line.split()) for line in lines)
            char_count = sum(len(line) for line in lines)
            print(f"Lines: {len(lines)}, Words: {word_count}, Characters: {char_count}")
    except FileNotFoundError:
        print("File does not exist.")

summarize_text_file('example.txt')
