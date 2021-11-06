# ordered collection/data type/data structure
# insertion order preserved

# unordered collection/data type/data structure
# insertion order not preserved

# I want to thank set of people.  no repeat
# I want to thank list of people. repeat

# set is a data structure where it will remove duplicates.

# ECE,ECE --> ECE
# Ravi, Mahi, Bhara, Ravi  --> Ravi, Mahi, Bhara

set_1 = {1,2,3}
print(set_1)
print(type(set_1))

set_2 = set(["Ravi","Bharath","Visu","Mahi","Ravi"])
print(set_2)
# {'Bharath', 'Ravi', 'Visu', 'Mahi'}
# insertion order not preservation and duplicates removed.

# add method
set_3 = {1, "Ravi", 23 , 45, "Avi"}
set_3.add(21)
print(set_3)
# TypeError: set.add() takes exactly one argument (2 given)
# set_3.add(24,87)
# print(set_3)

set_3.add((2,"Mahi"))
print(set_3)

#TypeError: unhashable type: 'list'
# set_3.add([2,"Mahi"])
# print(set_3)

# adding multiple inputs , we use update method.
set_3.update([2,"Mahi"])
print(set_3)

# TypeError: unsupported operand type(s) for +: 'set' and 'set'
# set_5 = set_1+set_3
# print(set_5)

# remove vs discard(does n't give error if element not exist)

set_3.remove("Mahi")
print(set_3)
# KeyError: 'Mahi'
# set_3.remove("Mahi")


set_3.discard("Ravi")
print(set_3)
# Does n't raise error if element does not exist.
set_3.discard("Ravi")

# it will remove a random element
set_3.pop()

print(set_3)

set_3.clear()
print(set_3)

