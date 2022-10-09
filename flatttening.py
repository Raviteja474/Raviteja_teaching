#input = [1,2,3,[1,2,3,8,["Raviteja","india",
                               #(12,12,(12,5,6,["Hi","Ravi"]))]]]
#input = [1,2,[3,4,[5,6,7],8,9],0]
input = [1,2,[3,4,[5,6,7,[45,67,98]],8,9],0]
# flattening
# [1,3,[1,2]]  --> [1,3,1,2]

"""nested list to flat list
   1. Declare a class
   2. Declare a function
   3. print   from the main function
   eg: input = [1,2,[3,4,[5,6,7],8,9],0]
      output : [1,2,3,4,5,6,7,8,9,0] """
#input = [1,2,[3,4,[5,6,7],8,9],0]
flatten_list = []

for element in input:
    print(element)
    if isinstance(element,int):
    # if type(element) == int
        flatten_list.append(element)
        print(flatten_list)

    elif isinstance(element,list):
        for sublist in element:
            if isinstance(sublist,int):
                flatten_list.append(sublist)
            else:
                for subsublist in sublist:
                    flatten_list.append(subsublist)
print(flatten_list)

# recursive function