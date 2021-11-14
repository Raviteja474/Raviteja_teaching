# password minimum 8, 1 lowercase, 1 upper case , 1 number, 1 special character

# approach 1: ASCII characters
# ravitE@14

password = input("Enter your input?")

# Always define default values to avoid NameError.
lowercase_flag = False
highercase_flag = False
numeric_flag = False
special_char_flag = False

# 33-47, 57-65, 91,96
special_characters = []
for index in range(33,97):
    if 33<index<48:
        special_characters.append(chr(index))
    elif 57<index<66:
        special_characters.append(chr(index))
    elif 91<index<97:
        special_characters.append(chr(index))

print(special_characters)

for character in password:
    # checking
    if len(password)<8:
        print("Give password atleast 8 charcters.")
        break
    # if any of the character is lowercase, we will make flag true.
    if character.islower():
        print("lowercase_flag became True for character", character)
        lowercase_flag = True

    # if any of the character is uppercase, we will make flag true.
    elif character.isupper():
        print("highercase_flag became True for character", character)
        highercase_flag = True

    # if any of the character is numeric, we will make flag true.
    elif character.isnumeric():
        print("numeric_flag became True for character", character)
        numeric_flag = True

    elif character in special_characters:
        print("special_char_flag became True for character", character)
        special_char_flag = True

# password will be qualified if all below 4 flags(always boolean value) true

if lowercase_flag and highercase_flag and numeric_flag and special_char_flag:
    print("password is qualified.")
else:
    print("password is not qualified.")

# unittest
# Test case document:
# test case requirement: password minimum 8, 1 lowercase, 1 upper case , 1 number, 1 special character
# positive test : Mahesh!19
# negative test :
# scenario:1 Give password less than 8 characters and expect test to be failed. Mahesh1, Ravi!12(test data)
# scenario 2: 8 lettters, no upper case with fullfiiling other requirments ravitej!19
