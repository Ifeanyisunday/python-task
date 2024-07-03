import unittest
from function_task2.function9 import same_string


class Testfunction9(unittest.TestCase):
    def test_function9(self):
        self.assertEqual(['epple', 'yherry', 'rear'], same_string(["epple", "Banana", "yherry", "Orange", "rear"]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
