from math_series import __version__
from math_series.math_series import *


def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci():
    actual1= fibonacci(-10)
    actual2= fibonacci(0)
    actual3= fibonacci(1)
    actual4= fibonacci(5)
    actual5= fibonacci(7)
    actual6= fibonacci("7")

    expected1= "invalid input"
    expected2= 0
    expected3= 1
    expected4= 5
    expected5= 13
    expected6= "invalid input"

    assert actual1==expected1
    assert actual2==expected2
    assert actual3==expected3
    assert actual4==expected4
    assert actual5==expected5
    assert actual6==expected6


def test_lucas():
    actual1= lucas(-4)
    actual2= lucas(0)
    actual3= lucas(1)
    actual4= lucas(5)
    actual5= lucas(7)
    actual6= lucas("9")

    expected1= "invalid input"
    expected2= 2
    expected3= 1
    expected4= 11
    expected5= 29
    expected6= "invalid input"

    assert actual1==expected1
    assert actual2==expected2
    assert actual3==expected3
    assert actual4==expected4
    assert actual5==expected5
    assert actual6==expected6

def test_sum_series():
    actual1= sum_series(-4)
    actual2= sum_series(0)
    actual3= sum_series(1)
    actual4= sum_series(5)
    actual5= sum_series(5,10,10)
    actual6= sum_series(1,1,2)
    actual7= sum_series("1",1,2)

    expected1= "invalid input"
    expected2= 0
    expected3= 1
    expected4= 5
    expected5= 80
    expected6= 2
    expected7= "invalid input"


    assert actual1==expected1
    assert actual2==expected2
    assert actual3==expected3
    assert actual4==expected4
    assert actual5==expected5
    assert actual6==expected6
    assert actual7==expected7

