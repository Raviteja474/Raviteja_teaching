import json
import random
import time

import openpyxl

# import this
import constants

# load/read the student files(.json) and feed it to dictionaries.
# assign the application number using random module
# attend for exam and check Adhar card
# give result after 10 secs, let them enjoy holidays
# give ranks
# ask them for counselling
# give seat allotment
# ask their parent to pay fee
# store payment details(text_file), student info(JSON file), total info (excel file)
# text file = payment receipt
# json file = student details
# excel file = college seat allotment details.

print("EAMCET NOFICATION************************************")
# with context manager you don't need to explicitely close the file, used for memory management.
# open method open any file txt/json/xlsx
# read mode
# as alias name or file object

with open(constants.EAMCET_NOTICATION_URL, "r")as f:
    # file_object.readlines with create list of contents in total file
    lines = f.readlines()
    # printing line by line
    for line in lines:
        print(line)

print("Adding application number to students.")

APPLICATION = "APEMCT2021"


# load student info and add application number, default file mode read
def get_student_json_info(file_location,mode="r"):
    with open(file_location, "r") as j:
        # we don't need to load text file but as json having a particular data structure i,e dictionary
        # load method will convert string of values from .json file to dictionary in python file
        student_info = json.load(j)
        # 19@@ giving application number ending with 4 random numbers
        application_id = APPLICATION + str(random.randrange(1000,9999))
        student_info["Application ID"]= application_id
        return student_info



# 19@@
def give_student_rank(student_info):
    # alredy_assign_rank = []
    # rank_random = random.choice(RANKS)
    # while rank_random not in alredy_assign_rank:
    #     alredy_assign_rank.append(rank_random)
    #     rank_random = random.choice(RANKS)
    #     break
    # print(f"rank assigned is {rank_random} to ")
    # creating new item with key EAMCET_rank and value rank as taken randonly from list of ranks 1-6
    # assigning EAMCET ranks randomly
    rank_random = random.randrange(1000,9999)
    student_info["EAMCET_rank"] = rank_random
    return student_info


def get_preference_list(student_info):
    branches = ["ECE", "EEE", "CSE", "IT", "MECH", "CIVIL"]
    # Each student will have his own taste of branches. that's why we are shuffling so that everyone will have
    # different preference list
    random.shuffle(branches)
    # updating student info dictionary with preference_list
    student_info["prefernce_list"] = branches
    return student_info


def get_branch_allocation(branch, avinash_info, bharath_info, mahesh_info, raviteja_info, vishnu_info, visweswar_info):
    print(f"counselling for branch {branch}")

    # accessing avinash_preference list based on key prefernce_list from student information.
    avinash_preference = avinash_info['prefernce_list']
    # Finding what is his prefernce number for this branch.
    avinash_index = avinash_preference.index(branch)
    print(f"Avinash preference is {avinash_index} for {branch}.")

    bharath_preference = bharath_info['prefernce_list']
    bharath_index = bharath_preference.index(branch)
    print(f"Bharath preference is {bharath_index} for {branch}.")

    mahesh_preference = mahesh_info['prefernce_list']
    mahesh_index = mahesh_preference.index(branch)
    print(f"mahesh preference is {mahesh_index} for {branch}.")

    raviteja_preference = raviteja_info['prefernce_list']
    raviteja_index = raviteja_preference.index(branch)
    print(f"raviteja preference is {raviteja_index} for {branch}.")

    vishnu_preference = vishnu_info['prefernce_list']
    vishnu_index = vishnu_preference.index(branch)
    print(f"vishnu preference is {vishnu_index} for {branch}.")

    visweswar_preference = visweswar_info['prefernce_list']
    visweswar_index = visweswar_preference.index(branch)
    print(f"visweswar preference is {visweswar_index} for {branch}.")
    # 19@@


