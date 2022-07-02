# a,b,c=20,20,20
# d=30
# if a==b and b==d:
#     # if a==b and b==d:
#     print("hi")
#
# # list(),  tuple(), set()
# sample_string = "Raviteja"
# print(list(sample_string))
# print(tuple(sample_string))
# print(set(sample_string))
#
# sample_list = [1,2,1,2,3,2,2,1,6,7]
# print(list(set(sample_list)))

# input 2 3
#         7 5 = 4
#         5 7 = -4
# ouput 2**2=4 3**2=9 (2+3)**2=25 , (2-3)**2=-1

def operations(a,b):
    # c=0
    # if a>b:
    #     c=(a-b)**2
    # else:
    #     c=-(a-b)**2
    c= (a-b)**2 if a>b else -(a-b)**2
    return a**2,b**2,(a+b)**2,c
print(operations(3,4))