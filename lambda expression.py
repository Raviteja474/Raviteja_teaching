# named functions = user defined functions
# nameless functions = lambda functions = anynonomous functions
from functools import reduce


def cube(num):
    return num**3
print(cube(7))

print("__________________________")

# cube_1 is lamda function; lambda arguments: expression
cube_1 = lambda num: num**3
print(cube_1(7))

list_1 = [1,2,3,4,5,6,7,8,9,10]

# lambda support 3 functions , map, filter , reduce

# map: identifying with one another
# take inputs and generate output but map each other.

# def square_number(list_1):
#     list_2 = []
#     for x in list_1:
#        list_2.append(x**2)
    #return list_2
# we will 10 outputs for 10 inputs
squares = map(lambda x: x**2, list_1)
print(list(squares))

# filter: taking spefic things from avaialble elements
# take a set of inputs from input and opt out the rest of elements



# def even_number(list_1):
#     list_2 = []
#     for element in list_1:
#         if element%2==0:
#             list_2.append(element)
    #return list_2

# filter(lambda iterator variable:condition, list)
# getting 5 outputs for 10 inputs; 5 filtered out.
even = filter(lambda element:element % 2 == 0, list_1)
print(list(even))

# reduce function will take multiple inputs and give only one ouput

# 5, 8, 10, 20, 50, 100  --> 5,8 replaced by 13
# 13, 10, 20, 50, 100  --> 13,10 = replaced by 23
#23, 20, 50, 100  --> 23,20 = replaced by 43
#43, 50, 100  --> 43,50 = replaced by 93
#93, 100  --> 93,100 = replaced by 193

li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)


li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: (x + y)**2), li)
print (sum)
