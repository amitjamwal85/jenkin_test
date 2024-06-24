import unittest

# Function to be tested
def add_numbers(a, b):
    return a + b

# Test case class
class TestAddNumbers(unittest.TestCase):

    # Test case: test addition of positive numbers
    def test_add_positive_numbers(self):
        result = add_numbers(5, 10)
        self.assertEqual(result, 15)

    # Test case: test addition of negative numbers
    def test_add_negative_numbers(self):
        result = add_numbers(-3, -7)
        self.assertEqual(result, -10)

    # Test case: test addition of a positive and a negative number
    def test_add_positive_and_negative_numbers(self):
        result = add_numbers(8, -4)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()

