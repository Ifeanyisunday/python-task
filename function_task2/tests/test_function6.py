import unittest
from function_task2.function6 import average


class Testfunction6(unittest.TestCase):
    def test_function6(self):
        self.assertEqual(28.5, average([32, 18, 24, 41, 16, 45, 31, 50, 22, 6]))  # add assertion here


if __name__ == '__main__':
    unittest.main()

