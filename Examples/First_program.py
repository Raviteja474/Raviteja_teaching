# print function, user-defined , builtin =python provided
# single line comment
# constant
PERSON_TEMPRATURE = 98


# Taking input from user
user_name = input("Enter user name ??")
# type conversion str -> integer
user_temparature = int(input("Enter user temparature ??"))

# Formatted strings
print(f"Hello {user_name}!")

# Variable declaration
allergy_item = 2

# mood boolean variable
# = assignment operator
mood = True

# conditioning
if mood:
    print("Go to picnic!!!!!!")
else:
    print("Be in home!!")
    
# 0 home, 1 work 2 picnic, == comparision operator
mood_level = 2

# keywords(python provided words), condition, if elif else ladder
if mood_level==0:
    print("Go to home!!!!!!")
elif mood_level==1:
    print("Go to work!!!!!!")
elif mood_level==2:
    print("Go to hotel!!!!!!")
    if user_temparature>PERSON_TEMPRATURE:
        print("Go out of hotel!!")
        exit()
    # iterating variable: var
    for var in range(1,6):
        if var != allergy_item:
            print("Eat item :", var)
    """
    Multi line comment
    print("Eat item 1")
    print("Eat item 2")
    print("Eat item 3")
    print("Eat item 4")
    print("Eat item 5")
    """
else :
    print("Go to picnic!!!!!!")