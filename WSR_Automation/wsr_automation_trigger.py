
"""
Purpose: Resultant consolidate excel sheet should be created from individual excel files.

input: Individual excel file location

outputs : Team_WSR_20_02_2022_11_23_AM.xlsx

20-02-2022 Sumanth K   Jira-Requirement-1

Steps

1.Input directory should contain atleast one individual file(.xlsx) with ONLY one sheet.
2.Team_WSR_*.xlsx file should be deleted as part of preconditioning.

3.Create an Team_WSR_present_date_time.xlsx file with number of individual .xlsx files
4. Read each individual file in iterations and write to the corrosponding sheet.


"""
import time
import os
import logging

logging.basicConfig(level=logging.DEBUG, filename=r'C:\Users\ravit\Desktop\Teaching\Raviteja_teaching\WSR_Automation\wsr_automation_trigger'+str(time.time())+r'.txt', filemode='a')

def is_valid_directory(input_directory):
    """

    :param input_directory:
    :return: true if it contains atleast one xlsx file
    """
    pass

def delete_existing_file_prefix(input_directory, file_prefix="Team_WSR"):
    """
    :param input_directory:
    :param file_prefix:
    :return:
    If "Team_WSR_20_02_2022_11_23_AM.xlsx" exists, need to replace by this "Team_WSR_20_02_2022_5_23_PM.xlsx" with current time stamp
    so delete this
    """
    pass

def get_sheet_names(input_directory):
    """
    param input_directory:
    :return: a list with elements
    Eg:  Avinash.xlsx, Bharath.xlsx, Visu.xlsx, Sumanth.xlsx, Mahesh.xlsx,
    ["Avinash", "Bharath", "Visu", "Sumanth", "Mahesh" ]
    """
    pass

def create_destination_excel_file(INPUT_DIRECTORY,sheet_names,file_name):
    """

    :param INPUT_DIRECTORY:
    :param sheet_names:
    :param file_name:
    :return:
    # step1. Excel file,
    step 2: Create all sheets here.
    """
    pass


def read_individual_excel_file(input_directory,individual_excel_file):
    """

    :param input_directory:
    :param individual_excel_file:
    :return: return excel data
    """
    pass



INPUT_DIRECTORY = r'C:\Users\ravit\Desktop\Teaching\Raviteja_teaching\files'

import os
from os.path import pardir, sep
INPUT_DIRECTORY = os.path.join(r'C:\Users',os.getenv("username"),r'Teaching\Raviteja_teaching\files')

FILE_PATTERN = 'Team_WSR'

class WSR_automation:
    def __init__(self):
        delete_existing_file_prefix(INPUT_DIRECTORY,FILE_PATTERN)
    def run(self):
        if is_valid_directory(INPUT_DIRECTORY):
           sheet_names = get_sheet_names(INPUT_DIRECTORY)
           file_name = "Team_WSR_20_02_2022_11_23_AM.xlsx"
           create_destination_excel_file(INPUT_DIRECTORY,sheet_names,file_name)
           for sheet in sheet_names:
               with open(INPUT_DIRECTORY+sheet+'.xlsx','r'):
                    pass
                    # read

        else:
            print("NOT Valid_directory")

if __name__ = "__main__":
    wsr_automation = WSR_automation()
    wsr_automation.run()