# tuple = we can't change the values once we assign
# tuple immutable data type.

var_1 = ()
print(type(var_1))

var_7 = (1,2,3,4,)
print(var_7)

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
# in-built tuple method
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

print("____________________________________________________________________________________________")

tuple_5 = (9)

for i in range(5):
    tuple_5 = (tuple_5,)  # ((9,),)  (((9,),),)
    print(tuple_5)


def ravi_info_method():
    print("calling some_method")
    # returning multiple inputs (packing)
    return ("Raviteja", 28, "Buchi")

def ravi_info_method_nt():
    print("calling some_method")
    # returning multiple inputs (packing)
    return "Raviteja", 28, "Buchi"

# handling multiple returns and unpacking below.
name, age, location = ravi_info_method()
# checking return type of the method
print(type(ravi_info_method()))
print(f"name: {name}, age: {age}, location: {location}")

# returned 3 values and unpacked only 3 values
name, age, location = ravi_info_method_nt()
# checking return type of the method
print(type(ravi_info_method()))
print(f"name: {name}, age: {age}, location: {location}")
print("_____________________________________________________________________________________________________")

# returned 3 values and unpacked only 2 values
# error: ValueError: too many values to unpack (expected 2)
# name,age = ravi_info_method()


# returned 3 values and unpacked only 1 values
name = ravi_info_method()
print(name)


# returned n --> unpacking 1 value(assign returned values as tuple) or n values(assign returned values individually)