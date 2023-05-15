# create unit test cases for the class using pytest in calc.py file



import pytest

from calc import Calculator


def test_add():
    Calc = Calculator()
    my_add = Calc.add(2,3)
    assert my_add == 5


def test_subtract():
    
    Calc = Calculator()
    result = Calc.subtract(2,3)
    assert result == -1


def test_multiply():
    Calc = Calculator()
    result = Calc.multiply(2,3)
    assert result == 6


def test_divide():
    Calc = Calculator()
    result = Calc.divide(9,3)
    assert result == 3.0

