import time
# imports should be always top.
""""
False	True	else	import	pass break		in
True		is	return and	continue	for		
as	def	from		while
assert	del		not	 elif	if	or

# static typing
int i = 10;
float f= 9.0;

# duck typing/dynamic typing(python)
i=10
j =9.0
***********************
"""
user_name = input("Enter your username?")
print("*"*18, user_name, "Enjoy your picnic!!!" , "*"*18)
""""
print("Rama is a good boy and he has three brothers.")
# Format specifiers
print("Rama is a good boy and \n he has three brothers.")
print("Rama is a good boy and \t \t he has three brothers.")
print("Rama is a good boy and \b\b\b\b\b\b\b\b\b\b he has three brothers.")
# print(user_name)
"""


# method signature/definition (parameters/arguments here, user_name )
def enjoy_food(user_name):
    # Method implementation
    print(f"Enjoy your food Mr.{user_name}!!")
    print(83483247237*59453845093859)


response = False
response = True
# overriding the variable
response = input("Do you have money??")

if response:
    print("Welcome to hotel!!!")
    # function calling/accessing
    start_time = time.time_ns()
    print(start_time)
    enjoy_food(user_name)
    end_time = time.time_ns()
    print(end_time)
    print(f"Total time taken is {end_time-start_time}")
    print("hand wash!!!")
else:
    print("Sorry not for free!!")

# Indent level 0
# Hardcoding False
# statement = 1 line
if False:
    # Unreachable
    # Indent level 1
    print("I am True!!")
else:
    pass
for i in range(1,10):
    print(i, end= "   ")

age= input("Enter age??")
no_criminial_records = input("Do you have criminal")

# condition, variable , hard coded True
if int(age) > 18 and not no_criminial_records and True:
    print("Please vote!!")
else:
    print("you can't vote")

student = input("Are you a student?")
teacher = input("Are you faculty?")
if student or teacher:
    print("Please enter the college!!")

starting_time = time.time()
i = 0
# wait for 5 seconds , with polling every second
while time.time()-starting_time < 5:
    print("I am waiting!!!")
    # incrementing value
    i=i+1
    time.sleep(1)

print(i)
print("I completed waiting!!")

student_python = input("Enter name??")
assert student_python!="raviteja", "WHY U R WRITING MAN??"
student_python = input("Enter name??")
assert student_python!="raviteja", "WHY U R WRITING MAN??"
student_python = input("Enter name??")
assert student_python!="raviteja", "WHY U R WRITING MAN??"

name = "Ram"
print(name)
del name
print(name)