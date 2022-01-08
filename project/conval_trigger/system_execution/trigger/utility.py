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
    :return:
    """
    pass

def flash_config(config_path):
    """
    This function used for config flashing.
    :param config_path:
    :return:
    """


def flash_firmware(firmware_path):
    """
    This function used for firmware flashing.
    :param firmware_path: (firmware location)
    :return:
    """


def extract_runnable_tests(combination):
    """
    Specifies which test we need to run.
    :param combination: (specifies on which config we need to run)
    :return:
    """


def rename_file(file_location):
    """
    This function rename the file extension.(use subprocess module to rename .cmd to .txt)
     :return:
     """


def copy_files(source_path, destination_path):
    """
    This function copies contents from source directory to destination directory.
    :return:
    shutil.copyfile
    """
    pass


def delete_files(path):
    """
    os module, rm function
    :param path:
    :return:
    """
    pass


def execute_local_command(command):
    """
    subprocess lines

    :param command:
    :return:
    """
    pass


def execute_remote_command(command):
    """

    :param command:
    :return:    """
    pass


def is_reachable(ip_adress):
    """
    subprocess,ping function
    :param command:
    :return:
    """
    pass


def is_reachable(ip_adress):
    """
    subprocess,ping function
    :param command:
    :return:
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


def excute_tests(tests_list):
    """
     C:\Users\PMahesh\Desktop\conval_trigger\validation_tests>python data_corruption.py & python memory_outofreach.py &
     python power_loss.py & python read_fail.py & python write_file.py
    :param ip_adreess:
    :param destination_path:
    :return:
    """
    pass
