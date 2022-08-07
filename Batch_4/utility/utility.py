
def tell_difference(obj1,obj2):
    height_differnce= obj1.height-obj2.height
    weight_differnce= obj1.weight-obj2.weight
    if obj1.height>obj2.height:
        print(f"{obj1.name} is higher {abs(height_differnce)} inches than {obj2.name}")
    else:
        print(f"{obj2.name} is higher {abs(height_differnce)} inches than {obj1.name}")
    if obj1.weight>obj2.weight:
        print(f"{obj1.name} is kgs  heavier{abs(weight_differnce)} inches than {obj2.name}")
    else:
        print(f"{obj2.name} is kgs heavier {abs(weight_differnce)} inches than {obj1.name}")