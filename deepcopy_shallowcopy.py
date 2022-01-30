# a=[1,2]
#
# b=a
#
# print(a)
# print(b)
#
# print(id(a))
# print(id(b))
#
# b= a[:]
#
# print(id(a))
# print(id(b))

# 19@@
import copy
#
# a= 10
# b=copy.copy(a)
# b=11
# print(a)
#
#
# a= 10
# b=copy.deepcopy(a)
# b=11
# print(a)


# Python code to demonstrate copy operations

# importing "copy" for copy operations
import copy

# initializing list 1
li1 = [1, 2, [3,5], 4]

# using deepcopy to deep copy
# copy : changes on duplicate is reflcted on original list
#deepcopy: changes on duplicate is not reflcted on original list
li2 = copy.copy(li1)

# original elements of list
print ("The original elements before deep copying")
for i in range(0,len(li1)):
	print (li1[i],end=" ")

print("\r")

# adding and element to new list
li2[2][0] = 7

# Change is reflected in l2
print ("The new list of elements after deep copying ")
for i in range(0,len( li1)):
	print (li2[i],end=" ")

print("\r")

# Change is NOT reflected in original list
# as it is a deep copy
print ("The original elements after deep copying")
for i in range(0,len( li1)):
	print (li1[i],end=" ")
