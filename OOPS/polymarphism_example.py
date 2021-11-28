# same function name (but different signatures); general polymorphism
# args: arguments
# kwargs: keyword arguments


def addition(*args):
    return sum(args)

print(addition(2,4,3))
# we need to have a solution, irrespective of number of inputs, it should sum

# irrepective number of inputs, we are able to generate sum,
print(addition(2,4,3,16,21,16))


def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

#first ='Geeks', mid ='for', last='Geeks'
# first: geeks, mid:for, last:geeks

def welcome_your_guest(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(f"Hi! {key} from {value}, enjoy the dinner.")

# variable(key), assigned value(value)-->dictionary
welcome_your_guest(Avinash="Buchi",Bharath="Nellore", Sumanth = "Kovur")

print("________________________________________________________________________")

def college_visit(*args,**kwargs):
    # *args list
    # **kwargs dictionary
    for student in args:
        print(f"{student} go and stand somewhere!")

    for student,parent in kwargs.items():
        print(f"Mr.{student} and sir {parent} please have a seat.")

college_visit("Mahesh", "Vishnu", "Sumanth", Raviteja = "Umamaheswararao", Bharath = "Narasimharao", visu= "chtttibabu")