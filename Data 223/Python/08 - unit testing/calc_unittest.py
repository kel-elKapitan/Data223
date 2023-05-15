# create test using unittest in calc_unittest.py file with unittest

import unittest

from calc import Calculator



class Test_Calculator(unittest.TestCase):

    def setUp(self):
        self.Calc = Calculator()

    def test_add(self):
        result = self.Calc.add(8, 2)
        self.assertEqual(result.get_sum(), 10, 'Wrong Calculation.')

    def test_subtract(self):
        result = self.Calc.subtract(8, 2)
        self.assertEqual(result.get_difference(), 6, 'Wrong Calculation.')

    def test_multiply(self):
        result = self.Calc.multiply(8, 2)
        self.assertEqual(result.get_product(), 16, 'Wrong Calculation.')

    def test_divide(self):
        result = self.Calc.divide(8, 2)
        self.assertEqual(result.get_quotient(), 4, 'Wrong Calculation.')





if __name__ == '__main__':
    unittest.main()