class Fish():
    def __init__(self):
        print("Fish called.")

class Dinosaur1(Fish):
    def __init__(self):
        print("Dinosaur called.")
        super().__init__()

    def who_ami(self):
        print("I am Dinosaur")

class Frog(Fish):
    def __init__(self):
        print("Frog called.")
        # 19@@
        print("_________________________________")
        # below 2 approaches are same
        super().__init__()
        # below 2 lins are same above line
        super(Frog, self).__init__()
        Fish.__init__(self)
        print("_________________________________")
    def who_ami(self):
        print("I am Frog")

class Crocodile(Frog,Dinosaur1):
    def __init__(self):
        print("Crocodile called.")
        # it is calling all parent constructors but not following MRO
        super().__init__()
        # Method resolution oder; only one method will be called
        super().who_ami()

crocodile = Crocodile()

# constructor chaining