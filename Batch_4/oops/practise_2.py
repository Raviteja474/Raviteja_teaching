# Eg:1 class laptop
#     object lenovo, dell, Thinkpad
#     object properties/ attributes: display,CPU, Hard disk


# 1. static method
#      @classmethod, @staticmethod,
# 2. non-static method
#     first parameter self
# 3. Static variable
#     global scope, class method
# 4. non-static variable
#     variables in non-static method


class Laptop:
    def __init__(self, display, CPU, SSD):
        self.display = display
        self.CPU = CPU
        self.SSD = SSD


lenovo = Laptop("15 inches", "i5 processer", "500 GB")
dell = Laptop("14 inches", "i7 processer", "300 GB")
thinkpad = Laptop("13 inches", "i3 processer", "1000 GB")

laptops = [lenovo, dell, thinkpad]

# object polymorphism
# read 2 method ploymophisms avaialble
# 1. default argument
# 2. * args, **kwargs
for laptop in laptops:
    # 19@@ Ravi, print object name , not Hex
    print(str(laptop))
    print(laptop.display)
    print(laptop.CPU)
    print(laptop.SSD)

