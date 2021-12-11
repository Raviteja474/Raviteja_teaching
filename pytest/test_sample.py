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