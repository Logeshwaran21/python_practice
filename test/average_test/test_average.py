import unittest

from python_practice.src.calculate_averge.util import average
class MyTestCase(unittest.TestCase):
    def test_average_valid(self):
        Input = average([1,2,3])
        output= 2.0
        self.assertEqual(Input,output,"Test_case passed")  # add assertion here
    def test_average_valid1(self):
        Input = average([0])
        output= "Zero Average Detected"
        self.assertEqual(Input,output,"Test_case passed")
    def test_average_valid_2(self):
        Input = average([22,24,25,67,71,81])
        output =48.33
        self.assertEqual(Input,output,"Test_case passed")
if __name__ == '__main__':
    unittest.main()
