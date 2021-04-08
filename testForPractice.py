import unittest
import practice

class TestCap(unittest.TestCase):
    def test_tuplesDouble(self):
        """It should return a list of tuples, and each tuple 
           should be paired with its corresponding square value"""
        input = [1, 2, 3]
        result = practice.tuplesDouble(input)
        self.assertEqual(result,[(1, 1), (2, 4), (3, 9)])

    def test_tuplesFunction(self):
        """It should return a list of tuples, and each tuple 
           should be paired with its corresponding function output"""
        input = [1, 2, 3]
        myfunc = practice.exampleExponential
        result = practice.tuplesFunction(input,myfunc)
        self.assertEqual(result,[(1, 1), (2, 4), (3, 9)])
    
if __name__ == '__main__':
    unittest.main()
