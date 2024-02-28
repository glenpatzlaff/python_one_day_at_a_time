import os

def cleanup_directory(directory, extension='.tmp'):
    files_removed = 0
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            os.remove(os.path.join(directory, filename))
            files_removed += 1
    print(f"Removed {files_removed} files.")

cleanup_directory('/path/to/directory')
