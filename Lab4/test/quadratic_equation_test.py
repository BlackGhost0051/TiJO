import unittest
from Lab4.src.quadratic_equation import QuadraticEquation

class QuadraticEquationTestCase(unittest.TestCase):
    def test_raise_error_when_a_is_zero(self):
        # arrange
        a, b, c = 0, 2, 4

        self.assertRaises(ValueError, QuadraticEquation, a, b, c)

    def test_no_error(self):
        # arrange
        a, b, c = 1, 2, 4

        self.assertNotEqual(QuadraticEquation(a, b, c), None)

    def test_two_real_solutions(self):
        # arrange
        a, b, c = 1, -3, 2

        eq = QuadraticEquation(a, b, c)

        solutions = eq.solve()

        self.assertEqual(len(solutions), 2)
        self.assertAlmostEqual(solutions[0], 2.0)
        self.assertAlmostEqual(solutions[1], 1.0)

    def test_no_real_solutions(self):
        # arrange
        a, b, c = 1, 1, 1

        eq = QuadraticEquation(a, b, c)

        solutions = eq.solve()

        self.assertIsNone(solutions)

    def test_one_real_solution(self):
        # arrange
        a, b, c = 1, -2, 1
        eq = QuadraticEquation(a, b, c)

        solutions = eq.solve()

        self.assertEqual(len(solutions), 1)
        self.assertAlmostEqual(solutions[0], 1.0)

if __name__ == '__main__':
    unittest.main()