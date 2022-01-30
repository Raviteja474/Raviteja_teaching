import os

pattern = "19@@"
LOCATION = r'C:\Users\ravit\Desktop\Teaching\Raviteja_teaching'
# List to store all
# directories
L = []

# Traversing through Test
for root, dirs, files in os.walk(LOCATION):
    # Adding the empty directory to
    # list
    L.append((root, dirs, files))
    print("_________________________________________")
    # L.extend((root, dirs, files))
    # print("_________________________________________")

print("List of all sub-directories and files:")
for i in L:
    print(i)