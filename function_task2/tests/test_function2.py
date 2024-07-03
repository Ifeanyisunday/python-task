import unittest
from function_task2.function2 import find_length_without_len_function


class Testfunction2(unittest.TestCase):
    def test_function2(self):
        self.assertEqual(10, find_length_without_len_function([32, 18, 24, 41, 16, 45, 31, 50, 22, 6]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
