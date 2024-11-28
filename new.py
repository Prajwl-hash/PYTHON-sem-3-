import os
import shutil


def move_file(src, dst):
    try:
        # Check if the source file exists
        if not os.path.isfile(src):
            print(f"Source file '{src}' does not exist.")
            return

        # Copy the file
        shutil.move(src, dst)
        print(f"File '{src}' copied to '{dst}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
source_path = r'4=D:\GCU\3rd sem\python\module 1\PYTHON_ASSIGNMENT (Module 1 chapter 1).pdf'  # Replace with your source file path
destination_path = r'D:\GCU\3rd sem\python\module 2'  # Replace with your destination file path

move_file(source_path, destination_path)