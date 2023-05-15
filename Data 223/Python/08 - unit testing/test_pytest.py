# test cases for pytest

import pytest

from demo_pytest import convert_string_to_int
from demo_pytest import add
from demo_pytest import get_dict_keys


def test_convert_string_to_int():
    result = convert_string_to_int("2,456,543,2345")
    assert result == 24565432345
    # if assert statement if False, it throws an assertion error


# sample function to test
def test_add():
    result = add(2,3)
    assert result == 5

# sample function ({'a':1,'b':2})
def test_get_dict_keys():
    input_dict = {"a": 1, "b": 2}
    actual = get_dict_keys(input_dict)
    expected = ["a","b"]
    assert actual == expected
    #assert result == ["a", "b"]

def test_get_dict_keys_with_message():
    input_dict = {"a": 1, "b": 2}
    actual = get_dict_keys(input_dict)
    expected = ["a","b"]
    assert actual == expected
    assert actual == expected, f"Actual value is {actual} and not equal to {expected}"
    #assert result == ["a", "b"]
    input_dict = {"a": 1, "b": 2}