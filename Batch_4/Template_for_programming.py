"""
Purpose: To find give number armstrong or not
inputs: user input
output: boolean yes/not

Test case:1  153  1**3+5**3+3**3  pass
Test case:2  159  1**3+5**3+9**3  fail


Beterment:
1. Find biggest 4 digit armstrong number
2. Find first prime and armstrong number
3. Find armstrong numbers in given range.
"""

n = int(input("Enter a Number"))
originalValue = n
cube = 0
while n > 0:
    num = n % 10
    cube = cube + pow(num, 3)
    n = n//10
print(cube)
if originalValue == cube:
    print("Amstrong")
else:
    print("not Amstrong")