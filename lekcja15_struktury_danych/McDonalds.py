from Queue import Queue


class Customer:
    def __init__(self, name, order) -> None:
        self.name = name
        self.order = order


class McDQueue:
    def __init__(self) -> None:
        self.queue = Queue()

    def is_empty(self):
        return self.queue.is_empty()

    def add_customer(self, name, order):
        customer = Customer(name, order)
        self.queue.enqueue(customer)

    def remove_customer(self):
        if not self.is_empty():
            return self.queue.dequeue()

    def next_customer_order(self):
        if not self.is_empty():
            next_customer = self.queue.peek()
            return next_customer.order

queue = McDQueue()

queue.add_customer('Krystian', 'hamburger')
queue.add_customer('Mati', 'frytki')
queue.add_customer('Ola', 'cola')
queue.add_customer('Marysia', 'cheeseburger')

while not queue.is_empty():
    next_customer = queue.remove_customer()
    print(f'Obsługujemy klienta {next_customer.name}, który zamówił {next_customer.order}')

    if not queue.is_empty():
        next_order = queue.next_customer_order()
        print(f'Nastepny klient zamowił {next_order}\n\n')
