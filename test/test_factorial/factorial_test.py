import unittest

from python_practice.src.factorial.util import factorial

class MyTestCase(unittest.TestCase):
    def test_average_valid_1(self):
        Input = factorial(5)
        output= 120
        self.assertEqual(Input,output)
    def test_average_valid_2(self):
        Input = factorial(10)
        output= 3628800
        self.assertEqual(Input,output)
    def test_average_valid_3(self):
        Input = factorial(12)
        output= 479001600
        self.assertEqual(Input,output)

if __name__ == '__main__':
    unittest.main()