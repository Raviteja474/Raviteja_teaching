import time


class Branch:
    # class/static variable
    # definition, assignment
    Principal = "Raj"
    # class method
    @classmethod
    def about_principal(cls):
        # observation 3: we can not assign class variables in static/class methods.
        print(f"Principal: {cls.Principal}")

    # 19@@, @staticmethod

    def __init__(self, branch_name, HOD, faculty_names):
        self.branch_name = branch_name
        self.HOD = HOD
        self.faculty_names = faculty_names

    # non-static/instance method as first parameter is self
    def branch_information(self):
        # non-static variables will be live.
        print(f"** Welcome to branch: {self.branch_name}")
        print(f"HOD is {self.HOD}")
        # index 1,2,3,4
        # self.faculty_names 0,3
        # Observation:4 For real time scenarios , start index from 1 and handle like below.
        for index in range(1,len(self.faculty_names)+1):
            print(f"Teacher {index} : {self.faculty_names[index-1]}")
        print("*"*80)
        # observation: static scope variables can't be used in non-static scope
        # print(cls.location)

# setting attributes to the constructor
ece = Branch("ECE","Ram1", ["Bheem1","Bheem2","Bheem3","Bheem4"])
eee = Branch("EEE","Ram2", ["Bheem5","Bheem6","Bheem7","Bheem8"])
cse = Branch("CSE","Ram3", ["Bheem9","Bheem10","Bheem11","Bheem12"])
it = Branch("IT","Ram4", ["Bheem13","Bheem14","Bheem15","Bheem16"])

# calling non-static methods with object polymorphism
# 19@@ python is that much fast??
start_time = time.time_ns()
# TO access classmethod, we don't need object
Branch.about_principal()
for branch in (ece,eee,cse,it):
    branch.branch_information()
print(f"Tuple time = {time.time_ns()-start_time}")

# TUPLE IS FASTER
# start_time = time.time_ns()
# for branch in [ece,eee,cse,it]:
#     branch.branch_information()
# print(f"List time = {time.time()-start_time}")

# observation 2: Avoid duplicates
# ece.branch_information()
# eee.branch_information()
# cse.branch_information()
# it.branch_information()
