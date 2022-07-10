import sys
BASIC_salary = 15000
rent = 5000
special_allowance = 20000

efficiency = int(input("What is his efficiency from 0 tp 100?"))
if not 0<=efficiency<=100:
    print(f"Invalid data: {efficiency}")
    sys.exit()


if efficiency<25:
    performace_bonus = 5000
elif efficiency<50:
    performace_bonus = 10000
elif efficiency<75:
    performace_bonus = 15000
else:
    performace_bonus = 20000

print(f"performace_bonus: {performace_bonus}")