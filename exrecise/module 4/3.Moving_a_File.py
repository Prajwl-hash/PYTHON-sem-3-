import shutil
import os

# Create a file
with open('example_move.txt', 'w') as f:
    f.write('This file will be moved.')

# Move the file to a different location
shutil.move('example_move.txt', 'new_example_move.txt')
print("File moved successfully!")
