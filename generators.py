
# normal function multiple return approach drawback
def help_sick_person():
    return "Give him medicines."
    # non-reachable code
    return "Call ambulance."
    return "Join him in hospital."

# you will always get same value
print(help_sick_person())
print(help_sick_person())
print(help_sick_person())

print("___________________________________________________________")

# sequence 19@@
# Generator will gives you a sequence of a value using multiple yield statements unlike above example
def help_sick_person():
    # we have 3 yield statments
    yield "Give him medicines."
    yield "Call ambulance."
    yield "Join him in hospital."

# creating a generator
generator = help_sick_person()
print(type(generator))

# we can iterator over generator object like list object
for help in generator:
    print(help)
