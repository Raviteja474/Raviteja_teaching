""""
why : interview memory saving
when : strings
how: this program tells

# Floor divison, normal divison
5//2 = 2
5/2 =2.5

6//2 =3
7//2 =3.5
"""

# debug = taking out the error
# compile time
# hard coding/compile time value passing
# starts from index 0 to index 4
var_1= "madam"
# run time value passing
var = input("Enter your string?")
length = len(var)
print(len(var)//2)

# clue 5->2
for i in range(0, length):
    # Formatted strings
    print(f"i {i} ........{var[i]} comparing {var[length-1-i]}")
    if var[i] != var[length-1-i]:
        print("It's not palindrome!!")

print("It's palindrome")
