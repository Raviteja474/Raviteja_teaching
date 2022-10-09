def sample_method():
    a,b,c=2,3,4
    return a,b,c

def sample_method_1():
    return "I am Indian"

print(type(sample_method()))
print(type(sample_method_1()))

x,y,z = sample_method()
print(x,y,z)
# x,y,z = sample_method()
# ValueError: not enough values to unpack (expected 4, got 3)