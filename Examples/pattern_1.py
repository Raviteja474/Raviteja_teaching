""""
*
* *
* * *
* * * *
* * * * *
"""
i = 0
while i < 6:
    print("* "*i)
    i = i+1
print("_________________________________________________________________________________________________")
for i in range(6):
    print("* "*i)
    # Assignment operator style in increment
    i+=1

print("_________________________________________________________________________________________________")
# range(5) = range(0,5)
i = 0
for i in range(5):
    for j in range(i+1):
        print("* ", end = "")
    print("")