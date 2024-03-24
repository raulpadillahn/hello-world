import unittest
from boot import calculate

class TestCalculator(unittest.TestCase):
 
    def test_sum(self):
        """
        Test that the sum calculation is correct.
        """
        result = calculate(5, 3)
        self.assertEqual(result["sum"], 8)  # Assert expected sum

    def test_difference(self):
        """
        Test that the difference calculation is correct.
        """
        result = calculate(10, 2)
        self.assertEqual(result["difference"], 8)  # Assert expected difference

    def test_product(self):
        """
        Test that the product calculation is correct.
        """
        result = calculate(4, 6)
        self.assertEqual(result["product"], 24)  # Assert expected product

    def test_quotient_positive(self):
        """
        Test that the quotient calculation is correct for positive divisor.
        """
        result = calculate(12, 3)
        self.assertEqual(result["quotient"], 4)  # Assert expected quotient

    def test_quotient_zero(self):
        """
        Test that the quotient calculation handles division by zero.
        """
        result = calculate(10, 0)
        self.assertEqual(result["quotient"], "Division by zero is not allowed!")  # Assert message for zero division

    def test_invalid_input(self):
        """
        Test that the function handles invalid input (non-numeric values).
        """
        self.assertIsNone(calculate("hello", 5))  # Assert None for invalid input
        self.assertIsNone(calculate(3, "world"))  # Assert None for invalid input

if __name__ == '__main__':
    unittest.main()