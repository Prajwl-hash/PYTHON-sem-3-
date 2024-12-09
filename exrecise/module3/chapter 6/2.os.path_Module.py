<<<<<<< HEAD
import os

file_name = 'example.txt'
directory = 'Documents'
full_path = os.path.join(directory,file_name )

if os.path.exists(full_path):
    print(f"{full_path} exists.")
else:
=======
import os

file_name = 'example.txt'
directory = 'Documents'
full_path = os.path.join(directory,file_name )

if os.path.exists(full_path):
    print(f"{full_path} exists.")
else:
>>>>>>> c965dbf5152de176c2dbd9448cc71dbd01538425
    print(f"{full_path} does not exist.")