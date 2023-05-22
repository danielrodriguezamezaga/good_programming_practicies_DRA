# by Daniel Rodriguez Amezaga
# 5 tests with pytest for the file funciones.py
# python -m pip install pytest

from operations import sum, subtract, multiply, remainder, string_length, tuple_length

def test_sum():
    assert sum(2,7) == 9
    
def test_():
    assert multiply(10,10) == 100
    
def test_subtract():
    assert subtract(8,2) == 6

def test_remainder():
    assert remainder(8,2) == 0
    
def test_string_length():
    assert string_length(("Daniel", "Dani")) == 2
    
def test_tuple_length():
    assert tuple_length("Daniel") == 6
