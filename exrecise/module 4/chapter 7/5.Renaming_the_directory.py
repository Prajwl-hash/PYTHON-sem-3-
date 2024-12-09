import os

# Create a sample directory to rename

original_dir = 'original_directory'
os.makedirs(original_dir,exist_ok=True)
with open(os.path.join(original_dir,'sample.text'),'w') as f:
    f.write('FIle inside the original directory.')

# Renaming the directory

new_dir = 'renamed_directory'
os.rename(original_dir,new_dir_name)
print(f' Renamed {original_dir} to {new_dir_name}')