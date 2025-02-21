# from unittest import TestCase

from Lab1.src.math_lib import is_perfect
from Lab1.src.math_lib import max


# class Test(TestCase):
def test_max(self) -> None:
    list1 = [1,2,3,4,5]
    result = max(list1)
    assert result == 5

def test_max_none(self) -> None:
    list2 = [2, 3, 5, 7, None]
    result = max(list2)
    assert result == None

def test_is_perfect(self) -> None:
    assert is_perfect(6) == True
    assert is_perfect(1) == False