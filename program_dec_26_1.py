elements = [1,2,3,4,5]
str_elements = []

for ele in elements:
    str_elements.append(str(ele))

print(f"{str_elements}: resultant string")
combinations = []
count=0

for el1 in str_elements:
    for el2 in str_elements:
        for el3 in str_elements:
            for el4 in str_elements:
                for el5 in str_elements:
                    print(f"count: {count}")
                    inner_list = []
                    inner_list.append(el1)
                    inner_list.append(el2)
                    inner_list.append(el3)
                    inner_list.append(el4)
                    inner_list.append(el5)
                    combinations.append(inner_list)
                    print(f"inner_list: {inner_list}")
                    count=count+1
permutations =0
for combination in combinations:
    if len(set(combination))==len(combination):
        print(f"Unique number: {combination}")
        permutations+=1
print(permutations)