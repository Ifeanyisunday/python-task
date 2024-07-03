import unittest
from function_task2.function13 import subset_of_two_sets


class Testfunction13(unittest.TestCase):
    def test_function13(self):
        self.assertEqual(False, subset_of_two_sets({6, 4, 3, 4, 8}, {2, 3, 5, 4, 5, 6, 7}))  # add assertion here


if __name__ == '__main__':
    unittest.main()