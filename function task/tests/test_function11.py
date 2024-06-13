import unittest
from function11 import add_element


class Testfunction11(unittest.TestCase):
    def test_function11(self):
        self.assertEqual(64, add_element())  # add assertion here


if __name__ == '__main__':
    unittest.main()
