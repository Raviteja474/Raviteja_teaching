from utility import *
# import utility
from utility import tell_difference
# import way 1 ; directly import libraries eg: import time, import re
# import way 2 ; directly import user created library
# from utility import *
# import way 3 ; directly import user created library, importing only class or function
# from utility import tell_difference

# utility have 3 methods --> from utility import *--> u can use 3 methods
# utility have 3 methods --> from utility import tell_difference-->
# u can use only tell_difference method

class Person:
    def __init__(self,height,weight,name):
        self.height = height
        self.weight = weight
        self.name = name


vaibhav = Person(5.8,70,"vaibhav")
lokesh = Person(5.9,75,"lokesh")
tell_difference(vaibhav,lokesh)

