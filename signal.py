list_1 = [1,2,3,5,6,9,2,4,6,5,6,8,11,12,12]
list_2 = [8,2,6,5,4,9,1,4,6,5,6,8,6,5]

max_number = 0
count = 0
for index in range(min(len(list_1),len(list_2))):
    if list_1[index] == list_2[index]:
        if max_number<list_1[index]:
            count+=1
            max_number=list_1[index]
print(max_number,count)




