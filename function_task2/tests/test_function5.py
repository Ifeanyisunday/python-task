import unittest
from function_task2.function5 import sum_of_third_index


class Testfunction5(unittest.TestCase):
    def test_function5(self):
        self.assertEqual(8380416, sum_of_third_index([32, 18, 24, 41, 16, 45, 31, 50, 22, 6]))  # add assertion here


if __name__ == '__main__':
    unittest.main()

