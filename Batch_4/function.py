# Write a function for absolute of value
# 10 or -10  --> 10
# SISO
# def absolute_function(num):
#     if num>=0:
#         return num
#     else:
#         return -num
# number_1 =10
# number_2 =-10
# print(absolute_function(number_1))
# print(absolute_function(number_2))
#
# # write a function for square and cube
# # SIMO
# def square_cube(num):
#     return num**2,num**3
# num = 5
# print(square_cube(num))
#
# # write a function for sum of digits
# # MISO
# def add(a,b):
#     return a+b
# number_1=10
# number_2=20
# print(add(number_1,number_2))

# write a function for multiple input and multiple outputs
# def operations(a,b):
#     # if a>b:
#     #     c=(a-b)**2
#     # else:
#     #     c=-(a-b)**2
#     # single line if
#     c= (a-b)**2 if a>b else -(a-b)**2
#     return a**2,b**2,(a+b)**2,c
# print(operations(3,4))
#
# * args , ** kwargs

# default value
# non-default = mandatory

# def calculator(a,b,operation="add"):
#     if operation == "add":
#         return a+b
#     elif operation == "subtract":
#         return a-b
#     if operation == "multiply":
#         return a*b
#     if operation == "divison":
#         return a/b
#
# print(calculator(1,2,"divison"))
# print(calculator(1,2,"multiply"))
# print(calculator(1,2,"add"))
# print(calculator(1,2,"subtract"))
# print(calculator(1,2))

# def addition_2(a,b):
#     return a+b
# def addition_3(a,b,c):
#     return a+b+c
# a=-21
# b=-89
# d=10089
# can't handle for more ouputs redundant and less effective.


def addition(arg1,*argv):
    print(arg1,argv)
    sum = 0
    for element in argv:
        sum = sum+element
    return sum


print(addition(1,2))
print(addition(1,2,3,4))
print(addition(1,2,-2))
print(addition(1,2,54,87,124,154,189,14,142,36))
print(addition(1))


# validating naming conventions
def function(**kwargs):
    sample_dict = {}
    for key, value in kwargs.items():

        mismatch_flag = False
        for letter in kwargs[key]:
            # '7'  ->7
            # 'R'   -->
            if 0<ord(letter)<65 or 91<ord(letter)<97 or 122<ord(letter)<500:
                mismatch_flag = True
        if not mismatch_flag:
            print("Adding, %s == %s" % (key, value))
            sample_dict[key] = value





# Driver code
function(student_1='Raviteja',student_2='Aviteja', student_3='Vaibhav15',
        student_4='Samarth')
