# even & odd number
for ele in range(1, 50):
    if ele % 2 == 0:
        print(f"it is even num {ele}")
    else:
        print(f"it is odd num {ele}")

# palindorme
# madam = madam
# bharath = htarahb
# a p p l e
# 4, 4-1, 3-1, 2-1, 1-1
# 0 1 2 3 4
# 1 2 3 4 5
# -5-4-3-2-1
original_input = "apple"
print(len(original_input))
reverse_input = ""
for ele in range(len(original_input) -1, -1, -1):
    reverse_input = reverse_input + original_input[ele]
print(original_input, reverse_input)
if original_input == reverse_input:
    print(f"it is a palindrome {original_input}")
else:
    print(f"it is not a palindrome {original_input}")

# fibonacci
# 0 1 1 2 3
list_1 = []
a = 0
b = 1
list_1.append(a)
list_1.append(b)
i = 0
while i < 20:
    c = a + b  #1
    a = b      #1
    b = c      #1
    list_1.append(c)
    i = i + 1

print(list_1)

# pattren
# *
# **
# ***
# ****
print("banana" * 2)
i = 1
while i < 6:
    print("*" * i)
    i = i + 1

i = 6
while i > 0:
    print("*" * i)
    i = i - 1
