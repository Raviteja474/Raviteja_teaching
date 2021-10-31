# special characters or not different in input function
name= input("Enter name?")
print(name)

# presence of escape characters impact output
name = "Ravi \nTeja"
print(name)

name = "Ravi \Teja"
print(name)

name = "Ravi \\\\Teja"
print(name)

# raw strings
name = r"Ravi \nTeja"
print(name)