'''
Chase M. Peak
-ordered list abstract data structure
-array-based implementation
'''

class MaxHeap:
    def __init__(self, capacity = 50):
        self.capacity = capacity
        self.items = [None] * (capacity + 1)
        self.num_items = 0

    def is_empty(self):
        return self.num_items == 0


    def is_full(self):
        return self.num_items == self.capacity


    def get_size(self):
        return self.num_items


    def get_capacity(self):
        return self.capacity


    def peek(self):
        if not self.is_empty():
            return self.items[1]


    def enqueue(self, data):
        if self.is_full():
            raise IndexError
        self.num_items += 1
        self.items[self.num_items] = data
        self.perc_up(self.num_items)



    def dequeue(self):
        if not self.is_empty():
            max = self.items[1]
            self.items[1], self.items[self.num_items] = self.items[self.num_items], self.items[1]
            self.num_items -= 1
            self.perc_down(1)
            return max


    def build_heap(self, alist): #bottom up heap construction
        if len(alist) > self.capacity:
            self.capacity = len(alist) + 1
        self.items = alist
        self.num_items = len(alist)
        for i in range(len(alist), 0, -1):
            if 2 * i <= self.num_items:
                self.perc_down(i)


    def perc_up(self, index):
        return self.rec_perc_up(index)

    def rec_perc_up(self, index):
        if index > 1 and self.items[index // 2] < self.items[index]:
            self.items[index], self.items[index // 2] = self.items[index // 2], self.items[index]
            index = index // 2


    def perc_down(self, index):
        lchild = self.items[2 * index]
        rchild = self.items[(2 * index) + 1]
        while lchild and rchild and (self.items[index] <= lchild or self.items[index] <= rchild):
            if rchild and lchild > rchild:
                self.items[index], self.items[index * 2] = self.items[index * 2], self.items[index]
                index = index * 2
            elif self.items[index] < lchild:
                self.items[index], self.items[index * 2] = self.items[index * 2], self.items[index]
            else:
                self.items[index], self.items[(index * 2) + 1] = self.items[(index * 2) + 1], self.items[index]
                index = (index * 2) + 1
            lchild = self.items[index * 2]
            rchild = self.items[(index * 2) + 1]


class MinHeap:
    def __init__(self, capacity = 50):
        self.capacity = capacity
        self.items = [None] * (capacity + 1)
        self.num_items = 0

    def is_empty(self):
        return self.num_items == 0


    def is_full(self):
        return self.num_items == self.capacity


    def get_size(self):
        return self.num_items


    def get_capacity(self):
        return self.capacity


    def peek(self):
        if not self.is_empty():
            return self.items[1]


    def enqueue(self, data):
        if self.is_full():
            raise IndexError
        self.num_items += 1
        self.items[self.num_items] = data
        self.perc_up(self.num_items)


    def dequeue(self):
        if not self.is_empty():
            min = self.items[1]
            self.items[1], self.items[self.num_items] = self.items[self.num_items], self.items[1]
            self.num_items -= 1
            self.perc_down(1)
            return min


    def build_heap(self, alist): #bottom up heap construction
        if len(alist) > self.capacity:
            self.capacity = len(alist) + 1
        self.items = alist
        self.num_items = len(alist)
        for i in range(len(alist), 0, -1):
            if 2 * i <= self.num_items:
                self.perc_down(i)

    def perc_up(self, index):
        return self.rec_perc_up(index)

    def rec_perc_up(self, index):
        if index > 1 and self.items[index // 2] > self.items[index]:
            self.items[index], self.items[index // 2] = self.items[index // 2], self.items[index]
            index = index // 2


    def perc_down(self, index):
        lchild = self.items[2 * index]
        rchild = self.items[(2 * index) + 1]
        while lchild and rchild and (self.items[index] >= lchild or self.items[index] >= rchild):
            if rchild and lchild < rchild: #made this less than (instead of greather than)
                self.items[index], self.items[index * 2] = self.items[index * 2], self.items[index]
                index = index * 2
            elif self.items[index] > lchild: #made this greater than (instead of less than)
                self.items[index], self.items[index * 2] = self.items[index * 2], self.items[index]
            else:
                self.items[index], self.items[(index * 2) + 1] = self.items[(index * 2) + 1], self.items[index]
                index = (index * 2) + 1
            lchild = self.items[index * 2]
            rchild = self.items[(index * 2) + 1]
