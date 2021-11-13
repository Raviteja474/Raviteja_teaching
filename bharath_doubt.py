# a-z
# chr function will take ASCII value as input and gives alphanumeric(a-z A-Z 0-9) character


# z y x ..........a
# z y x .......... b

# z x......b a z
# x.......a

# 6 5 4 3 2 1
# 5 4 3 2 1 6

# 1 2 3 4 5 6
list_1 = []

# storing z to a using negative index into list_1
for value in range(65,91):
    list_1.append(chr(value))

list_1 = list_1[::-1]
# getting length of the list
len_list = len(list_1)


for index in range(26):
    # combining two lists
    # 0:26               + 0:0
    # 1: 26              + 0:1
    # 2: 26              + 0:2
    # 26:26              + 0:26
    print(list_1[index:len_list]+list_1[0:index])

print(list_1)


# 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N' , a b c d e f g h i j


str_2 = "19 10 1993"
# str_2 = "19-10-1993"

# replace function will replace first argument with second argument.
str_3 = str_2.replace(" ", "-")
print(str_3)

str_5 = ["Pamujula", "avinash", "buchi"]
str_7 = "***".join(str_5)
print(str_7)
#
str_4_list = str_2.split(" ")
# join function will join two strings with string specified
str_4 = "-".join(str_4_list)
print(str_4)

print("_________________________________________________________________________________")

# ord function will convert character to unicode value
# chr function will convert unicode value to character

# print ASCII table but print only ten items in a row
for value in range(256):
    print(f"Index :{value} and character: {chr(value)},", end = " ")
    # we have 10, 20, 30 .......... which are divided by 10 with remainder 0 , then only give new line.
    if value % 10 == 0:
        print("")

# 11, 12 , 13 unicode character
for value in range(11,14):
    print(f" {value}...........{chr(value)}")


# total string
str_8 = "Rama is good boy."
# index function will try to give index of the substring specified.
# sub string
var = str_8.index("good")
print(var)





