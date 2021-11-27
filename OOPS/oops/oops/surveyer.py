# importing all classes in module chinnayyagrandsons
from chinnayyagrandsons import *
from education import *

# creating object to a class
chinnayya = ChinnayyaPadavala()
# calling instance method in reference with object
chinnayya.occupation()

# calling class variable
print(Subramanyam.adhar)

mahesh = Mahesh()
# inheriting from his grand father (super parent class, his immediate parent don't have that attribute.)
mahesh.sirname_info()
mahesh.occupation()
mahesh.color()
mahesh.special_talent()
mahesh.dream_about()


# this is abstraction
# mandatory implementation from @abc.abstractmethod
mahesh.national_elgibility()
# optional implementation
mahesh.age_elgibility()


chandra = Chandra()
murali = Murali()
sravani = Sravani()

student_names = [mahesh,chandra,murali,sravani]

# polymorphism
for student in student_names:
    student.your_name()





