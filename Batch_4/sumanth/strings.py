# write a code to print that first unique character and position of that character -->
# sample_dict = {"python": 2022}
# print(sample_dict)
# sample_dict["python"] = 2023
# print(sample_dict)

# empty_dict = {}
# print(empty_dict)
# empty_dict["python"] = 2023
# print(empty_dict)

# write a code to print unique characters and duplicate characters and their position
# input_string = "india is @#$#!% my country !@#$@#$#!%"
#
# special_char = "!@#$@ ^&*?<>%"
#
# count_of_char = {} #i:2, n:1, d:1
#
# for char in input_string:
#     if char not in special_char:
#         if char not in count_of_char:
#             count_of_char[char] = 1
#         else:
#             count_of_char[char] += 1
#
# print(f"Count of characters in the given string --> {count_of_char}")
# unique_char = []
# duplicate_char = []
# for key, value in count_of_char.items():
#     if value == 1:
#         # print(key)
#         unique_char.append(key)
#         index_of_unique = input_string.index(key)
#         print(f"{key} --> {index_of_unique}")
#     else:
#         # print(key)
#         duplicate_char.append(key)
#         index_of_duplicate = input_string.index(key)
#         print(f"{key} --> {index_of_duplicate}")
#
# print(unique_char)
# print(duplicate_char)


# write a code to print that first unique character and position of that character
input_string = "india is @#$#!% my country !@#$@#$#!%"

special_char = "!@#$@ ^&*?<>%"

count_of_char = {} #i:2, n:1, d:1

for char in input_string:
    if char not in special_char:
        if char not in count_of_char:
            count_of_char[char] = 1
        else:
            count_of_char[char] += 1

print(f"Count of characters in the given string --> {count_of_char}")

for key, value in count_of_char.items():
    if value == 1:
        # print(key)
        index_of_unique = input_string.index(key)
        print(f"First Unique character is : '{key}' and position of that character is: {index_of_unique}")
        break

# sample_string = "india is my country"
# for index, char in enumerate(sample_string):
#     if sample_string.count(char) == 1:
#         print(f"First Unique character is : '{char}' and position of that character is: {index}")
#         break

# string = "ffgyytuuugg"
# for i in range(len(string)-1):
#     c=string.count(string[i])
#     if c==1:
#        print(string[i])

