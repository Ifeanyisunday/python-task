import unittest
from function3 import sum_of_even_index


class Testfunction3(unittest.TestCase):
    def test_function3(self):
        self.assertEqual(125, sum_of_even_index())  # add assertion here


if __name__ == '__main__':
    unittest.main()
