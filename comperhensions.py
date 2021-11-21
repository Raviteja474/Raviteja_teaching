numbers = []
for number in range(10):
    numbers.append(number)
print(numbers)

# concise way
numbers_1 = [number for number in range(10)]
print(numbers_1)

# conditions
numbers_2 = [number for number in range(10) if number%2==1]
print(numbers_2)

# multiple loops
for table in range(1,6):
    for rows in range(1,11):
        print(f"{table}*{rows} = {table*rows}")

# 1 for - outer loop, 2 nd - inner loop
# result , outer loop inner loop, condition
numbers_3 = [table*rows for table in range(1,6) for rows in range(1,11) if table % 2 == 0]
print(numbers_3)

list_1 = ["Mahesh","Avinash", "Bharath","Ravi"]
list_2 = ["Anjayya","Ganesh babu", "Narasimharao"]

var_5 = zip(list_1,list_2)
print(var_5)
print(list(var_5))

print("_________________________________dict comperhensions______________________________________")
# single list
myDict = {x:x**3 for x in range(11) if x%2==1}
print (myDict)

keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]

# but this line shows dict comprehension here
myDict = {k: v for (k, v) in zip(keys, values)}
print(myDict)

sDict = {x.upper(): x*3 for x in 'coding '}
print (sDict)