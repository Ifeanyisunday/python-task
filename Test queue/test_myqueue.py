import unittest
from my_queue import Queue


class TestQueue(unittest.TestCase):
    def test_if_can_add_to_queue(self):
        my_queue = Queue()
        ##my_queue.add_to_queue(1)
        ##my_queue.add_to_queue(2)
        ##my_queue.add_to_queue(3)
        self.assertEqual([], my_queue.print_queue())

    def test_if_can_remove_from_queue(self):
        my_queue = Queue()
        my_queue.add_to_queue(1)
        my_queue.add_to_queue(2)
        my_queue.add_to_queue("sunday")
        my_queue.add_to_queue("guy")
        self.assertEqual([1, 2, "sunday", "guy"], my_queue.print_queue())
        my_queue.remove_from_queue()
        my_queue.remove_from_queue()
        my_queue.remove_from_queue()
        self.assertEqual(["guy"], my_queue.print_queue())



if __name__ == '__main__':
    unittest.main()
