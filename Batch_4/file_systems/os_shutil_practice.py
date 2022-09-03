import os
import logging

cwd = os.getcwd()
print("Current working directory:", cwd)

os.chdir('../')
cwd = os.getcwd()
print("Current working directory:", cwd)

os.chdir('../')
cwd = os.getcwd()
print("Current working directory:", cwd)

# hardcoding directory
os.chdir(r'D:\Raviteja_teaching\Batch_4\resumes')
cwd = os.getcwd()
print("Current working directory:", cwd)