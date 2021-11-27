import abc
# abc = abstract base class
from abc import ABC
# abc.py module contains class ABC

class JNTUAnantapur(ABC):

    # mandate
    # this decorator will make mandatory for child class yi implement this.
    # Can't instantiate abstract class Mahesh with abstract method national_elgibility
    # Mandatory method will decorated by "@abc.abstractmethod"
    @abc.abstractmethod
    def national_elgibility(self):
        pass

    # optional method to implement because we don't have "@abc.abstractmethod"
    def age_elgibility(self):
        print("Student should have minimum 17 years.")
