import unittest
from function15 import find_largest_and_smallest


class Testfunction15(unittest.TestCase):
    def test_function15(self):
        self.assertEqual((9, 1), find_largest_and_smallest())  # add assertion here


if __name__ == '__main__':
    unittest.main()

