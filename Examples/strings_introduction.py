# python handles single, double, triple quotations as is.
name = 'Bharath'
print(name.lower())
print(name.upper())


name = "Bharath"
print(name.lower())
print(name.upper())

name = '''Bharath'''
print(name.lower())
print(name.upper())
print("_______________________________________________________________________________________________________________________")
# Takes as string after double quotations
name = "Bharath"
print(name.lower())
print(name.upper())

print(len(name))

# In indexing we have positive and negative indexes
# If we don't provide starting and ending values, it takes all values.
print(name[:])
# prints 2,3,4,5 indexes
print(name[2:6])
print(name[2:6])
# negative index with string slicing
print(name[2:-3])

# updating/deleting substring based upon index is not allowed
# but we can update entire string.

print("__________________________________________________________________________________________")

# http://sticksandstones.kstrom.com/appen.html
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences:               ")
print(String1)


String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ")
print(String1)

String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

String1 = "{0:e}".format(45446464165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)

String1 = "{0:.21f}".format(1/6)
print("\none-sixth is : ")
print(String1)

# < left alignment ^center alignment > right alignment , 10 minimum size guranteeed irrespective of occupancy
String1 = "|{:<10}|{:^10}|{:>10}|".format('Ge', 'formatting12211111', 'Geeks')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)

# To demonstrate aligning of spaces
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)
print(String1)

