class Parent():
    def __init__(self):
        print("Parent")

class Student(Parent):
    # def __new__(cls):
    #     print("__new__")
    #     return super(Student, cls).__new__(cls)

    def __init__(self,name,age):
        print("__init__")
        self.name = name
        self.age = age
        #super().__init__()
        Parent.__init__(self)
        # 19@@

avi = Student("Avinash",26)