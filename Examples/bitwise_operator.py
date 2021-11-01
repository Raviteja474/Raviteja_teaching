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