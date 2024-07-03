import unittest
from function_task2.function14 import clear_set


class Testfunction14(unittest.TestCase):
    def test_function14(self):
        self.assertEqual(None, clear_set({1, 2, 3, 4, 5}))  # add assertion here


if __name__ == '__main__':
    unittest.main()
