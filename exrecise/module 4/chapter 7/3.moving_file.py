import shutil
import os

with open ('file_to_move','w') as f:
    f.write('This fill will be moved.')

os.makedirs('destination_dir', exist_ok=True)


shutil.move('file_to_move', 'destination_dir/file_to_move.txt')
print('File moved to "destination_dir/file_to_move.txt".')