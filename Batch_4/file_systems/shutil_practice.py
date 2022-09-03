import shutil
import os

source = r'D:\Raviteja_teaching\Batch_4\file_systems\logs_creation_deletion.py'

destination_1 = r'D:\Raviteja_teaching\Batch_4\file_systems\folder1'
destination_2 = r'D:\Raviteja_teaching\Batch_4\file_systems\folder2'

dest_1 = shutil.copy(source, destination_1)

dest_2 = shutil.copy2(source, destination_2)

matadata = os.stat(destination_1)
print(matadata)

# file --> direcory
# file --> file

# copytree
# direcory--> directory
