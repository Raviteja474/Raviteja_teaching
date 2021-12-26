sentence_1="india is my country all indians are my brothers and sisters"
list_2=sentence_1.split(" ")
list_1=[]
dict_1={}
for index in range(len(list_2)):
    print(len(list_2[index]))
    list_1.append(len(list_2[index]))
    dict_1[list_2[index]]=len(list_2[index])
print(dict_1)

print("--------------------------------------------")
var_1=max(list_1)
print(max(list_1))
print(min(list_1))
max_value=0
for key,value in dict_1.items():
    if var_1 == dict_1[key]:
        print(f"{key} is the max word")
    # if max_value < dict_1[key]:
    #     max_value=dict_1
print(max_value)