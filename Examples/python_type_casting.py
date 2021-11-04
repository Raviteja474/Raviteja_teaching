# upper casting
# lower casting

# converting to higher data type(float)
a = 9
b= float(9)
print(b)

# down casting; loss of data; converting to lower data type(int)
c= 9.7
d = int(c)
print(d)

# convert it to boolean
String1 = "{0:b}".format(16)
print(String1)

String_2 = bin(61)
print(String_2)

# base 2
int_value = int('11111111', 2)
print(int_value)


int_value = hex(int('11111111', 2))
print(int_value)

hex_value = hex(255)
print(hex_value)

hex_value = oct(255)
print(hex_value)

String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

String1 = "{0:e}".format(45446464165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

String1 = "{0:.21f}".format(1/6)
print("\none-sixth is : ")
print(String1)