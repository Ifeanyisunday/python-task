import unittest
from function4 import sum_of_odd_index


class Testfunction4(unittest.TestCase):
    def test_function4(self):
        self.assertEqual(160, sum_of_odd_index())  # add assertion here


if __name__ == '__main__':
    unittest.main()
