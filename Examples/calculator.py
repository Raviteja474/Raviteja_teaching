import time

import pylint


# BODMAS Brackets Order Division Multiplication Addition subtraction
# 2*3+4-5*(7+9)-11  = 2*3+4-5*16-11 = 6+4-80-11 =10-80-11 = -81
# This illustrates string and functions concepts
# Aim: simple and complex calculations
# exec function
# Modulaity, atomosity, reusability, maintainability



# raw_string

# ASCII(4 bytes , 32 bits, 2**32 bits, ) unicode(8 bytes)
# Unicode was created to allow more character sets than ASCII.
# print avinash in telugu

# From that string , take out 2 values
# split is builtin
# values = input("Enter your values?")
# a,b,c = values.split(",")
# print(a,b)

# Make addition as default operation, if user don't provide operation name
# values mandatory argument and operation default argument
def extract_operation(values, operation = "addition"):
    value_1, value_2 = values.split(" ")
    return value_1,value_2,operation


def addition(a,b):
    print("This is addition.")
    return a+b

def subtraction(a,b):
    print("This is subtraction.")
    return a-b

def multiplication(a,b):
    print("This is multiplication.")
    return a*b

def division(a,b):
    print("This is division.")
    if b == 0:
        print("Please don't enter divisor as 0.")
    else:
        return a/b


starting_time = time.time()
# Infinite loop which runs forever and terminates only when break happens
while True:
    values = input("Enter your first two values followed by name of the operation?")
    # There are 2 breks , 1 will close program when we type I am done and second will close calculator for every 1 min
    if "I am done" in values:
        print("Closing the calculator!!!")
        break
    if time.time()-starting_time > 60:
        print("Calculator works only 1 minute!!")
        break

    if len(values.split(" ")) > 2:
        value_1, value_2, operation = values.split(" ")
    else:
        value_1, value_2, operation = extract_operation(values)
    print(value_1, value_2, operation)
    print(type(value_1), type(value_2), type(operation))

    # type casting, changing from one type to another type , here from str to int
    value_1 = int(value_1)
    value_2 = int(value_2)
    print(type(value_1), type(value_2), type(operation))

    # changing to lowercase irrespective of the case provide by user.
    # This treats Addition, addition , AddITION, adDITION same as everything converted to lowercase "addition".
    operation = operation.lower()

    # perform unit testing for this.
    if operation == "addition":
        print(addition(value_1,value_2))

    elif operation == "subtraction":
        print(subtraction(value_1, value_2))

    elif operation == "multiplication":
        print(multiplication(value_1, value_2))

    elif operation == "division":
        print(division(value_1, value_2))

    else:
        print("Hey man!!!!  It's wrong operation.")
