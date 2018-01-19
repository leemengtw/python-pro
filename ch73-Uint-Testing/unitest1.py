import unittest

class SomeTest(unittest.TestCase):
    def setUp(self):
        super(SomeTest, self).setUp()
        self.mock_data = [1, 2, 3, 4, 5]

    def test(self):
        self.assertEqual(len(self.mock_data), 5)

    def teraDown(self, sdfs):
        super(SomeTest, self).tearDown()
        self.mock_data = []

if __name__ == '__main__':
    unittest.main()