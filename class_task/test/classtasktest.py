import unittest
from class_task import classtask


class MyTestCase(unittest.TestCase):
    def test_if_output_is_noduplicate(self):
        self.assertEqual([1, 2, 3, 4], classtask.noDuplicate1([1, 1, 2, 3, 3, 4]))

    def test_if_output_is_noduplicate1(self):
        self.assertEqual([6, 7, 8, 9], classtask.noDuplicate2([6, 7, 6, 8, 7, 9]))
    # add assertion here


if __name__ == '__main__':
    unittest.main()
