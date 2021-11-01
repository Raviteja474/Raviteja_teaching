a = 1
b = 2

# normal prints
print(a, b)
print("a value is ", a, "b value is ", b)
# prints with format function
# substitution
print("a value is {}, b value is {}".format(a, b))

# F-string or formatted strings
print(f"a value is {a}, b value is {b}")

# positional strings
# 0 th index a value , 1st index b value
print("a value is {0}, b value is {1}".format(a, b))
print("b value is {1}, a value is {0}".format(a, b))

# Alias names
print("Pamujula family members names. {visu} {avi} and {teja}".format(visu="Visweswar", avi= "Avinash", teja="Raviteja"))

# o th index element should have atlas 16 letter size with center alignment
# 1st index element should have atlas 4 letter size with left alignment.
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)
print(String1)
print("______________________________________________________________________________________________")

# printing with type specifiers, d stands for decimal and f stand for float
value = 12.3456789
print('The value of Integer1 is %d' % value)
print('The value of Integer1 is %f' % value)
# 19 specifies the value should carry atleast 19 letter size and after . it should print only 2 digits
print('The value of Integer1 is %19.2f' % value)
print('The value of Integer1 is %3.6f' % value)
print('The value of Integer1 is %3.16f' % value)