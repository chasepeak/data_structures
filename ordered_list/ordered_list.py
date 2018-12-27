'''
Chase M. Peak
-ordered list abstract data structure
-linked-based implementation
-doubly-linked list
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class OrderedList:
    def __init__(self):
        dummy = Node(None)
        dummy.next = dummy
        dummy.prev = dummy

        self.dummy = dummy


    def is_empty(self):
        return self.dummy.next == self.dummy


    def add(self, item):
        new_node = Node(item)
        current_node = self.dummy.next

        while current_node.next != self.dummy and new_node.data > current_node.next.data:
            current_node = current_node.next
        current_node.next.prev = new_node
        new_node.next = current_node.next
        current_node.next = new_node
        new_node.prev = current_node


    def remove(self, item):
        if self.is_empty():
            return False
        new_node = Node(item)
        current_node = self.dummy.next
        for i in range(self.size()):
            if current_node.data == new_node.data:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                return True
            elif current_node.data > new_node.data:
                return False
            current_node = current_node.next


    def index(self, item):
        current_node = self.dummy.next
        counter = 0
        for i in range(self.size()):
            if current_node.data == item:
                return counter
            elif current_node.data > item:
                return None
            counter += 1
            current_node = current_node.next
        if current_node.data == item:
            return counter


    def pop(self, index):
        if index < 0 or index >= self.size():
            raise IndexError
        current_node = self.dummy.next
        for i in range(index):
            current_node = current_node.next
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        return current_node.data


    def search(self, item):
        return self.rec_search(item, self.dummy)


    def rec_search(self, target, current_node):
        if current_node.data == target:
            return True
        elif current_node.next == self.dummy and current_node.data != target:
            return False
        return self.rec_search(target, current_node.next)


    def list_asc(self):
        alist = []
        current_node = self.dummy.next
        for i in range(self.size()):
            alist.append(current_node.data)
            current_node = current_node.next
        return alist


    def list_desc(self):
        return self.rec_list_desc([], self.dummy.prev)


    def rec_list_desc(self, list, current_node):
        if current_node == self.dummy:
            return list
        list.append(current_node.data)
        return self.rec_list_desc(list, current_node.prev)


    def size(self):
        return self.rec_size(self.dummy.next)


    def rec_size(self, current_node):
        if current_node == self.dummy:
            return 0
        return 1 + self.rec_size(current_node.next)
