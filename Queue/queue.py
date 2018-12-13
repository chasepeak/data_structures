class Queue():

    def __init__(self, capacity):
        if type(capacity) != int:
            raise ValueError('invalid capacity input')
        self.capacity = int(capacity)
        self.items = [None] * capacity
        self.num_items = 0
        self.front = 0 #keep track of front index

    def is_empty(self):
        return self.num_items == 0

    def is_full(self):
        return self.num_items == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise IndexError('queue is full')
        self.items[(self.num_items + self.front) % self.capacity] = item
        self.num_items += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('queue is empty')
        self.front = (self.front + 1) % self.capacity
        self.num_items -= 1
        return self.items[self.front - 1]

    def size(self):
        return self.capacity

    def change_cap_to(self, capacity):
        if self.num_items > capacity:
            raise IndexError('invalid capacity input')
        elif type(capacity) != int:
            raise ValueError('invalid capacity input')
        first_half = self.items[self.front:]
        second_half = self.items[:self.front]
        self.items = first_half + second_half + [None] * abs(capacity - self.capacity)
        self.capacity = capacity
        self.front = 0

    def peek(self):
        return self.items[self.front]
