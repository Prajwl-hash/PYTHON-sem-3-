import shutil
import os

# Create a sample directory with files
source_dir = 'source_dir'
os.makedirs(source_dir, exist_ok=True)

with open(os.path.join(source_dir, 'file1.txt'), 'w') as f:
    f.write('This is file 1.')

with open(os.path.join(source_dir, 'file2.txt'), 'w') as f:
    f.write('This is file 2.')

# Copying the directory
destination_dir = 'destination_dir'
shutil.copytree(source_dir, destination_dir)

print(f'Copied {source_dir} to {destination_dir}')
