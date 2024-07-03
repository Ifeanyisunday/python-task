import unittest
from my_stack import Stack


class TestStack(unittest.TestCase):
    def test_add_to_stack(self):
        stack = Stack()
        stack.add_to_stack("guy")
        stack.add_to_stack(22)
        stack.add_to_stack("mr s.k")
        stack.add_to_stack(10)
        self.assertEqual(["guy", 22, "mr s.k", 10], stack.print_stack())

    def test_remove_from_stack(self):
        stack = Stack()
        stack.add_to_stack("guy")
        stack.add_to_stack(22)
        stack.add_to_stack("mr s.k")
        stack.add_to_stack(10)
        stack.remove_from_stack()
        self.assertEqual(["guy", 22, "mr s.k"], stack.print_stack())
        stack.remove_from_stack()
        self.assertEqual(["guy", 22,], stack.print_stack())
    # add assertion here


if __name__ == '__main__':
    unittest.main()
