
def range11():
    a = 0
    b = 1
    fib_list = []
    fib_list.append(a)
    fib_list.append(b)

    i = 0
    while i < 30:

        c = a + b
        a = b
        b = c
        fib_list.append(c)
        i+=1

    print(fib_list[20:26])
range11()


def sum_of():
    a = 0
    b = 1
    fib_list = []
    fib_list.append(a)
    fib_list.append(b)

    i = 0
    while i < 30:

        c = a + b
        a = b
        b = c
        fib_list.append(c)
        i += 1

    sum = 0
    for ele in fib_list:
        sum += ele
    print(sum)

sum_of()

def ls_1():
    lst_1 = ["teja", "avi", "bharath", "mahesh", "visu", "sumanth"]
    lst_2 = []
    for ele in range(len(lst_1)):

        if len(lst_1[ele]) % 2 == 0:
            print(f"{lst_1[ele]} is even.")
            lst_2.append("even")

        else:
            print(f"{lst_1[ele]} is odd.")
            lst_2.append("odd")

    return lst_2

print(ls_1())

sentence_1 = "teja avi bharath mahesh visu sumanth"

# sentence_1 = "even odd odd even even odd"
lst_4 = sentence_1.split(" ")
print(lst_4)
lst_3 = []
for ele in range(len(lst_4)):

    if len(lst_4[ele]) % 2 == 0:
        print(f"{lst_4[ele]} is even.")
        lst_3.append("even")
    else:
        print(f"{lst_4[ele]} is odd.")
        lst_3.append("odd")

print(lst_3)

sen_2 = "@@".join(lst_3)
print(sen_2)

sem = "india is my country all indians are my brothers and sisters"
lst = sem.split(" ")
print(max(lst))
print(min(lst))