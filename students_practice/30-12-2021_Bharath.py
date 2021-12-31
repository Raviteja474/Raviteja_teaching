# prime number range
# a number divisible by itself 3,5,7,11
# prime number should be divisible by 1 or by itself
user_input = int(input("enter a number:"))
user_input1 = int(input("enter end number:"))
for val in range(user_input, user_input1):
    for ele in range(2, val):
        if val % ele == 0:
            # print(f"{val} is not prime num.")
            break
    else:
        print(f"{val} is prime num.")
