import os

# Create a directory
os.mkdir('example_dir_to_rename')
# Rename the directory
os.rename('example_dir_to_rename', 'renamed_dir')
print("Directory renamed successfully!")