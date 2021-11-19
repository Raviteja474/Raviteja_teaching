import time

string_1 = "laptop is"
# we have a string with 2 words, 1 word should come second, second word should come first
# ex: "is laptop"

string_2 = "laptop is very costly."
print(string_2.split(" "))
string_2_list = string_2.split(" ")
string_2_list_reverse = string_2_list[::-1]

print(" ".join(string_2_list_reverse))

print("___________________________________________________")

sample_list = [1,2,3,4,5,6,7,8,9,10]
starting_element_swap_number = int(input("Enter how many elements from front you want to swap?"))
ending_element_swap_number = int(input("Enter how many elements from last you want to swap?"))

# n elements
# length-1 length   constants   1,3

length = len(sample_list)

# hardcode
# result_string = sample_list[length-2:length] + sample_list[3:length-2]+ sample_list[0:3]
# print(result_string)
# break total list into 3 parts

# part 1 : backside list
# part 2 : constant values which won't change
# part 3: front side list
result_string = sample_list[length-ending_element_swap_number:length] + sample_list[starting_element_swap_number:length-ending_element_swap_number]+\
                sample_list[0:starting_element_swap_number]
print(result_string)

print(time.time())
time.sleep(1)
print(time.time())


sample_list = [1,2,3,4,5,6,7,8,9,10,11,12]

# 1 2 3 4  8 7 6 5  9 10 11 12

# 1 2 3    6 5 4  7 8 9  12 11 10



