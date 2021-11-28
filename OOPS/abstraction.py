# abstraction:
""""
abstraction: no yet implemented, whoever inherits this class that class must implement the abstract methods.

class Nokia(ABC)--> abstract class
@abc.abstractmethod --> abstract method
# use: nokia 1100 --> basic phone; smart phone feature(nit)
    # -->
# when we want user to mandate implementation of particular method , write it in an abstract class and inherit that.
# then user need to must implement that method, if not he can't even create an object.
"""
import abc
from abc import *
# abstractmethod()

class Nokia(ABC):

   # non-abstract methods don't have implementation
    def basic_phone(self):
        print("Basic phone.")

   # abstract method don't have implementation
    @abc.abstractmethod
    def smart_phone(self):
        pass

# we can't instantiate an abstract class
# nokia = Nokia()
# # TypeError: Can't instantiate=object creation abstract class Nokia with abstract method talking
# print(nokia)

class Realme(Nokia):
    def conference_calling(self):
        print("Conference call enabled.")
    def smart_phone(self):
        print("Smart feature enabled.")

realme= Realme()
# Can't instantiate abstract class Realme with abstract method smart_phone
# if a child class inherit a Abstract class, child class must implement all abstract methods in it.
print(realme)
