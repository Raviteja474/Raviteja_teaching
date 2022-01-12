# shutil.copy() method in Python is used to copy the content of the source file to the destination file or directory.
# It also preserves the file’s permission mode but other metadata of the file like the file’s creation and
# modification times is not preserved.
import shutil


source = r'C:\Users\ravit\Desktop\Teaching\Raviteja_teaching\raviteja/avi.txt'
destination = r'C:\Users\ravit\Desktop\Teaching\Raviteja_teaching\raviteja2'
# Copy the content of
# source to destination
# don't preservers metadata
# dest = shutil.copy(source, destination)
# preservers metadata(created, file permissions)
dest = shutil.copy2(source, destination)

# Print path of newly
# created file
print("Destination path:", dest)

# print
# # MULITPLE FILES
source = r'C:\Users\ravit\Desktop\Teaching\Raviteja_teaching\raviteja'
destination = r'C:\Users\ravit\Desktop\Teaching\Raviteja_teaching\raviteja2'
# Copy the content of  source to destination
# FileExistsError: [WinError 183]
shutil.rmtree(destination)
dest = shutil.copytree(source, destination)

# Print path of newly
# created file
print("Destination path:", dest)
