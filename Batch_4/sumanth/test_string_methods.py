import sample_file
import pytest

@pytest.mark.parametrize("input_1, input_2, output", [("Pycharm", " 2022", "Pycharm 2022"),
                                                      ("Pycharm", " 2020", "Pycharm 2020")])
def test_add_string(input_1, input_2, output):
    assert sample_file.addition(input_1, input_2) == output




