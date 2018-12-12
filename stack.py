class Stack():
    
    def __init__(self, capacity):
        try:
            self.capacity = int(capacity)
            self.items = [None] * capacity
            self.num_items = 0
        except:
            raise ValueError('enter an integer value')


    def is_empty(self):
        return self.num_items == 0

    def is_full(self):
        return self.num_items == self.capacity

    def push(self, item):
        if self.is_full():
            raise IndexError('stack is full')
        self.items[self.num_items] = item
        self.num_items += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('stack is empty')
        self.num_items -= 1
        return self.items[self.num_items]

    def size(self):
        return self.capacity

    def peek(self):
        return self.items[self.num_items - 1]

    def change_cap_to(self, capacity):
        if type(capacity) != int or capacity <= 0:
            raise ValueError('invalid input for capacity')
        self.items += [None] * abs(self.capacity - capacity)
        self.capacity = capacity
