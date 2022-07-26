class Parent:
    def about(self):
        print("My name is: Parent")


class Child(Parent):
    # Child class method overriding parent class above method

    def __init__(self, name, wife = None, chidren=0):
        self.name = name
        self.wife = wife
        self.chidren = chidren
        self.one_person_amount = 10000
    def about(self):
        print(f"My name is: {self.name}")

    # per person insurance =10000
    def insurance_policy(self):
        insurance_amount = self.one_person_amount
        if self.wife is not None:
            print("I have a wife")
            insurance_amount += self.one_person_amount
        # 0 is not None
        if self.chidren>0:
            print(f"I have Number of Children: {self.chidren}")
            # don't try to hardcode
            insurance_amount += self.one_person_amount* self.chidren
        # If function don't return anything it will give None
        return insurance_amount


# Better to give values along with parameter/argument names.
# child = Child("Ram",True,0)
# child = Child("Ram",True,0)
# Object overloading, we can create object with different number of inputs
# and object behave likewise.
child = Child(name="Ram")
print(f"Total insurance is: {child.insurance_policy()}")
child = Child(name="Ram",wife=True)
print(f"Total insurance is: {child.insurance_policy()}")
child = Child(name="Ram",wife=True,chidren=100)
print(f"Total insurance is: {child.insurance_policy()}")
# child.about()


