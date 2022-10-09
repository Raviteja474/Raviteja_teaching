sample_list = [2,4,5,2,56,2,8,8,2]
max_repetataions = 3
repetation=0
temp_index = 0
expected_value = 2
for index in range(len(sample_list)):
	if repetation<max_repetataions:
		if sample_list[index] == expected_value:
			repetation+=1
			temp_index = index
print(f"3 rd occurence at {temp_index}")