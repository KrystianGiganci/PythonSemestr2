class Queue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, item):  # Dodanie do kolejki
        self.queue.append(item)

    def dequeue(self):        # Usunięcie z kolejki
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.queue)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())
print(queue.dequeue())
print(queue.size())
