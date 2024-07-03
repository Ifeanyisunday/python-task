import unittest
from function_task2.function8 import smallest


class Testfunction8(unittest.TestCase):
    def test_function8(self):
        self.assertEqual(6, smallest([32, 18, 24, 41, 16, 45, 31, 50, 22, 6]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
