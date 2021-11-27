# creating  Person class
class Person():
    # if you create a method in class you should but "self" keyword in paranthesis.
    def can_speack(self):
        print("Person should speak.")

# EVERYTHING IN PYTHON IS AN OBJECT.
variable=19
print(type(variable))

# builtin-classes/ builtin types/ built in data types
list_1 = [1,2,3,4,5]
print(type(list_1))
dict_1 = {"avi": 26, "Ravi": 28}
print(type(dict_1))

# user defined types/ user defined classes
# create an object to class
avinash = Person()
# we can access instance methods using object reference.
avinash.can_speack()



print(avinash)
print("Avinash type: ",type(avinash))
print("Person type: ",type(Person))
print("Person type: ",type(type(Person)))


# we can create mulitple objects to same class.

bharath = Person()
print(bharath)
# <__main__.Person object at 0x0000015EB80FE0B0>
# Each object has memory.
ravi = Person()
ravi.can_speack()
print(ravi)
mahesh = Person()
print(mahesh)