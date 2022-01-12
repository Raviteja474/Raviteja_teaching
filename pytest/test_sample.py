import math
import pytest

@pytest.fixture
def input():
   value = 25
   return value

# sub test1
def test_sqrt(value_23):
   print(value_23,"**************************************************")
   num = 25
   assert math.sqrt(num) == 5
   #return None

# sub test2
def test_square():
   num = 7
   assert 7*7 == 49

# sub test3
def test_payment():
   assert 10 == 11

# sub test4
@pytest.mark.temp
def test_equality1(input):
   assert not input==25

# sub test5
def test_equality2(input):
   assert input==25



# marker_name user defined
# parameterize default/library support
# pytest -m studentverify -v
@pytest.mark.studentverify
@pytest.mark.parametrize("rollno,percentage", [(1485455,95),(2,36),(3,35),(4,24),(51,101)])
def test_student_pass(rollno,percentage):
   print(rollno,percentage)
   assert 1<=rollno<=1000
   assert 35<=percentage<=100

# Every test input is independent from others , if you go with for loop with iterations
# it will throw error,in case of single failure
# test_sample.py::test_student_pass[1485455-95] FAILED                                                                                                                                                        [ 20%]
# test_sample.py::test_student_pass[2-36] PASSED                                                                                                                                                              [ 40%]
# test_sample.py::test_student_pass[3-35] PASSED                                                                                                                                                              [ 60%]
# test_sample.py::test_student_pass[4-24] FAILED                                                                                                                                                              [ 80%]
# test_sample.py::test_student_pass[51-101] FAILED