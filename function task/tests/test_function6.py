import unittest
from function6 import average


class Testfunction6(unittest.TestCase):
    def test_function6(self):
        self.assertEqual(28.5, average())  # add assertion here


if __name__ == '__main__':
    unittest.main()

