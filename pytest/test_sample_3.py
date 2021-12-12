import pytest


@pytest.mark.xfail
def test_1():
    assert 111<10

@pytest.mark.xfail
def test_2():
    assert 1<10

@pytest.mark.skip
def test_3():
    assert 111 < 10

@pytest.mark.skip
def test_4():
    assert 9<10


def test_5():
    assert 1 < 10


def test_6():
    assert 11>10

def test_7():
    assert 1>10

def test_8():
    assert 1>10