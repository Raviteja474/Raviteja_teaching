# password minimum 8, 1 lowercase, 1 upper case , 1 number, 1 special character

# approach 1: ASCII characters
# ravitE@14

password = input("Enter your input?")

# Always define default values to avoid NameError.
lowercase_flag = False
highercase_flag = False
numeric_flag = False
special_char_flag = False

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

    elif character in ["@", '!']:
        print("special_char_flag became True for character", character)
        special_char_flag = True

# password will be qualified if all below 4 flags(always boolean value) true

if lowercase_flag and highercase_flag and numeric_flag and special_char_flag:
    print("password is qualified.")
else:
    print("password is not qualified.")
