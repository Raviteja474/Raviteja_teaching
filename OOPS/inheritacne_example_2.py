# instead of creating object to access super class , get it from child class.
# 19@@ singleton design pattern, new method

class Parent():
    # creating parent class object with constructor.
    # sir_name="Padavala" is default argument
    def __init__(self,sir_name="Padavala"):
        print("Parent constructor called.")
        self.sir_name = sir_name

    def print_age(self):
        print(f"he is {self.sir_name} family.")


class Child(Parent):
    def __init__(self, age=18):
        print("Child constructor called.")
        self.age = age
        # it will parent call init method.
        # using super() we can call parent methods or variables
        super().__init__("Pamujula")
        # Parent.__init__() also same; explicitely giving class name.

    def print_age(self):
        print(f"he is {self.age} old.")

child = Child()
print(child.sir_name)

