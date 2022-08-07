import sample_file
import pytest

@pytest.mark.temporary
def test_add_string():
    addition_of_strings = sample_file.addition("Python", "Batch")
    assert addition_of_strings == "Pythonatch"
    assert sample_file.addition("Pycharm", " 2022") == "Pycharm 2022"

@pytest.mark.skip(reason="Temporary purpose")
def test_product_string():
    multiplication_of_strings = sample_file.multiplication("Python", 2)
    assert multiplication_of_strings == "PythonPython"
    assert sample_file.multiplication("Pycharm", 3) == "PycharmPycharmPycharm"


