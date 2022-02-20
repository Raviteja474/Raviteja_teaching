from WSR_Automation import wsr_automation_trigger
from wsr_automation_trigger import *
WSR_automation = WSR_automation()

def setup():
    WSR_automation.__init__()


def test_is_valid_directory():
    assert (wsr_automation_trigger.is_valid_directory("hardcoded_value: correct value with proper excel files"))
    assert not (wsr_automation_trigger.is_valid_directory("hardcoded_value: incorrect directory"))
    assert not (wsr_automation_trigger.is_valid_directory("hardcoded_value: correct value with improper excel files"))

def test_delete_existing_file_prefix():
    assert (wsr_automation_trigger.delete_existing_file_prefix("hardcoded_value: correct value "))
    assert not (wsr_automation_trigger.delete_existing_file_prefix("hardcoded_value: correct value;open file "))
    assert not (wsr_automation_trigger.delete_existing_file_prefix("hardcoded_value: incorrect value "))

def teardown():
    print("Dummy")

