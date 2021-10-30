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

x = str(input("enter a name:"))
for i in range(0, int(len(x) // 2)):
    if x[i] == x[len(x) - i - 1]:
        continue
    else:
        print("{0} is not a palindrome".format(x))
        break
else:
    print("{0} is a palindrome..".format(x))
