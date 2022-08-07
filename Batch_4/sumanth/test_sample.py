import sample_file
import pytest

@pytest.mark.temporary
def test_add_int():
    addition_result = sample_file.addition(4, 5)
    assert addition_result == 9
    assert sample_file.addition(10, 50) == 60
    assert sample_file.addition(16, 14) == 10

@pytest.mark.skipif()
def test_add_folat():
    addition_result = sample_file.addition(3.2, 2.4)
    assert addition_result == 5.6
