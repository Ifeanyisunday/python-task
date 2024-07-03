import unittest
from function_task2.function19 import add_to_dictionary, display_by_keys, display_by_values, display_sum_of_all_ages


class MyTestCase(unittest.TestCase):
    def test_add_to_dictionary(self):
        self.assertEqual(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z'], add_to_dictionary())

    def test_display_by_keys(self):
        self.assertEqual(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z'], display_by_keys())

    def test_display_by_values(self):
        self.assertEqual(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z'], display_by_values())

    # add assertion here

    def test_display_sum_of_all_ages(self):
        self.assertEqual(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z'], display_sum_of_all_ages())


if __name__ == '__main__':
    unittest.main()
