import json
import random
import time

import openpyxl

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

def give_student_rank(student_info):
    rank = random.choice(RANKS)
    print(rank)
    # creating new item with key EAMCET_rank and value rank as taken randonly from list of ranks 1-6
    student_info["EAMCET_rank"] = rank
    return student_info

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
print("Welcome to EAMCET-2021 and please wear mask and maintain social distance")
print("DON'T COPY :)")
time.sleep(5)
print("Thanks for attending exam. We will announce results shortly.")


starting_time = time.time()
while True:
    if time.time()-starting_time<10:
        # pickup a random ball every time
        print("Enjoying holidays :):):):):):):):):):):):):):):):):):):):):):):):):):):):)")
        time.sleep(1)
    else:
        break

RANKS = [1,2,3,4,5,6]
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
