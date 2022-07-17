user_input_string = input("Enter your string: ")

# Ramya123Chandra

# isnum(2)= True
# isnum('A')= False
digit_count =0
for character in user_input_string:
    if character.isdigit():
        print(f"This digit: {character}")
        digit_count +=1
print(f"Total digits are: {digit_count}")

sample_dict = {"Visu": "Chitti babu", "Raviteja":"Umamaheswarao"}
expected_dict = {}
for key,value in sample_dict.items():
    expected_dict[value] =key
print(expected_dict)

# 19@@ async, await
# 19@@ empty tuple 40 bytes??
