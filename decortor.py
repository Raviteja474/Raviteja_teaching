import time

def hello_decorator(func):
    print("Outer method reached.")

    def inner1(*args, **kwargs):
        print("Inner method reached.")
        print(f"_______________________Starting {func} method__________________________________")

        # getting the returned value
        # calling the actual method.
        returned_value = func(*args, **kwargs)
        print(f"_________________________Ending{func} method________________________________")

        # returning the value to the original frame
        return returned_value

    print("Inner method calling.")
    return inner1

# 19@@
# adding decorator to the function
# hello_decorator(sum_two_numbers) this equal to below 2 lines
@hello_decorator
def sum_two_numbers(a, b):
    sum1= a+b
    print(f"sum is: {sum1}")

time.sleep(3)

@hello_decorator
def substact_two_numbers(a, b):
    subtract1= a-b
    print(f"substact is: {subtract1}")

time.sleep(3)

@hello_decorator
def multiplicate_two_numbers(a, b):
    mul1= a*b
    print(f"multiplicate is: {mul1}")


a, b = 1, 2

# getting the value through return of the function
sum_two_numbers(a, b)
substact_two_numbers(a, b)
multiplicate_two_numbers(a, b)