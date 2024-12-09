import shutil
import os

# Create a directory to archive
os.mkdir('example_dir_to_archive')
with open('example_dir_to_archive/file1.txt', 'w') as f:
    f.write('Archivable file.')

# Archive the directory into a zip file
shutil.make_archive('archived_dir', 'zip', 'example_dir_to_archive')
print("Directory archived successfully!")
