# Python program to demonstrate
# command line arguments
# Useful when we want to run python file with different number/combination of inputs
import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end=" ")
for i in range(1, n):
    print(sys.argv[i], end=" ")

# Addition of numbers
Sum = 0

for i in range(1, n):
    Sum += int(sys.argv[i])

print("\n\nResult:", Sum)

# program exit here
#sys.exit("Age less than 18")
print("ravi")

# returns the list of directories that the interpreter will search for the required module.
print(sys.path)
print(sys.modules)

a = 'Geeks1221'

print(sys.getrefcount(a))
b_z=1
print(sys.getrefcount(b_z))


print(sys.executable)

str1= "print(2+4-121-121-12*12)"

exec(str1)