# passing json file location and opening it in read mode in default method argument
avinash_info = get_student_json_info(constants.AVINASH_URL)
print(avinash_info)
bharath_info = get_student_json_info(constants.BHARATH_URL)
print(bharath_info)
mahesh_info = get_student_json_info(constants.MAHESH_URL)
print(mahesh_info)
raviteja_info = get_student_json_info(constants.RAVITEJA_URL)
print(raviteja_info)
vishnu_info = get_student_json_info(constants.VISHNU_URL)
print(vishnu_info)
visweswar_info = get_student_json_info(constants.VISWESWAR_URL)
print(visweswar_info)

# multithreading 19@@ check adhar in simultaneous.
print("_____________________________________________Welcome to EAMCET-2021 and please wear mask and maintain social"
      " distance______________________________________________")
print("DON'T COPY :)")
time.sleep(5)
print("______________________________________________Thanks for attending exam. We will announce results shortly."
      "_________________________________________________________")


starting_time = time.time()
while True:
    if time.time()-starting_time < 3:
        # pickup a random ball every time
        print("Enjoying holidays :):):):):):):):):):):):):):):):):):):):):):):):):):):):)")
        time.sleep(1)
    else:
        break

print("_____________________________________Holidays over. Your Ranks are out, plesse check in internet."
      "________________________________")
RANKS = [1, 2, 3, 4, 5, 6]
# giving 6 students , 6 ranks 19@@ , don't give duplicate ranks
avinash_info = give_student_rank(avinash_info)
print(avinash_info)
bharath_info = give_student_rank(bharath_info)
print(bharath_info)
mahesh_info = give_student_rank(mahesh_info)
print(mahesh_info)
raviteja_info = give_student_rank(raviteja_info)
print(raviteja_info)
vishnu_info = give_student_rank(vishnu_info)
print(vishnu_info)
visweswar_info = give_student_rank(visweswar_info)
print(visweswar_info)


print("_________________________________________Congratulations all for qualifying EAMCET , please attend counselling."
      "__________________________________________")

# Avi Civil, ECE, EEE  6000
# visu CSE, EEE, IT   5000
# Ravi CSE , IT, Civil  7000

#  prepare student branch preference list
avinash_info = get_preference_list(avinash_info)
print(avinash_info)
bharath_info = get_preference_list(bharath_info)
print(bharath_info)
mahesh_info = get_preference_list(mahesh_info)
print(mahesh_info)
raviteja_info = get_preference_list(raviteja_info)
print(raviteja_info)
vishnu_info = get_preference_list(vishnu_info)
print(vishnu_info)
visweswar_info = get_preference_list(visweswar_info)
print(visweswar_info)

print("_____________________________________Seat counselling starts.________________________________")
# storing all branches to list from an excel file
branches = []
wb = openpyxl.load_workbook(constants.FEES_INFO_URL)
# finding the active sheet from excel file
sheet_obj = wb.active
# reading the cell
for row_value in range(2, 7):
    cell_obj = sheet_obj.cell(row=row_value, column=1)
    # printing the cell value
    print("Adding ",cell_obj.value)
    branches.append(cell_obj.value)

print(f"All available branches in GTNN {branches}")
for branch in branches:
    get_branch_allocation(branch, avinash_info, bharath_info,mahesh_info,raviteja_info,vishnu_info,visweswar_info)

# storing all branches and fees info to dictionary from an excel file
branche_fees = {}
wb = openpyxl.load_workbook(constants.FEES_INFO_URL)
# finding the active sheet from excel file
sheet_obj = wb.active
# reading the cell
for row_value in range(2, 7):
    cell_branch = sheet_obj.cell(row=row_value, column=1)
    # printing the cell value
    print("cell_branch ",cell_branch.value)

    cell_fees = sheet_obj.cell(row=row_value, column=2)
    print("cell_fees ",cell_fees.value)
    branche_fees[cell_branch.value] = cell_fees.value

print(branche_fees)

