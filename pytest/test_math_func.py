import math_func
# import pytest


# pytest .\test_math_func.py -s

def setup():
    print("Setup method will execute before every testcase")


def test_add():
    assert math_func.add(2, 3) == 5
    assert math_func.add(9, 2) == 11
    assert math_func.add(20, 30) == 50
    assert math_func.add(28, 32) == 60


# @pytest.mark.product
def test_product():
    assert math_func.product(2, 3) == 6
    assert math_func.product(10, 5) == 50
    assert math_func.product(10, 3) == 30


def test_add_strings():
    assert not math_func.add("ketharaju", "Sumanth") == "ketharajSumanth"
    assert math_func.add("Pamujula", "Sunil") == "PamujulaSunil"


def test_product_strings():
    assert not math_func.product("Sumanth", 2) == "Sumanth Sumanth"
    assert math_func.product("Pamujula", 2) == "PamujulaPamujula"
    assert math_func.product("Sunil", 2) == "SunilSunil"


def teardown():
    print("teardown method will execute after every testcase")
