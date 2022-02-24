import pytest

def func(x):
    return x+5

# assertation is nothing but CHECK which return either True or False
## if assert is failed then method execution will move to next step and break the curren test.
def test_method():
    assert func(3)==8

# run commnad => pytest 1_first_test.py 
