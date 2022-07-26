# parent class1
class Ganesh:
    def __init__(self,location="Buchi", sir_name="Pamujula"):
        self.location = location
        self.sir_name = sir_name
    def about(self):
        print("I am Ganesh")
    def think(self):
        print("Ganesh thinking")


# parent class2
class Sampurna:
    def __init__(self,machine_skill = "Good work", sir_name="Khanna"):
        self.machine_skill= machine_skill
        self.sir_name = sir_name
    def about(self):
        print("I am Sampurna")
    def cook(self):
        print("Sampurna cooking")
# child class 1
class Avinash(Sampurna,Ganesh):
    def __init__(self, btech_branch, gender, height, car_knowledge):
        # calling parent class intializer
        Ganesh().__init__()
        # cslling super() constructor will call prefered parent
        super().__init__()
        # setting the attributes(non-static variables) when we created the object
        self.btech_branch = btech_branch
        self.gender = gender
        self.height = height
        self.car_knowledge = car_knowledge


# child class 2
class Priya(Ganesh,Sampurna):
    def __init__(self,btech_branch, gender, height, cooking_skill):
        super().__init__()
        self.btech_branch = btech_branch
        self.gender = gender
        self.height = height
        self.cooking_skill = cooking_skill


# 19@@ Ravi - non-default parameters in super
ganesh = Ganesh("Nellore", "Pamujula")
avinash = Avinash("CIVIL", "Male",5.9,True)
priya = Priya("EEE", "Female",5.3, "Vegetarian cook")

priya.cook()
priya.think()
priya.about()




# 19@@ AttributeError: 'Avinash' object has no attribute 'location'
# print(avinash.location)

# Method Resoultion order