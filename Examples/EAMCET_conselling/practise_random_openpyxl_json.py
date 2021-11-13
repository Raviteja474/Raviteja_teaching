import json
import time

import openpyxl

import constants

import time

import random

# File handling
# we don't have huge datas in python file itself so we will consume/read datas from other files like (text files(.txt), excel(.xlsx)
# and json files(.json))

# json = javascript object notation  .json

# text file reading
# file operation modes
# r = read
# w = write; it will not create a file if it don't exist and it always write file from very first.
# w+ = create a new file, if file does n't exist
# a = append, if we have contents till line 10, it will resume to write from line 11.

# context manager = it will automatically close the file, once we are done with the file usage.
# with is keyword used with context manger.
# open method accept file location and file mode.

# f is file object to simplify the coding.
# f = open(constants.PAYMENT_INFO_URL, "r")
# as is alias keyword

with open(constants.PAYMENT_INFO_URL, "r")as f:
    # it will read all the lines from file
    lines = f.readlines()
    print(lines)
    #  we are printing every line.
    for line in lines:
        print(line)

# json file
# loads = to read the json file
# dumps = to write into json file

with open(constants.AVINASH_URL, "r")as j:
    # load method will open json file and read json file object and store as disctionary.
    json_obj = json.load(j)
    print(json_obj)
    print(type(json_obj))

print("____________________________________________________________________________________________________")
# excel
# rows
# columns
# cell
# sheet/spread sheet
# loading excel file from file location
wb= openpyxl.load_workbook(constants.FEES_INFO_URL)
# finding the active sheet from excel file
sheet_obj = wb.active
# reading the cell value
cell_obj = sheet_obj.cell(row=1, column=1)
# printing the cell value
print(cell_obj.value)

# use random module to generate 6 digit OTP
starting_time = time.time()
while True:
    if time.time()-starting_time<3:
        # randrange function will give values between two values
        print(random.randrange(10000,999999))
        time.sleep(1)
        break

# random funtion will give some random float value,
print(random.random())

cards = ["king", "queen", "Autin", "diamond", "joker"]
while True:
    if time.time()-starting_time<6:
        # shuffle list every time
        random.shuffle(cards)
        time.sleep(1)
        print(cards)
    else:
        break

# random choice
balls = ["gold ball","silver ball"]
while True:
    if time.time()-starting_time<60:
        # pickup a random ball every time
        print(random.choice(balls))
        time.sleep(1)
    else:
        break

