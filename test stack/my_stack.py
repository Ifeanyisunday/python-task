class Stack:
    def __init__(self):
        self.stack = []

    def add_to_stack(self, element):
        if self.stack is []:
            return self.if_queue_is_empty()
        elif element not in self.stack:
            self.stack.append(element)

    def remove_from_stack(self):
        if self.stack is []:
            return self.if_queue_is_empty()
        else:
            self.stack.pop()

    def if_queue_is_empty(self):
        return len(self.stack) == 0

    def print_stack(self):
        return self.stack
