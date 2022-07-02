import calculator_program

# test suite
# test scenario
# positive tests
# test case 6, test data(3,4)
print(calculator_program.addition(3,4))
print(calculator_program.substract(3,4))
print(calculator_program.multiply(3,4))
print(calculator_program.division(3,4))

# negative testing
print("*"*80)
# default value
calculator_program.addition(3)
# ZeroDivisionError: division by zero
calculator_program.division(3,0)