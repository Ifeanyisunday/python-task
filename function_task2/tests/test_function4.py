import unittest
from function_task2.function4 import sum_of_odd_index


class Testfunction4(unittest.TestCase):
    def test_function4(self):
        self.assertEqual(160, sum_of_odd_index([32, 18, 24, 41, 16, 45, 31, 50, 22, 6]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
