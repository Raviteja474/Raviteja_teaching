""""
bitwise
always will do bitwise operations once it convers value from decimal to binary.

"""

a = 10
b = 4

# Print bitwise AND operation
print(a & b)
# a         1010
# b         0100
# result       0000 --> 0

# Print bitwise OR operation
print(a | b)
# a         1010
# b         0100
# result    1110  --> 14

# Print bitwise NOT operation
print(~a)
# a         1010
#  2 complement = 1's complemnt 1 256 -128 to 127 , -10-1= -11

# print bitwise XOR operation
print(a ^ b)
# a         1010
# b         0100
# result    1110  --->14
# 00 0
# 01 1
# 10 1
# 11 0

# print bitwise right shift operation
print(a >> 2)
# a         1010
# result       0010->2

# print bitwise left shift operation
print(a << 2)

# a         1010
# result    101000

# ternary operator
a = 5
if a == 5:
    b=6
else :
    b=7
print(b)

# if a ==5 then assign b=8 , if not b=9, ternary operator, concise way of writing if and else
# b = value1 if condtion else value2
# if condition success b =value1 , if it failes b=value2
b = 8 if a == 5 else 9

print(b)

x=10
y=20
print(x,y)
x,y = 30,40
print(x,y)

z =10,-10,19
print(z)

# swapping 2numbers
i = 15
j = 16

temp = i
i= j
j= temp

print(i,j)

i = 25
j = 26
i,j = j,i
print(i,j)