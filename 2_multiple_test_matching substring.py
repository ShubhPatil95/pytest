# We can perform grouping in 2 ways:
#  1. Matching Substring
#  2. Applying Marker

#1. Matching Substring => run command to run specific test=> py.test -k method1 -v
import pytest

def test_method1():
    x=5
    y=7
    assert x==y

def test_method2():
    a=15
    b=20
    assert a+5==b


