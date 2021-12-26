count = 1
row = int(input("enter number of rows:"))
for i in range(row):
    for j in range(0, 5-i):
        if count % 2 == 0:
            if count >= 10:
                print(-count, end="")
            else:
                print(-count, end=" ")
        elif abs(count) >= 10:
            print(count, end="")
        else:
            print(count, end=" ")
        count += 1
    print()


count = 1
row = int(input("enter any number:"))
for i in range(row):
    for j in range(0,i+1):
        if count>10:
            print(count,end="")
        else:
            print(count,end=" ")
        count +=1
    print()
