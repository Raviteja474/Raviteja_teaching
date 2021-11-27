class Person():
    # class variables (if variable is outside constructor those are class variables.)
    can_walk = True
    can_play = True

    # instance methods
    def playing(self, person):
        print(f"{person} is playing.")

    def singing(self, person):
        print(f"{person} is singing.")


mahesh = Person()
mahesh.playing("Mahesh")
visu = Person()
visu.singing("Visweswar")
