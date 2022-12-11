class Stack:

    def __init__(self: list):
        self.stack = []

    def is_empty(self):
        return not self.stack

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
