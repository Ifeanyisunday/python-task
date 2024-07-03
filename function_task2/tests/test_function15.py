import unittest
from function_task2.function15 import find_largest_and_smallest


class Testfunction15(unittest.TestCase):
    def test_function15(self):
        self.assertEqual((9, 1), find_largest_and_smallest({3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}))  # add assertion here


if __name__ == '__main__':
    unittest.main()

