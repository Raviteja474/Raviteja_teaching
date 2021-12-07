def square_1(n):
    return n**2

squares = []
list_1 = [1,2,3,4,5]
for element in list_1:
    squares.append(square_1(element))

print(squares)


print("_____________________________________")
def square(n):
    return n ** 2


# We double all numbers using map()
numbers = [1, 2, 3, 4]
# map function will take 2 inputs 1.method name 2. data structure and gives result for that

# map is an introduction to decortors, map function will accept user defined functions as inputs
# we are sending function in function, in python functions are also objects.
result = map(square, numbers)
print(list(result))
