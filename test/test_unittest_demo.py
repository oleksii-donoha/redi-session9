import unittest

from src.unittest_demo import hyperbolic_function


class MyTestCase(unittest.TestCase):

    def test_negative(self):
        result = hyperbolic_function(-10)
        self.assertEqual(result, -0.1)

    def test_positive(self):
        result = hyperbolic_function(10)
        self.assertEqual(result, 0.1)


if __name__ == '__main__':
    unittest.main()
