import unittest
from function12 import union_of_two_sets


class Testfunction12(unittest.TestCase):
    def test_function12(self):
        self.assertEqual({2, 3, 4, 5, 6, 7, 8}, union_of_two_sets())  # add assertion here


if __name__ == '__main__':
    unittest.main()