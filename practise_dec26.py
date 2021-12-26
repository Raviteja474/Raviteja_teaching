matrx_size = int(input("Enter matrix size?"))
matrx_list = []
count = 0

while True:

    int_values = []
    inputs = input("Enter inputs?")
    str_values = inputs.split(" ")

    print(f"{len(str_values)} is matrix size")
    print(str_values)

    for value in str_values:
        int_values.append(int(value))

    if not len(int_values) == matrx_size:
        print("insufficeint inputs")
        matrx_list = []
        break
    # appending to outer list
    matrx_list.append(int_values)
    count += 1

    if count == matrx_size:
        break

print(matrx_list)


