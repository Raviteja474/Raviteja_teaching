""""
  1 2 3 -1
  6 4 3 1
  1 1 1 0
  1 3 1 0

# row common, column vary
# row vary, column common
# row =column
# 19@@ handle opposite diagonal
"""
value_list = []
matrix= [[1,2,3,-1],[6,4,3,1],[1,1,1,0],[1,3,1,0]]
# outer loop common
for row in range(4):
    # inner loop varies
    row_variable = 0
    for column in range(4):
        print(f"row: {row},column:{column}, value: {matrix[row][column]} ")
        row_variable+=matrix[row][column]
    value_list.append(row_variable)

print(value_list.append("Avinash"))

for column in range(4):
    column_variable = 0
    for row in range(4):
        print(f"row: {row},column:{column}, value: {matrix[row][column]}")
        column_variable += matrix[row][column]
    value_list.append(column_variable)
print(value_list)

diagonal_variable = 0
for row in range(4):
    for column in range(4):
        if row==column:
            diagonal_variable+=matrix[row][column]
value_list.append(diagonal_variable)

print(value_list)

