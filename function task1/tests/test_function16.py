import unittest
from function16 import length_of_set


class Testfunction16(unittest.TestCase):
    def test_function16(self):
        self.assertEqual(7, length_of_set())  # add assertion here


if __name__ == '__main__':
    unittest.main()
