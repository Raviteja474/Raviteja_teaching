a = 0
b = 1
fib_list = []

fib = int(input("how many numbers you need to print:"))

if fib <= 0:
    print(f"{fib} is a invalid")
elif fib == 1:
    fib_list.append(a)

elif fib == 2:
    fib_list.append(a)
    fib_list.append(b)
else:
    print("The given input expects more than two flibonacci numbers")
    fib_list.append(a)
    fib_list.append(b)

    while (fib > 2):
        # we are storing the value of the previous two numbers
        c = a + b
        a = b
        b = c
        fib_list.append(c)
        fib = fib - 1
print(f"Total flibonacci list is {fib_list}")




