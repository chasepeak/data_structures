import unittest
from heap import *

class TestMaxHeap(unittest.TestCase):
    def test_basic(self):
        heap = MaxHeap()
        list = [1,2,3,4,5,6,7,8,9,10]
        heap.build_heap(list)
        print(heap.get_contents())
    pass

class TestMinHeap(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
