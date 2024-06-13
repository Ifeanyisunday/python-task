import unittest
from function7 import largest


class Testfunction7(unittest.TestCase):
    def test_function7(self):
        self.assertEqual(50, largest())  # add assertion here


if __name__ == '__main__':
    unittest.main()