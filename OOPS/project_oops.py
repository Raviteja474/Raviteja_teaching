# RAM --> DRAM, SRAM(fast)
# Drive --> HDD, SSD
import abc
from abc import ABC

class RAM(ABC):
    def __init__(self,transistor="YMHFHH1232",size = "40cm"):
        self.size = size
        self.__transistor=transistor
    def about(self):
        print("We are here to increase computer speed with tansisitor{self.__transistor}.")
    @abc.abstractmethod
    def implementation(self):
        pass

class DRAM(RAM):

    def implementation(self):
        print(f"I have size : {self.size}")
        print(f"I am dynamic RAM with transistor: {self.__transistor}")

class SRAM(RAM):
    def implementation(self):
        print("I am static RAM")

class Mouse(RAM):
    def details(self):
        print("I can select content.")

print(f"{issubclass(DRAM,RAM)} Checking??????????????????")
# abstraction example
dram= DRAM()
print(f"{isinstance(dram,DRAM)} IS IT OBJECT??????????????????")
print(f"{isinstance(dram,SRAM)} IS IT OBJECT??????????????????")
sram= SRAM()

#mouse = Mouse()
# TypeError: Can't instantiate abstract class Mouse with abstract method implementation
# polymorphism
# operator overloading, default arguments, * args,* kwargs; non-object polymorphism

# OOPS polymorphsim
dram.implementation()
sram.implementation()
print("__________________________________________________________________________________________________________")


# class Drive:
#     def about(self):
#         print("We are here to store the data.")
# class HDD(Drive):
#     pass
# class SSD(Drive):
#     pass