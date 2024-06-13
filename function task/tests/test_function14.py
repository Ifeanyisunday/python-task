import unittest
from function14 import clear_set


class Testfunction14(unittest.TestCase):
    def test_function14(self):
        self.assertEqual(None, clear_set())  # add assertion here


if __name__ == '__main__':
    unittest.main()
