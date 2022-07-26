import sys
def lokesh():
    print("I am lokesh.")
print(lokesh)
print(sys.getsizeof(lokesh))

dict_1 = {1:2}
print(dict_1)
list_1 = [1,2]
print(list_1)

print(type(dict_1))
print(type(list_1))

# customized datatype another name for class
class Sample:
    pass

sample = Sample()
print(type(sample))
print(type(type(sample)))
print(type(dict))
print(type(list))
print(type(object))
print(type(type))

# type of any class is type


# <class 'dict'>
# <class 'list'>
# <class '__main__.Sample'>