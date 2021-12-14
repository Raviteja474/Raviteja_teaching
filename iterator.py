#

sample_list = [1,2,3,4,5]

for element in range(len(sample_list)):
    print(sample_list[element], end = " ")
print("\n")
for element in sample_list:
    print(element, end = " ")

sample_list_iterator = iter(sample_list)

while True:
    # TypeError: 'list' object is not an iterator
    #print(next(sample_list))
    try:
        print(next(sample_list_iterator))
    except StopIteration as s:
        print(s)
        print("Iterator size over , Thanks you")
        break