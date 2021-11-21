# worst
def print_avinash():
    print("Hi, I am Avinash.")

def print_avinash_age():
    print("Ji, I am 25.")

def print_mahesh():
    print("Hi, I am mahesh.")

def print_mahesh_age():
    print("Ji, I am 23.")

def print_bharath():
    print("Hi, I am bharath.")

def print_bharath_age():
    print("Ji, I am 24.")

print_avinash()
print_avinash_age()
print_bharath()
print_bharath_age()
print_mahesh()
print_mahesh_age()

print("_________________________________________________________")
# procedural language (non-object language)
# only methods, no objects
def print_name(name):
    print("Hi, I am ",name)

def print_age(age):
    print("Hi, age is ",age)

def get_branch(branch):
    print("Hi, I am studying ",branch)

def get_blood_group(branch):
    print("Hi, I am studying ",branch)

print_name("Avinash")
print_age(24)
get_blood_group("O+")
get_branch("ECE")

print_name("Bharath")
print_age(25)
get_blood_group("b+")
get_branch("EEE")

print_name("Mahesh")
print_age(23)
get_blood_group("A+")
get_branch("CSE")
# you are sending the values through the method, this is the drawback.
print("_______________________________________________________________")

# methods and class
class Person:
    def __init__(self,name,age,branch,blood_group):
        self.name = name
        self.age=age
        self.branch = branch
        self.blood_group = blood_group

    def print_person_info(self):
        print(f"Name: {self.name}, Age : {self.age}, Branch : {self.branch}, blood_group: {self.blood_group}")

#object creation
# objects have memory, behavior.
# bundling/ reusability/ data maintaince
avinash= Person("Avinash",25,"ECE","O+")
bharath= Person("Bharath",24,"EEE","B+")
mahesh= Person("Mahesh",23,"CSE","A+")

avinash.print_person_info()
bharath.print_person_info()
mahesh.print_person_info()