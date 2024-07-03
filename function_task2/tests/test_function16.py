import unittest
from function_task2.function16 import length_of_set


class Testfunction16(unittest.TestCase):
    def test_function16(self):
        self.assertEqual(7, length_of_set({3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}))  # add assertion here


if __name__ == '__main__':
    unittest.main()
