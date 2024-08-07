#. Write a python program to print the contents of a directory using the os module.
#Search online for the function which does that.

import os

def print_directory_contents(path='.'):
    try:
        # List all files and directories in the specified path
        contents = os.listdir(path)
        
        print(f"Contents of directory '{path}':")
        for item in contents:
            print(item)
    except Exception as e:
        print(f"Error: {e}")

# Specify the path of the directory you want to list
directory_path = '.'  # Current directory
print_directory_contents(directory_path)
