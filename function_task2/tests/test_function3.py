import unittest
from function_task2.function3 import sum_of_even_index


class Testfunction3(unittest.TestCase):
    def test_function3(self):
        self.assertEqual(125, sum_of_even_index([32, 18, 24, 41, 16, 45, 31, 50, 22, 6]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
