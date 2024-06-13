import unittest
from function1 import collection_of_number


class Testfunction1(unittest.TestCase):
    def test_function1(self):
        self.assertEqual([32, 18, 24, 41, 16, 45, 31, 50, 22, 6], collection_of_number())  # add assertion here


if __name__ == '__main__':
    unittest.main()
