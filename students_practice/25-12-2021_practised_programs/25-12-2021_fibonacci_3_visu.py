a = 0
b = 1
fib_list = []

user_input = int(input("give me our input number to know whether it is fibonacci or not:"))

# generating fibonacci numbers in infinite loop untill most recent fibonacci number>given number

while True:
    fib_list.append(a)
    fib_list.append(b)
    # we are storing the value of the previous two numbers
    c = a + b
    a = b
    b = c
    fib_list.append(c)

    if c > user_input:
        print("The entered input is lessthan recent fibonacci number")
        break
print(f"{fib_list} total fibonacci number is so far")
if user_input in fib_list:
    print(f"{user_input} is a fibonacci number ")
else:
    print(f"{user_input} is not a fibonacci number")

# print(f"Total flibonacci list is {fib_list}")




