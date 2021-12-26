a = 0
b = 1
fib_list = []

result_list = []

user_input = int(input("lower range input:"))

user_input1 = int(input("higher range input:"))

# generating fibonacci numbers in infinite loop untill most recent fibonacci number>given number

while True:
    fib_list.append(a)
    fib_list.append(b)
    # we are storing the value of the previous two numbers
    c = a + b
    a = b
    b = c
    fib_list.append(c)

    if c > user_input1:
        print("The entered input is lessthan recent fibonacci number")
        break
print(f"{fib_list} total fibonacci number is so far")
for element in fib_list:

    if element > user_input and element < user_input1:
        result_list.append(element)

    else:
        continue
print(f"{result_list} is grater than lower range input and lower than higher range input")

# print(f"Total flibonacci list is {fib_list}")





