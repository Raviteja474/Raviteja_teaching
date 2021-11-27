class Student:
    COLLEGE_INFO = "Geethajali clg"

    def __init__(self,name,salary,branch):
        print("Init came@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        self.name_info = name
        self.salary_info = salary
        self.branch_info = branch

    # call
    def __new__(cls, *args, **kwargs):
        print("I am new######################################################")

    def name_details(self):
        print(f"My name is {self.name_info} ")

    def salary_details(self):
        print(f"I have {self.salary_info} salary.")

    def branch_details(self):
        print(f"I am from {self.branch_info}")


mahesh = Student("Mahesh Padavala",50000,"civil")
sumanth = Student("Sumanth K",50001,"ECE")
ravi = Student("Ravi p",50002,"EEE")
chandra = Student("Chandra P",50003,"EIE")

students_name = [mahesh,sumanth,ravi,chandra]

for student in students_name:
    print(student.COLLEGE_INFO)
    student.name_details()
    student.branch_details()
    student.salary_details()


