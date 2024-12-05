import os

old_name = input("Enter the current file name: ")
new_name = input("Enter the new file name: ")

os.rename(old_name, new_name)
print("File renamed successfully!")
