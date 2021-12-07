# enumerate function will accept ant data strcture as inout and generate list of tuples
# that tuple will have 2 values, 1: index, 2: iterating element

list_1 = ["First class", "Second class", "Third class", "fourth class"]

# creating enumerate objects
obj1 = enumerate(list_1)

print(list(enumerate(list_1)))
# changing start index to 1 from 0; by passing starting index as second argument to a function enumerate
print(list(enumerate(list_1, 1)))

# you can mention the desired expected data type i.e, list/tuple/set
print(tuple(enumerate(list_1)))

print("____________________________________________________________________")
l1 = ["eat", "sleep", "repeat"]
print(enumerate(l1))
for ele in enumerate(l1):
    # printing tuple element
    print(ele)

# 100 starting index
for count, ele in enumerate(l1, 100):
    print(count, ele)