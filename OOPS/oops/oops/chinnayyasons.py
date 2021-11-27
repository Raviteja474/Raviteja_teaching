import abc
from abc import ABC
# abc module will be used to deal with abstraction.
from chinnayyapadavala import ChinnayyaPadavala
# from module_name import classname; signature
# from chinnayyapadavala import *
# automatically import all classes

class Subramanyam(ChinnayyaPadavala):
    adhar = "102"

    def occupation(self):
        print("He is a silk business")

    def native_place(self):
        print("He is from New Buchi.")


class Anjayya(ChinnayyaPadavala,ABC):
    adhar = "103"
    def occupation(self):
        print("He is a sarry businessman.")

    def native_place(self):
        print("He is from old-Buchi")

    def color(self):
        print("white...")

    def special_talent(self):
        print("He is interested in yoga.")

    @abc.abstractmethod
    def dream_about(self):
        pass