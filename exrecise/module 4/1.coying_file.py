import shutil

# Create a file and write something to it
with open('example.txt', 'w') as f:
    f.write('This is an example file.')

# Copy the file to a new location
shutil.copy('example.txt', 'example_copy.txt')
print("File copied successfully!")
