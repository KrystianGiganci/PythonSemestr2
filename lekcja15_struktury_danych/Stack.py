class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        # if len(self.stack) == 0:
        #     return True
        # else:
        #     return False
        return self.size() == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.pop())  # 4
print(stack.peek())
print(stack.pop())
print(stack.is_empty())
print(stack.size())
print(stack.pop())
