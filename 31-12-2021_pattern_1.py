# 				  *   *
#                 *   *
#             *   *   *   *
#             *   *   *   *
#         *   *   *   *   *   *
#         *   *   *   *   *   *
#     *   *   *   *   *   *   *   *
#     *   *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *   *
#
#
# 				  *   *
#             *   *   *   *
#         *   *   *   *   *   *
#     *   *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *   *
#
# rows =5
# row1: 4W,2S,4W    rows-1, 2*n, rows-1
# row2: 3W,4S,3W
# row2: 2W,6S,2W
# row4: 1W,8S,1W
# row5: 0W,10S,0W

input_rows = int(input("Enter number of rows"))
star = "*    "
white = "     "

for row in range(1,input_rows+1):
    for i in range(2):
        print((input_rows-row)*white, end="")
        print((2*row)*star, end="")
        print((input_rows - row) * white, end="")
        print()

# 19@@ pass by value, pass by reference
