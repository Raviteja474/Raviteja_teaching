from model import *


class Shape(Model):
    # can be accessed anywhere; public
    # class variable/static variable
    public = 2
    print("class Share entered.....")

    def __init__(self, length, breadth, personal="I am shape"):
        super().__init__()
        self._length = length
        # within the class and inherited class; protected
        self._breadth = breadth
        # accessible with in class; private
        self.__personal = personal

    def display_sides(self):
        print("Length: ", self._length)
        print("Breadth: ", self._breadth)
        print("personal", self.__personal)
        print(self.m1)
        print(self._m2)
        # print(self.__m3)


class Rectangle(Shape):

    print("class Rectangle entered.....")

    def __init__(self, length, breadth):
        # Shape.__init__(self,length, breadth)
        super().__init__(length, breadth)

    def calculate_area(self):
        print("Area: ", self._length * self._breadth)


obj = Rectangle(80, 50)

obj.display_sides()

obj.calculate_area()