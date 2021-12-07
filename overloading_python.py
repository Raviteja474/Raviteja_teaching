# overloading = compile tine polymorphism

# it will accept mulitple number of inputs(forms), based upon that it will generate results.

# + used for addition and concatenation in different scenarios.
print(1 + 2)
print("Geeks" + "For")
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

def solve_type_problem(a,b):
    a=str(a)
    b=str(b)
    return a+b
# define function before calling function
# solving type error problem with user defind function as built in function/operator not able to solve our problem.
print(solve_type_problem(1,"geeks"))

# Product two numbers
print(3 * 4)
# Repeat the String
print("Geeks" * 4)

