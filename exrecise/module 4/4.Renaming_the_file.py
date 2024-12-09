import os

# Create a file
with open('example_rename.txt', 'w') as f:
    f.write('This file will be renamed.')

# Rename the file
os.rename('example_rename.txt', 'renamed_file.txt')
print("File renamed successfully!")
