import unittest
from function2 import find_length_without_len_function


class Testfunction2(unittest.TestCase):
    def test_function2(self):
        self.assertEqual(10, find_length_without_len_function())  # add assertion here


if __name__ == '__main__':
    unittest.main()
