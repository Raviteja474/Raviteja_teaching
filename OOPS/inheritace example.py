class GrandFather():
    def property(self):
        print("He own a house in Kovur.!")

class Father(GrandFather):
    def occupation(self):
        print("He is Teacher!")
    def property(self):
        print("He own a house in Nellore!")
class Mother():
    def occupation(self):
        print("She is a house wife!")

# MRO = Method resolution order
# present --> inherit :1, inherit:2 --> super parent class
class Bharath(Mother,Father):
    # overriding the parent class method
    def occupation(self):
        print("He is a software engineer.")

bharath = Bharath()
bharath.occupation()
# if this object don't have required attribute/method it will search
# in immediate parent and so along.
bharath.property()