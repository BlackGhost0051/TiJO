import unittest

from Lab2.src.Calc import Calc

class TestCalc(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.calc = Calc()

    def test_add(self):
        print("test_add")
        result = self.calc.add(3, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        print("test_divide_by_zero")
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def tearDown(self):
        print("tearDown\n")
        self.calc = None

if __name__ == '__main__':
    unittest.main()