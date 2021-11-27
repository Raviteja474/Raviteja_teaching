# it is super parent class(Grand father)
# ChinnayyaPadavala(object) = ChinnayyaPadavala()
# object is super parent of class, it will be inherited automatically.
class ChinnayyaPadavala(object):
    # it's class variable because it is not defined in any instace methods
    adhar = "101"
    # occupation is a instance method
    # 1. it didn't use @classmethod
    # 2. it has self parameter as first parameter
    def occupation(self):
        print("He is a farmer.")

    def native_place(self):
        print("He is from Munimudi.")

    def sirname_info(self):
        print("He belongs to Padavala family.")
