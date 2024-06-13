import unittest
from function10 import sequential_collection


class Testfunction10(unittest.TestCase):
    def test_function10(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], sequential_collection())  # add assertion here


if __name__ == '__main__':
    unittest.main()
