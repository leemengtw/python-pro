import mymath
import unittest

class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """

    def test_add_integers(self):
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_strings(self):
        result = mymath.add('abc', 'def')
        self.assertEqual(result, 'abcdef')

    def this_method_will_not_be_called(self):
        print('Catch me if you can.')

if __name__ == '__main__':
    unittest.main()
