input_list = [123, 23, 56, 78, 4, 1, 2, 3, 89, 113, 56, 124, 79]

# print(max(input_list))

max_num = input_list[0]
for num in input_list:
    if num > max_num:
        max_num = num
    # print(num)
print(f"Maximum number from the given list --> {max_num}")

second_max = input_list[1]
for num in input_list:
    if num != max_num and num > second_max:
        second_max = num
print(f"Second Maximum number from the given list --> {second_max}")

min_num = input_list[0]
for num in input_list:
    if num < min_num:
        min_num = num
    # print(num)
print(f"Minimum number from the given list --> {min_num}")

second_min = input_list[1]
for num in input_list:
    if num != min_num and num < second_min:
        second_min = num
print(f"Second Minimum number from the given list --> {second_min}")
