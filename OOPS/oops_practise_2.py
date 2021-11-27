class Person():
    # class variables (if variable is outside constructor those are class variables.)
    can_walk = True
    can_play = True

    # class method
    @classmethod
    def class_method(cls):
        print("I am class method.")

    # dunder method __ starts with , ends with __ = magic method = special method
    # variables within init method are called instance variables.
    # init method will automatically be called when we are creating an object.(even when you don't call)
    # init method will construct an object
    def __init__(self, name, age, gender):
        print("Person init method is called.")
        self.name = name
        self.age = age
        self.gender = gender

    # instance method
    def print_peron_info(self):
        print(f"Name: {self.name}, age: {self.age}, gender: {self.gender}")

# creating an object and intializing the values through init method.
avinash = Person("Avinash Pamujula", 26, "Male")
# calling instance method through OBJECT ONLY.
avinash.print_peron_info()

# we can call class method/ class variable with class name.(No need of creating object)
Person.class_method()
print(Person.can_play)


# combinations
# 1. instance variable
# 2. non-instance/class variable
# 3. instance method
# 4. non-instance method