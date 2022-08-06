# using re and for loop output is print all the number in given string
import re
sample_string = "86758h49ghsdfe#$%@3h4"

# numbers = "0123456789"

# for char in sample_string:
#     if char.isdigit():
#         print(char)

# for char in sample_string:
#     if char in numbers:
#         print(char)

digit_pattern = "\d"
digits_match = re.findall(digit_pattern, sample_string)
print(digits_match)

max_num = int(digits_match[0])
for num in digits_match:
    if int(num) > max_num:
        max_num = int(num)
print(f"Maximum number from the given list --> {max_num}")


input_string = "98ty6op758h49ghsdfe#$%@3h4"
multiple_digits_pattern = "\d+"
multiple_digits_match = re.findall(multiple_digits_pattern, input_string)
print(multiple_digits_match)

max_num = int(multiple_digits_match[0])
for num in multiple_digits_match:
    if int(num) > max_num:
        max_num = int(num)
print(f"Maximum number from the given list --> {max_num}")
