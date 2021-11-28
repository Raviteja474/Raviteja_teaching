# Access specifier
# public : Anyone can access
# protected : only inherited ones can access; _
# private : noone can access; __


# 19@@ protected??

class GrandFather():
    sir_name = "Pamujula"
    _property= "house"
    __drawing_skills = True

    def sir_name(self):
        print("Pamujula")
    def _property(self):
        print("house")
    def __drawing_skills(self):
        print("yes")

class Father(GrandFather):
    work = "business"
    print(GrandFather.sir_name)
    print(GrandFather._property)
    # print(GrandFather.__drawing_skills)
    print("_________________________________________")

class OutsidePerson():
    work = "Farmer"
    print(GrandFather.sir_name)
    print(GrandFather._property)
    print(GrandFather.__drawing_skills)

OutsidePerson
