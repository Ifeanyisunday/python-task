import unittest
from function9 import len_string


class Testfunction9(unittest.TestCase):
    def test_function9(self):
        self.assertEqual(['epple', 'yherry', 'rear'], len_string())  # add assertion here


if __name__ == '__main__':
    unittest.main()
