from pysum.pysum import sum

def test_sum_two_mumbers():
    assert sum(1, 2) == 3

def test_sum_zero():
    assert sum(0, 2) == 2

