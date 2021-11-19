str1 = "my isname isisis jameis isis bond"
sub = "is"

# 2 nd parameter n , will tell to search the sub string from index n to end of the string.
# default is 0
print(str1.count(sub))
print(str1.count(sub, 10))
print(str1.count(sub, 2))

var= "James kfdgkjdfgkjdjgjdjBond"
print(var[5:2:-1])
# positive end of the string(length)
# positive end of the string(length); negative starting of the string (0th index)
print(var[5::])

print(var[2::-1])

print(var[2:8:-1])

var_1= ['j','a','m', 'e','s','b','o','n','d','e']
print(var_1[2::-1])



# % (Modulus) 4
# & (BitWise AND) 3
# ** (Exponent) 1
# > (Comparison) 2

# 19@@
result = 2%4&3**3>1
print(result)
# 2%4&27>1  -->1
# 2 %4 & True  --> 2
# 2 %0
# print(2%0)

#   LEGB
x=0

def func1():
    global x
    x = 50
    return x
func1()
print(x)

a = 4
b = 11
print(a | b)
# 0 1 0 0
# 1 0 1 1
# 1 1 1 1  = 15
print(a >> 2)
# 0100--> 0001

print("___________________________________________________________________________________________________")
var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            print("Vishnu",i,j, var)
            continue
        else:
            print("Avinash",i,j, var)
    print("_________________________________Variable increased_______________________________________")
    var+=1
else:
    print(var)
    print("_________________________________Variable increased_______________________________________")
    var+=1
print(var)

x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    print(x)
print("hi")

for k in range(2,-4, -1):
    print(k)
print("________________________________________________________")
for num in range(10, 14):
    for i in range(2, num):
        if num%i == 1:
            print(num,i,num%i)
            # 10%2 , 10%3
            print(num)
            break
        else:
            print(num, i, num % i)

print("________________________________________________________")

# 19@@
# 0 positive 1 negative
# s   E  step    default value  S E Step
# 20 25  1
# 20 25 -1
# 20 -25 1
# 20 -25 -1
# 20 -25  -1
print("_____________________________________________")
for i in range(20,-1,1):
    print(i)
# -20 25  -1
# -20 -25  1
# -20 -25  -1

result = [i*j for i in range(5) for j in range(11) if i>0 and j>0]
print(result)


matrix = [[1,6,7],[7,6,5], [3,2,7]]
for row in range(len(matrix)):
    for column in range(matrix[row]):


