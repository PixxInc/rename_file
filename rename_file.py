import os
import sys

def rename_file(file_path, new_name):
    try:
        # Extract the directory from the file path
        directory = os.path.dirname(file_path)

        # Get the original file extension
        extension = os.path.splitext(file_path)[1]

        # Construct the new file path
        new_file_path = os.path.join(directory, new_name + extension)

        # Rename the file
        os.rename(file_path, new_file_path)
        print(f"File renamed to: {new_file_path}")
    except OSError as e:
        print(f"OS Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python rename_file.py \"<file_path>\" \"<new_name>\"")
        sys.exit(1)

    # Use arguments safely with quotes if needed
    file_path = sys.argv[1].strip("\"")
    new_name = sys.argv[2].strip("\"")
    
    rename_file(file_path, new_name)
