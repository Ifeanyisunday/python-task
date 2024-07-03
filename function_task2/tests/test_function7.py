import unittest
from function_task2.function7 import largest


class Testfunction7(unittest.TestCase):
    def test_function7(self):
        self.assertEqual(50, largest([32, 18, 24, 41, 16, 45, 31, 50, 22, 6]))  # add assertion here


if __name__ == '__main__':
    unittest.main()