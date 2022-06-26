names = ["Ravi","vaibhav","samarth","Avinash","sowjanya"]

# # 1. accessing elements with iterator variable
# for name in names:
#     print(name)

# 2. accessing elements with index
for index in range(len(names)):
    print(names[index])

# len(names)=5, range(5) --> 0,1,2,3,4
# line 9 :
# name[0],
# name[1],
# name[2],
# name[3],
# name[4]


string_1 = "India is my country and all indians are my brothers and sisters."
#"India is my country and all indians are my brothers and sisters."
#"India#is#my#country#and#all#indians#are#my#brothers#and#sisters."
# replces old with new
string_1=string_1.replace(" ", "#")

# devide string into list using split function and join.
list_1 = string_1.split(" ")
# replasable string.join(list_name)
print("#".join(list_1))

string_1 = "India is my country and all indians are my brothers and sisters."
# string will be splitted into list based on space
list_1 = string_1.split(" ")
# taking every alternate element from list as step size is 2
# storing to the same variable to avoid unnecessary variable declarations
list_1=list_1[::2]
# Adding space for every element
string_1=" ".join(list_1)
print(string_1)
# India my and indians my and

print("*"*80)
string_2 = "India is my country and all indians are my brothers and sisters."
# aidnI si ym yrtnuoc dna snaidni era ym srehtorb dna llasretsis
list_2 = string_2.split(" ")
for index in range(len(list_2)):
    # list_2[index]=list_2[index][::-1]
    list_2[index]=list_2[index][::-1]
print(" ".join(list_2))

print("*"*80)
dict_2 = {1: "Ravi", 2: "Teja", 3: "VaibhavVaibhavVaibhavVaibhavVaibhavVaibhav"}
print(dict_2[3][1:15])
print(dict_2.keys())
print(type(dict_2.keys()))
print(dict_2.values())
print(type(dict_2.values()))

print("#"*80)
dict_4 = {2:{"Ram":78},3:{"Raj":600},4:{"Ravi":591}}
for item in dict_4.values():
    print(item)
print("#"*80)

print("*"*80)
topper_marks = 0
dict_5 = {2:{"Ram":78},3:{"Raj":600},4:{"Ravi":591}}
for key,value in dict_5.items():
    for key1,value1 in dict_5[key].items():
        if dict_5[key][key1]>topper_marks:
            topper_marks=dict_5[key][key1]
print(f"topper_marks: {topper_marks}")


print("*"*80)
college = ["Finance", "Placement",{"Address": "pincode 524305"},
           {"ECE":{2:{"Ram":78},3:{"Ram":600},4:{"Ravi":591}},
           "EEE":{2:{"Ram1":718},3:{"Ram2":300},4:{"Ravi7":101}},
           "CSE":{2:{"Ram8":178},3:{"Ram12":110},4:{"Ravi5":110}}}]

# who is topper of ECE
print(college[3]["ECE"])



