# tuple = we can't change the values once we assign
# tuple immutable data type.

var_1 = ()
print(type(var_1))

# not recommendable
var_4 = ("Ravi")
print(var_4)
print(len(var_4))
print(var_4[2])

# close tuple with , always
var_2 = ("Ravi",)
print(var_2)
print(len(var_4))
print(var_2[0])


list_1 = [1, 2, 3, 4, 5]
var_3 = tuple(list_1)
print(var_3)

# immutable we can't change the values once we assign.
# var_2[0] = "Bhaarath"

# when you try to change total tuple value, it will support but when you try to change individual element it will not support.
var_2 = ("Bharath", "Nellore", 24)
print(var_2)

sample_string = "Visu"
# String immutability concept TypeError: 'str' object does not support item assignment
# to replace i with j
# sample_string[1] = 'j'
# print(sample_string)

sample_string = "Avinash"
print(sample_string)
print("____________________________________________________________________________________________")
list_1 = [1,2,3,4]
print(hex(id(sample_string)))
list_1[2]=66
print(hex(id(sample_string)))
print("____________________________________________________________________________________________")
# id() method returns memory location
sample_string = "Visu"
print(hex(id(sample_string)))
sample_string = sample_string.replace('i','j')
print(sample_string)
print(hex(id(sample_string)))

# ____________________________________________________________________________________________
# 0x2a614960230
# 0x2a614960230
# ____________________________________________________________________________________________
# 0x2a6149601f0
# Vjsu
# 0x2a614960370

# using tuples in tuples
tup_1 = (1,2,3)
tup_2 = tup_1*3
tup_3 = tup_1+tup_1
print(tup_2)
print(tup_3)
