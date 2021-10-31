import time
# imports should be always top.
""""
False	True	else	import	pass break		in
True		is	return and	continue	for		
as	def	from		while
assert	del		not	 elif	if	or

return  None  in

any all

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


# return keyword returns the result of the method
def add_method(a,b):
    print("Hi, I am add method")
    return a+b

# reusability if primary purpose of the method.
def add_ages(a,b):
    print("Adding 2 poeple ages")
    # To check validity of the parameters
    if a<0 or b<0:
        print("We can't enter negative ages. Invalid data!!")
        # We don't have that data/ invalid data
        return None
    else:
        return a+b


print(f"Adding 2 person ages {add_ages(15,34)}")
print(f"Adding 2 person ages {add_ages(0,0)}")

print(f"Adding 3+4 = {add_method(0,0)}")
print(f"Adding 3+4 = {add_method(3,4)}")
print(f"Adding 48+414 = {add_method(48,414)}")
add_result = add_method(-5748,4144)
print(f"Adding -5748+4144 = {add_result}")
print(f"Adding -5748+4144 = {add_method(-5748,4144)}")

# Ram Ramakrishna  , Ravi Raviteja   purpose  not in purposie
# in keyword used for checking whether this sub string exist in string or not.
if "Ram" in "Ramkrishna":
    print("Ram present in above string.")
print("_______________________________________________________________________________________________")

# oth index will tell if he is faculty or not and 1st index indicates if he is HOD or not
sample_list = [True, False]

if any(sample_list):
    print("Please enter into college!!")

if all(sample_list):
    print("You don't have permission to suspend student!!")
else:
    print("You are just a faculty")

name = "Ram"
print(name)
# Deleting the variable will give error.
del name
print(name)