import paramiko
import os
import datetime
import re
import subprocess
import nmap
import pprint
import json
import openpyxl
import logging
import shutil
import winrm
import csv


def read_conval_file(conval_file_path):
    """
    This function used for conval file reading.
    :param coval_file_path:
    :return:  list, store all line in list
    """
    pass

# Default SSD, ELAN,customer mandatory, stop_on_fail False

def get_product(product_string):
    """
    This function gives product from given string
    product_string=
    """
    pass

# 4 lines...

def host_API():
    """
    :returns dictionary of avaiable test pc info
    15 dictionary......
    """
    pass



def extract_runnable_tests(number_of_tests,number_of_machines_list):
    """
    Specifies which test we need to run o which machines
    # Eg: 150, number_of_machines_list = [107.99.42.01,107.99.42.02, 107.99.42.03]
    :return: dict
    {107.99.42.01:[1,50], 107.99.42.02:[50,100], 107.99.42.03:[101,150]},
    """
    pass


def rename_file(file_location):
    """
    This function rename the file extension.(use subprocess module to rename non .txt to .txt)
     :return:
     """


def copy_files(source_path, destination_path):
    """
   This function will delete files from Test PC using winrm

   Returns errorcode : 0 if succeed , non-zero if not

    """
    pass


def delete_files(path):
    """
   This function will delete files from Test PC using winrm

   Returns errorcode : 0 if succeed , non-zero if not

    """
    pass


def execute_local_command(command):
    """
    subprocess lines

    :param command:
    :return:

    # if somewant to use this, they will use like below
    ips = [107.99.42.01, 107.99.42.02, 107.99.42.03, 107.99.42.04]

    for ip in ips:
        execute_local_command(r'ping '+ip)

    """
    pass




def execute_remote_command(command):
    """

    :param command:
    :return:    """
    pass


def is_reachable(ip_adress):
    """
    will use subprocess, will return True if no data packets lost
    """
    pass


def send_files(destination_path, ip_adress="192.168.43.4"):
    """
    paramiko module
    :param ip_adreess:
    :param destination_path:
    :return:
    """
    pass


