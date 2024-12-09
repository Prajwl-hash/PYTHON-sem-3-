import shutil
import os

# Create a directory with files
os.mkdir('example_dir')
with open('example_dir/file1.txt', 'w') as f:
    f.write('File 1 content.')
with open('example_dir/file2.txt', 'w') as f:
    f.write('File 2 content.')

# Copy the directory
shutil.copytree('example_dir', 'example_dir_copy')
print("Directory copied successfully!")
