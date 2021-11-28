class Bird:

    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):

    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):

    def flight(self):
        print("Ostriches cannot fly.")

class Chicken(Bird):

    def flight(self):
        print("I can fly to little distant.")


obj_spr = sparrow()
obj_ost = ostrich()
obj_chicken = Chicken()

birds_list = [obj_spr,obj_ost,obj_chicken]

for bird in birds_list:
    print("Can you fly?")
    print(f"{bird.flight()}")