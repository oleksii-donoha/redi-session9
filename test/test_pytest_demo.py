from src.unittest_demo import hyperbolic_function


def test_negative():
    assert hyperbolic_function(-10) == -0.1


def test_positive():
    assert hyperbolic_function(10) == 0.1
   