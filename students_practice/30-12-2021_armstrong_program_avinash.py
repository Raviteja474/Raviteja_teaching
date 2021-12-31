num_1=int(input("enter first number:"))
num_2=int(input("enter end number:"))
# 153 = 1**3+5**3+3**3=153
#
for element in range(num_1,num_2+1):
    element_1=element
    sum=0
    print("currently iam checking element is:", element)
    while element>0:
        digit=element%10
        element=element//10
        sum=sum+digit**3
        print("sum till now : ",sum)
    print("total sum at the end:",sum)
    if sum==element_1:
        print(f"{element_1} the given number is an amstrong number ")
        print("---------------------------------------------------------------------------------------------------------")
    else:
        print(f"{element_1} the given number is not an amstrong number ")
        print("-------------------------------------------------------------------------------------------------")

        # print(f"{element} is not an amstrong number")

