import unittest
from function8 import smallest


class Testfunction8(unittest.TestCase):
    def test_function8(self):
        self.assertEqual(6, smallest())  # add assertion here


if __name__ == '__main__':
    unittest.main()
