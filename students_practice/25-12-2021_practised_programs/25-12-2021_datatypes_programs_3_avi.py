student_list=["raviteja","bharath","avinash","anjayya","mahesh","ganesh","visu","sumanth"]

for index in range(0,len(student_list)):
    print(index,student_list[index])
    if student_list[index]=="mahesh":
        print(f"....{index} is {student_list[index]}")
        print(f"....{index-1} is {student_list[index-1]}")
        print(f"....{index+1} is {student_list[index+1]}")



list_1=["avinash","bharath","mahesh","visu","sumanth","teja","vishnu","ganesh","anjayya","prudhvi","sidhu","chandra"]

# iterator variable will give index
# list[index]will give element
for index in range(len(list_1)):
    print(list_1[index],end="\n")
    # we are checking the element in list with hardcoded value
    if list_1[index]=="mahesh":
        # print(f"{list_1[index]} is placed at : {index}")
        print(f"{list_1[index]} is placed at : {index}")
        #print(f"{list_1[index]} is free ticket")
        # storing matched index to a variable
        var_1=index
print("---------------------------------------------------------")
for index in range(len(list_1)):
    if index==var_1:
        print(f"{list_1[index]} need to pay 0 ")
    elif index==var_1-1:
        print(f"{list_1[index]} need to pay 50 ")
    elif index==var_1+1:
        print(f"{list_1[index]} is to pay 60")
    else:
        print(f"{list_1[index]} is to pay 100")




        # # print(f"{list_1[index-1]} is placed at :{index-1}")
        # print(f"{list_1[index - 1]} is to pay 50")
        #
        # # print(f"{list_1[index+1]} is placed at :{index + 1}")
        # print(f"{list_1[index + 1]} is to pay 60 ")













