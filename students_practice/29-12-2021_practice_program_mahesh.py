# import math
#
# print(math.factorial(-7))

# num_1 = int(input("enter a number:"))
#
# fact_1 =1
#
#
# for i in range(1,num_1+1):
#     if num_1 == 0:
#         print(f'{fact_1} is 1')
#     elif num_1 <0:
#          print(f'{fact_1} not defined for negative values')
#     else:
#         fact_1 = fact_1*i
# print(fact_1)


# multiplication table

# num_2 = int(input("Enter mul number:"))
# num_3 = int(input("Enter range number:"))
#
# for ele in range(1,num_3+1):
#     print(f"{num_2} * {ele} = {num_2*ele}")

# fibonacci number

# term_1 = int(input("enter fibonocci number:"))
# a=0
# b=1
# list_1=[]
# list_1.append(a)
# list_1.append(b)
# i=0
# while i<term_1:
#     c = a + b
#     a = b
#     b = c
#     list_1.append(c)
#     i+=1
#
# print(list_1)

# Armstrong number

term_2 = input("enter armstrong number:")
list_1 =[]
list_2 = []
sum_1 = 0

var_1 = len(term_2)
var_2 = int(var_1)
for ele in term_2:
    list_1.append(ele)
# print(list_1)
for value in list_1:
    list_2.append(int(value))
# print(list_2)
for index in list_2:
    var_3 = index**var_1
    # print(var_3)
    sum_1 += var_3
print(f'{sum_1} is an armstrong number')












