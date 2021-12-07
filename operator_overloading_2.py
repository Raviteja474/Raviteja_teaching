
print(len([1,2,3,4,5]))

def len(list_2):
    return 1

# built in length function is overloaded by user-defined length function
# method overloading
print(len([1,2,3,4,5]))
print(len([1,2,5]))

print("____________________________________________________")

def tell_about_him(name):
    return f"{name} is a good boy."

# line 18 methods will override line 14 method.
def tell_about_him(name):
    return f"{name} is a bad boy."

print(tell_about_him("Ravi"))