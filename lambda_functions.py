#lambda y: y*y*y
#lambda input: output
# write a function to maximum number

# def max_number(a,b):
#     if a>b:
#         return a
#     else:
#         return b
#
a = 23
b=31
# max_number(a,b)


# Example of lambda function using if-else
# max=lambda a, b : a if(a > b) else b
# print(max(a,b))
#
# max_1=lambda a, b : a if(a > b) else b
# print(max_1(a,b))






# i = [[2, 3, 4], [1, 4, 16, 64], [3, -3, 9, 12], [3, 6, 9, 12]]
# i = [1,22,13,-34]
# print(sorted(i))
# print(i)
# sorted function will sort but wil not change contents like list.sort()
# print(i.sort())
# print(i)



list = [[2, 3, 4,-1,19], [1, 4, 16, 64,21,], [3, -3, 9, 12,31], [3, 6, 19, 12,-45]]
# sort_list = [[-1, 2, 3, 4,,19], [1, 4, 16, 21, 64], [-3, 3,  9, 12,31],
# [-45, 3, 6,  12,19,]]
# secondLargest = list_var[len(list_var) - 2]
# eg: [-1, 2, 3, 4,,19]
# secondLargest = list_var[5 - 2] = list_var[3];sorted;4

# Sort each sublist
sort_list = lambda list: (sorted(element) for element in list)

# Get the second largest element
secondLargest = lambda list, sort_list: [list_var[len(list_var) - 2]
                                         for list_var in sort_list(list)]
res = secondLargest(list, sort_list)

print(res)

