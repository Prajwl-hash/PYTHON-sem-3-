import shutil
import os

# Create a directory with files
os.mkdir('example_dir_to_delete')
with open('example_dir_to_delete/file1.txt', 'w') as f:
    f.write('Temporary file.')

# Delete the directory
shutil.rmtree('example_dir_to_delete')
print("Directory deleted successfully!")
