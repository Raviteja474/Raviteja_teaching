list_1=["avi","teja","mahesh","bharath","sumanth","visu","avi","mahesh","sumanth","avi"]
# dict_1={3:"avi",1:"teja",2:"mahesh",1:"bharath",2:"sumanth",1:"visu"}

dict_1={}
for index in range(len(list_1)):
    if list_1[index] in dict_1.keys():
        dict_1[list_1[index]]+=1
    else:
        dict_1[list_1[index]] = 1
print(dict_1)


