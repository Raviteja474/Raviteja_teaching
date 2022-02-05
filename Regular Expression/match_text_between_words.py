import re
input_string = """This is explanation of re module
This is explanation of re module
This is explanation of module
This is explanation of re module
This is explanation of module
This is explanation of module
Bharath is son of narasimha rao
raviteja is son of umamaheswara rao"""

expected_output = {}
lines = input_string.splitlines()
# print(lines)
for line in lines:
    father_pattern = re.compile(r"of .* rao")
    father_match = father_pattern.search(line)
    son_pattern = re.compile(r".* is")
    son_match = son_pattern.search(line)
    if father_match:
        father = father_match.group()[3:]
        print(father)
        son = son_match.group()[:-3]
        expected_output[father] = son
print(expected_output)
    # if son_match:
    #     print(son_match)


# sample_string = "this is pychram"
# pattern = re.compile(r"is [a-z]+$")
# pattern = re.compile(r" is .*")
# string_match = pattern.search(sample_string)
# print(string_match)


# pattern = re.compile(r"re")
# match = pattern.finditer(input_string)
# lines = input_string.splitlines()
# print(lines)
# for line in lines:
#     match = pattern.search(line)
#     if match:
#         print(match)



