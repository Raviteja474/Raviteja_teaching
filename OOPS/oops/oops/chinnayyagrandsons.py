from chinnayyasons import *
# line 1 = line3+line 4
# from chinnayyasons import Subramanyam
# from chinnayyasons import Anjayya
from education import *


class Mahesh(Anjayya,JNTUAnantapur):
    adhar = "104"
    # intentionally write pass to occupation becuase he don't want to inherit his father occcupation.
    def occupation(self):
        pass

    def special_interest(self):
        print("He is interested in cricket")

    def dream_about(self):
        print("Dream about Indian cricket.")

    def national_elgibility(self):
        print("Mahesh is an Indian")

    def your_name(self):
        print("I am Mahesh")

    def age_elgibility(self):
        print("I am very talented, I don't need to follow rules, I am 15 years.")


class Chandra(Subramanyam):
    adhar = "105"
    def occupation(self):
        print("He is a software engineer")

    def native_place(self):
        print("He is from Hyderabad.")

    def your_name(self):
        print("I am Chandra")


class Murali(Subramanyam):
    adhar = "106"
    def occupation(self):
        print("He is a PEF master.")

    def marital_status(self):
        return True

    def your_name(self):
        print("I am Murali")


class Sravani(Anjayya):
    adhar = "107"
    def gender_info(self):
        return "Female"

    def your_name(self):
        print("I am Sravani")

    def dream_about(self):
        print("Dream about Indian Dream.")

