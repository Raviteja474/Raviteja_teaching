class Class1:
    def m(self):
        print("In Class1")


class Class2(Class1):
    def m(self):
        print("In Class2")


class Class3(Class1):
    def m(self):
        print("In Class3")

class Class5():
    def m(self):
        print("In Class5")


class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        # If you want to call instance method of class
        # a. if you inherit them, you can call with Parentclassname.method
        # b. you need to create an object and need to call
        # a
        Class2.m(self)
        Class3.m(self)
        Class1.m(self)
        # b
        class5 = Class5()
        class5.m()


obj = Class4()
obj.m()