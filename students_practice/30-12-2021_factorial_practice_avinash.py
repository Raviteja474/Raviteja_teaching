user_input=int(input("enter a number"))
# 6!= 6*5*4*3*2*1-720
initial_value=1
for i in range(6,0,-1):
    initial_value=i*initial_value
    print(f"{initial_value} initial_value till now , present i value is:{i}")
print(f"{initial_value} initial value at end")
# this is non-recursive way of factorial

# def factorial(number):
#     number = number * number-1
#     while not number == 1:
#         return number
#
# print(factorial(6))


