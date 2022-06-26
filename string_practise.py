str_3 = "VaibhavVaibhavVaibhavVaibhavVaibhavVaibhav"
for index in range(len(str_3)):
    if str_3[index] == 'i':
        start = index
        print(f"First i occured at index: {index}")
        break

for index in range(len(str_3)):
    if str_3[index] == 'i':
        end = index
print(f"Last i occured at index: {end}")

print(str_3[21:154])
list_4 = [1.2,3,4]
print(list_4[2:8])
# IndexError: list assignment index out of range
list_4[6]=3
