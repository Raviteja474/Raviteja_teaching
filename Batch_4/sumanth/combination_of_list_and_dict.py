# sample_num = 1
#
# for i in range(1, 11):
#     print(sample_num)
#     sample_num += 1
#     if sample_num > 3:
#         sample_num = 1


sample_list = [-1, 2, 3, -4, -5, -6, 7, 8, 9, -10, 11, -12, 13]

ouput = {-1: -1, 2: 4, 3: 27, -4: -4, -5: 25, -6: -216, 7: 7, 8: 64, 9: 729, -10: -10, 11: 121, -12: -1728, 13: 13}

ouput_2 = {1: -1, 2: 4, 3: 27, 4: -4, 5: 25, 6: -216, 7: 7, 8: 64, 9: 729, 10: -10, 11: 121, 12: -1728, 13: 13}

final_output = {}
power_num = 1
for num in sample_list:
    final_output[num] = num ** power_num
    power_num += 1
    if power_num > 3:
        power_num = 1
print(final_output)

expected_output = {}
num_power = 1
for num in sample_list:
    if num < 0:
        convert_negative_to_positive_num = num * -1
        expected_output[convert_negative_to_positive_num] = num ** num_power
        num_power += 1
        if num_power > 3:
            num_power = 1
    else:
        expected_output[num] = num ** num_power
        num_power += 1
        if num_power > 3:
            num_power = 1
print(expected_output)

# for i in range(1, 11):
#     if sample_num > 3:
#         # print(sample_num)
#         sample_num = 1
#         print(sample_num)
#     else:
#         print(sample_num)
#         sample_num += 1
