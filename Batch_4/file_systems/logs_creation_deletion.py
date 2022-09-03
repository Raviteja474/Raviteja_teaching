import logging
import time
import os

# create a log file in folder 1 --> minute 1
# create a log file in folder 2  --> minute 2
# delete it after a minute
current_dir = os.getcwd()
folder_tobe_added_1 = 'folder1'
folder_tobe_added_2 = 'folder2'
path_1 = os.path.join(current_dir, folder_tobe_added_1)

if not os.path.exists(path_1):
    os.mkdir(path_1)
    print(f"path created {path_1}")
else:
    print(f"path existed {path_1}, no need to create")

path_2 = os.path.join(current_dir, folder_tobe_added_2)
if not os.path.exists(path_2):
    os.mkdir(path_2)
    print(f"path created {path_2}")
else:
    print(f"path existed {path_2}, no need to create")

# concatenation
# logging.basicConfig(level=logging.DEBUG,
#                     filename=path+str(time.time())+r'.txt', filemode='a')
# D:\Raviteja_teaching\Batch_4\file_systems\folder11662176689.8834615.txt
# which is not our expectation
# important of os.path.join
logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.join(path_1,str(time.time())+r'.txt'), filemode='a')
start_time = time.time()
while time.time()-start_time<15:
    logging.info("My print statement1")
# PermissionError: [WinError 32] The process cannot access the file
# because it is being used by another process:
# iterations
# dummy assert 4==5
# os.close(file)


logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.join(path_2,str(time.time())+r'.txt'), filemode='a')
start_time = time.time()
while time.time()-start_time<15:
    logging.info("My print statement2")

time.sleep(15)
# "The directory is not empty:" --> not helpful with contents
# os.rmdir(path_1)

file_names = os.listdir(path_1)
filelist = [ file_name for file_name in file_names if file_name.endswith(".txt")]
for file in filelist:
    os.remove(os.path.join(path_1, file))

file_names = os.listdir(path_2)
filelist = [file_name for file_name in file_names if file_name.endswith(".txt")]
for file in filelist:
    os.remove(os.path.join(path_2, file))


