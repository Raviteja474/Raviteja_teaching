import array as arr

# List occupies much more memory as every node defined the List has its own memory set whereas Arrays are memory-efficient
# data structure

a = arr.array('i', [1, 2, 3])

# printing original array
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()

# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])



# printing original array
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")

# 19@@
# val= arr.array('u', ["thili", "gfgfdg"])
my_array = arr.array("u","thili")
print(my_array)