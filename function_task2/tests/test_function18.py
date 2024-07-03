import unittest
from function_task2.function18 import collect_10_numbers, sum_collection, remove_item, find_intersection


class TestFunction18(unittest.TestCase):
    def test_collect_10_numbers(self):
        self.assertEqual(45, collect_10_numbers())

    def test_sum_collection(self):
        self.assertEqual(45, sum_collection({1, 2, 3, 4, 5, 6, 7, 8, 9}))

    def test_remove_item(self):
        self.assertEqual(None, remove_item({1, 2, 3, 4, 5, 6, 7, 8, 9}, {2, 4, 6, 8, 10}))

    def test_find_intersection(self):
        self.assertEqual(None, find_intersection({1, 2, 3, 4, 5, 6, 7, 8, 9}, {2, 4, 6, 8, 10}))


if __name__ == '__main__':
    unittest.main()
