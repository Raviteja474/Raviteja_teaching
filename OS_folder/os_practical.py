# problem create in raviteja folder raviteja.txt file in one level above this directory
#C:\Users\ravit\Desktop\Teaching\Raviteja_teaching\OS_folder\os_practical.py
# create C:\Users\ravit\Desktop\Teaching\Raviteja_teaching/raviteja.txt
import platform
import os
import shutil
# present directory
cwd = os.getcwd()
print(cwd)

# changing directory to given value, here on our operations will effect in this directory
os.chdir(r'C:\Users\ravit\Desktop\Teaching\Raviteja_teaching')
# alternate to go one level above this directory
#os.chdir('../')

cwd = os.getcwd()
print(cwd)


# before creating folder using mkdir first you should be in that working directory using chdir
# this relative path
# os.mkdir(r'raviteja')

# absolute path
if os.path.exists(r'C:\Users\ravit\Desktop\Teaching\Raviteja_teaching\raviteja'):
    print("File already exist, no need to create.")
else:
    os.mkdir(r'C:\Users\ravit\Desktop\Teaching\Raviteja_teaching\raviteja')
    print("raviteja folder created.")

# FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'raviteja'

# create 5 text files mahesh.txt, avi.txt, visu.txt, bharath.txt, sumanth.txt
# you can append file names like below but not recommendable
#file_name= r'C:\Users\ravit\Desktop\Teaching\Raviteja_teaching\raviteja'+"/mahesh.txt"

# paramater 1 folder in which you want to create and second param is file name
file_name = os.path.join(r'C:\Users\ravit\Desktop\Teaching',
                         r'Raviteja_teaching\raviteja','mahesh_1.txt',)
print(file_name)
with open(file_name,"w+") as f:
     pass
print("_____________________________________________________________________________")
file_directory = r'C:\Users\ravit\Desktop\Teaching\Raviteja_teaching\raviteja'
file_names = [r'mahesh.txt', r'avi.txt', r'visu.txt', r'bharath.txt', r'sumanth.txt']

# for file in range(len(file_names))
for file in file_names:
    #forms eg: C:\Users\ravit\Desktop\Teaching\Raviteja_teaching\raviteja\mahesh.txt
    file_create = os.path.join(file_directory,file)
    # will this exist #forms eg: C:\Users\ravit\Desktop\Teaching\Raviteja_teaching\raviteja\mahesh.txt
    if not os.path.isfile(file_create):
        with open(file_create,"w+") as f:
            print(f"{file_create} created.")
    else:
        print(f"{file_create} already exist")

print("Printing all files.")
dir_list = os.listdir(r'C:\Users\ravit\Desktop\Teaching\Raviteja_teaching')
print(dir_list)

for item in dir_list:
    print(f"__________\nchecking ...{item}")
    if not os.path.isfile(item):
        print(f"{item} I am folder")
    else:
        print(f"{item} I am file\n")

#os.path.exists("") file/folder it will whether exist or not.
#os.path.isfile("") returns true of a file exist

# os.remove() it removes folder.
# os.rmdir() it removes file.
# FileNotFoundError: [WinError 2] The system cannot find the file specified: 'C:\\Users\\ravit\\Desktop\\Teaching\\Raviteja_teaching\\raviteja\\mahesh_21.txt'

os.remove(r'C:\Users\ravit\Desktop\Teaching\Raviteja_teaching\raviteja\mahesh.txt')
try:
    os.rmdir(r'C:\Users\ravit\Desktop\Teaching\Raviteja_teaching\raviteja/')
except Exception as e:
    print(e)
    # [WinError 145] The directory is not empty: 'C:\\Users\\ravit\\Desktop\\Teaching\\Raviteja_teaching\\raviteja/'

size = os.path.getsize(r'C:\Users\ravit\Desktop\Teaching\Raviteja_teaching\raviteja\avi.txt')
print(f"avi file size is {size}")
print(os.name)
print(platform.system())


# 19@@ os.walk()
