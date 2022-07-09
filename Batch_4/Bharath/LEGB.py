LEGB - local, enclosed, global, bulit-in

#global
a = 23
print(a)

def metho_1():
    print(a)
    
metho_1()
print(a)

#locals
def method_2():
    b = 10
    print(b)
    
method_2()

print(b)

# global & locals

a = "i am outside"
print(a)

def method_3():
    a = "i am inside"
    print(a)
    
method_3()

print(a)

# global Keyword
a = " i am outside"
print(a)
def method_4():
    
    global a
    a = "i am inside"
    print(a)
    
method_4()

print(a)
    
