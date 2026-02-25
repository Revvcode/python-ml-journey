# assert keyword can be used to test code chunks and returns boolean values, gives an AssertionError
# pytest is a useful library for testing (3rd party, need to install), use it with pytest "file-name or path"

import pytest
from bettercalculator import square


def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")