lambda function
lambda x,y : expression
map(), filter, reduce(import functools)


var_1 = lambda x,y : x + y
print(var_1(10, 20))

var_2 = lambda x,y : x % y
print(var_2(20, 2))

var_3 = lambda string_1 : string_1
print(var_3("python"))

list_1 =[23,34,45,456]
var_4 = list(map(lambda x : x * x, list_1))
print(var_4)

list_2 = [20,30,40,50]
var_5 = tuple(map(lambda y :y -10, list_2))
print(var_5)

list_3 = [23,34,"berry",45,56,65,"apple","banana"]
var_6 = list(filter(lambda z : z % 2 == 0, list_3))
print(var_6)

var_7 = list(filter(lambda ab : ab > 40, list_3))
print(var_7)

var_8 =list(filter(lambda ac : type(ac) == str, list_3))
print(var_8)

list_4 = [23,434,45,6,343,23,343,5454,34,32]
var_9 = list(filter(lambda az : az % 2 != 0 and az % 3 != 0, list_4))
print(var_9)

ip_list = [23,434,45,6,343,23,343,5454,34,32]
#ip_list = [100, 200, 300, 17, 19, 23, 21]

is_prime = list(filter(lambda i: all(i%j!=0 for j in range(2, i//2)), ip_list))

print(is_prime)


from functools import reduce

list_1 = [23,34,45,768,6,23,44,54]
var_1 = reduce(lambda x, y: x % y, list_1)
print(var_1)

String1 = "{0:.1f}".format(2/7)
print("\none-sixth is : ")
print(String1)
var_1 = 23
print(f"{var_1} is the number")