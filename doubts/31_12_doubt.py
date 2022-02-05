#       input=4
# 	  w="  "
# 	  s="* "
#
# row1: 3W, 1s,3W; input=0->input-iter 2*iter-1  input-iter
# row2: 2W,3S, 2W; input=1
# row3:1W,5s,1W; input=2
# row4: 7S; input=3


input_rows = int(input("Enter required rows?"))
star = "* "
space = "  "

for row in range(1,input_rows+1):
    #print(row)
    print((input_rows-row)*space, end="")
    print((2*row-1)*star, end="")
    print((input_rows - row) * space, end="")
    print()
