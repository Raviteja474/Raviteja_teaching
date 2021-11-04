# creating a list with some elements
person_1 = ["Raviteja", 28, "M.Tech", "Buchi", "ECE"]
# creating a empty list.
person_2 = []
# creating a empty list with list function.
person_3 = list()
# print(person_1,person_2,person_3)
# printing list using iteration/looping variable "ele"
for ele in person_1:
    print(ele, end = " ")

length_person = len(person_1)

# looping based on index number
for index in range(length_person):
    print(person_1[index])
    # calling person_1[0]. person_1[1], person_1[2], person_1[3]

# multi index support , we have "Raviteja" on 0 th index, it's print 5 th value in that string.
print(person_1[0][5])
# don't try to access elements which are not there, always use length function to verify whether this data is correct or not
# print(person_1[1][5])


# ["Raviteja", 28, "M.Tech", "Buchi", "ECE",56.0]
# Raviteja28M.TechBuchiECE56.0

print("______________________________________________________________________________________________________")
person_4 = ["Raviteja", "M.Tech", "Buchi", "ECE"]

# outer for loop iterate based on person_4 total length
for outer_index in range(len(person_4)):
    # inner for loop iterate based on element length
    for inner_index in range(len(person_4[outer_index])):
        print(person_4[outer_index][inner_index], end="")
print("\n")

# list is mutable datatype, we can change the values.
person_4[2] = "Nellore"
print(person_4)

# Multi dimensional(index)
# gold rate = dollar-rupee conversion, demand, supply, transportation
print("@@@@@@@@@@@@@@@@@@@@@@@")
# multi-dimenssinal
person_5 = [["Ravi",4,5,[1,289789,"Teja"],"Hello", "hai"],"Travel",29]


print(person_5[0][3][2][3])
# error TypeError: 'int' object is not subscriptable
# print(person_5[0][3][1][3])

# append used for adding element
sample_list = [1,2,3,4]
# adds value as a list element
sample_list.append([5,6,7])
print(sample_list)

# adds values to the outer list unlike append
sample_list.extend([8,9,10])
print(sample_list)
# append used for adding element
college = ["ECE", "CSE", "IT"]
college.append("CIVIL")
print(college)

college.extend("MECH")
print(college)

print("_____________________________________________________________________________________")

list_3 = [1, 2, 3, 4]
print("Initial List: ")
print(list_3)
# adds element 12 at index 3
list_3.insert(3, 12)
list_3.insert(0, 'Geeks')
print(list_3)

# it will remove the given value
list_3.remove("Geeks")
print(list_3)
# it will take out last element
list_3.pop()
print(list_3)

list_3.pop(2)
print(list_3)
print("_______________________________________________________________________________________________________""")

            # 0           1      2        3      4       5  6     7     8    9    10
            #  -11     -10        -9     -8      -7  -6   -5     -4     -3    -2   -1
person_6 = ["Raviteja", 28, "M.Tech", "Buchi", "ECE", 29, 121, "test", 121, 312, 9.01]
# starting index(default value zero),ending index(default value length of the list), step size(which step u need to print)
print(person_6)
# left to right
print(person_6[::])
print(person_6[0:2:])

print(person_6[0:6:2])

# right to left
print(person_6[0:6:-2])
print(person_6[6:0:-2])

print(person_6[-3:4:-3])

print(person_6[-3::-2])
print(person_6[-3::2])

# -1 as starting index , -11 ending index with step size 1
print(person_6[::-1])
print("________________________________________________________________________________")
# sublists
person_7 = ["Raviteja", 28, "M.Tech", "Buchi", "ECE", 29, 121, "test", 121, 312, 9.0,1.14,8]
print(person_7[5:9])
# default step size +1 person_7[-5:-9]  equals to person_7[-5:-9:1]
print(person_7[-5:-9])

print(person_7[-6:12])


