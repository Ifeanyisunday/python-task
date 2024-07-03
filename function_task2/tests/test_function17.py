import unittest
from function_task2.function17 import add_to_tuple, add_odd_index, add_even_index, add_largest_and_smallest, unpack_tuple


class Testfunction17(unittest.TestCase):
    def test_function17_add_tuple(self):
        self.assertEqual((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20), add_to_tuple())

    def test_function17_add_odd_index(self):
        self.assertEqual(110, add_odd_index())

    def test_function17_add_even_index(self):
        self.assertEqual(100, add_even_index())

    def test_function17_add_largest_and_smallest(self):
        self.assertEqual(21, add_largest_and_smallest())

    def test_function17_unpack_tuple(self):
        self.assertEqual(12345, unpack_tuple())


if __name__ == '__main__':
    unittest.main()
