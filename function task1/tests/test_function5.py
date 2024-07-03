import unittest
from function5 import sum_of_third_index


class Testfunction5(unittest.TestCase):
    def test_function5(self):
        self.assertEqual(8380416, sum_of_third_index())  # add assertion here


if __name__ == '__main__':
    unittest.main()

