import os

file_name = 'example.txt'
directory = 'Documents'
full_path = os.path.join(directory,file_name )

if os.path.exists(full_path):
    print(f"{full_path} exists.")
else:
    print(f"{full_path} does not exist.")