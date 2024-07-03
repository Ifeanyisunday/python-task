import unittest
from function_task2.function11 import add_element


class Testfunction11(unittest.TestCase):
    def test_function11(self):
        self.assertEqual(64, add_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
))  # add assertion here


if __name__ == '__main__':
    unittest.main()
