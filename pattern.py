# rows-1-i 2*i+1 rows-1-i

rows = 5
for i in range(0,5):
    print((rows-1-i)*" ",end="")
    print((2*i+1)*"*",end="")
    print((rows-1-i)*" ",end="")
    print()