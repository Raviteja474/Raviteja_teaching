 #    *
 #   **
 #  ***
 # ****

rows = int(input("Enter how many rows?"))
for row in range(1,rows+1):
    print(" "*(rows-row),"*"*row)
