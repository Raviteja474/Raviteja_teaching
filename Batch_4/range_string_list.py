string_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list_1= ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']

# positive step
# start:end:step
# default 0:len(list):1
print(string_1[2:8])
print(string_1[2:8:1])
print(string_1[2:8:2])
print(string_1[2:8:3])
print(list_1[15:23:2])
print(list_1[15::2])
print(list_1[::2])
print("______________________negative step______________________")
# negative step
print(list_1[-1:-10:-1])
print(list_1[-1:-10:-2])
print(list_1[-1:-10:1])
print(list_1[-1:-10:2])
list_1= ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']
print(list_1[-1:10:2])
print(list_1[-1:10:-2])
# default -1: inclusive o th index:-1
print(list_1[::-1])
print(string_1[::-1])
