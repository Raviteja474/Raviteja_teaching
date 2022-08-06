import re
sample_string = "!@456#$789%^890&*><?"

output = "4567890!@#$%^&*><?"

expected_string = ""
numbers_pattern = "\d"
special_char_pattern = "\W"

numbers_match = re.findall(numbers_pattern, sample_string)
# print(numbers_match)
only_numbers = "".join(numbers_match)
# print(only_numbers)

special_char_match = re.findall(special_char_pattern, sample_string)
# print(special_char_match)
only_special_char = "".join(special_char_match)
# print(only_special_char)

print(only_numbers+only_special_char)



