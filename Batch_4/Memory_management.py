# heap
# PVM = python packages
# garbage collection
# 19@@ -Raviteja
# GIL -multithreading
# id function --> unique id for the specified object

# https://scoutapm.com/blog/python-memory-management#:~:text=Heap%20memory,-All%20objects%20and&text=When%20a%20variable%20is%20created,by%20all%20your%20program's%20methods.

# stack = function statement, fast, continuous , local variable
# heap = objects,  slow, dynamic , global variable
a=10
b=a
print(id(a))
print(id(b))
print("*"*80)
b=11
print(id(b))
a=12
print(id(a))
print("*"*80)

# import random
# import time
# while True:
#     OTP = random.randrange(100000, 999999)
#     time.sleep(0.5)
#     print(f"Generating OTP {OTP}")

# a= 10
# b=10
# print(a==b)
# print(id(a))
# print(id(b))
# if a is b:
#     print("is")
#
# if id(a) == id(b):
#     print("id")
# if a == b:
#     print("==")

def sample_method(a,b):
    a=10
    b=20
    return a*b

