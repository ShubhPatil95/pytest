import pytest

## fixtured fucntion can be reused any methods
@pytest.fixture 
def number():
    a=10
    b=20
    c=25
    return [a,b,c]

def test_method1(number):
    x=15
    assert number[0]==x

def test_method2(number):
    y=20
    assert number[1]==y


def test_method3(number):
    z=25
    assert number[2]==z


## to skip that test
@pytest.fixture
## it will not add it to failed count(even failed) instead xfaild count
@pytest.xfail


