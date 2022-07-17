# *
# * *
# * * *
# * * * *
#
# * * * * *
# * * * *
# * * *
# * *
# *
#
#      *
#    * * *
#  * * * * *
#
# *
#   *
#     *
#        *
#           *
#        *
#     *
#   *
# *

lines = int(input("How many rows? "))
for i in range(1,lines+1):
	print("* "*i+(lines-i)* "  ")

print("\n"*3)

for i in range(0,lines+1):
	print("* "*(lines-i)+"  "*i)

print("\n"*3)

for i in range(1,lines+1):
	print("  "*(lines-i)+"* "*(2*i-1)+ "  "*(lines-i))


print("\n"*3)

for i in range(1,lines+1):
	print("  "*(lines-i)+"* "*(2*i-1)+ "  "*(lines-i))
for i in range(1,lines+1):
	print("  "*(lines//2+1)+"* "*(lines//2)+ "* "*(lines//2-1) +"  "*(lines//2+1))


