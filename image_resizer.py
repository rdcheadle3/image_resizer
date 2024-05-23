import os

def print_files_in_dir(directory):
    print("Checking directory...")  # Debug statement
    if not os.path.exists(directory):
        print(f"Directory does not exist: {directory}")
    else:
        print(f"Directory exists: {directory}")
        files = os.listdir(directory)
        print(f"Files in directory: {files}")

if __name__ == "__main__":
    print("Script is running...")  # Debug statement
    directory = "/home/rcheadle/workspace/github.com/rdcheadle3/image_resizer/tools/"  # Replace with your directory path
    print_files_in_dir(directory)
    print("Script completed.")  # Debug statement
