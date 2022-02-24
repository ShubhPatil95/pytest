# We can perform grouping in 2 ways:
#  1. Matching Substring
#  2. Applying Marker

#1. Applying Marker=> run command to run specific test=> py.test -m anyname1
import pytest

pytest.mark.anyname1
def test_method1():
    x=5
    y=7
    assert x==y

pytest.mark.anyname2
def test_method2():
    a=15
    b=20
    assert a+5==b


