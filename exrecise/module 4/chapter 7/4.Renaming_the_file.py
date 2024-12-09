import os

# Create a sample file to rename
with open ('original_file.text','w') as f :
    f.write('This file will be renamed.')

# Rename the file
os.rename('original_file.text','new_file.txt')
print('File renamed from "original_file.text" to "new_file.txt"')