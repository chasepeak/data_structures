import unittest
from ordered_list import *

class TestOrderedList(unittest.TestCase):

    def test_errors(self):
        alist = OrderedList()
        with self.assertRaises(IndexError):
            alist.pop(0)
        alist.add(1)
        with self.assertRaises(IndexError):
            alist.pop(2)


    def test_functions(self):
        alist = OrderedList()
        self.assertTrue(alist.is_empty())
        self.assertFalse(alist.remove(None))

        blist = [1,3,2,5,4]
        for i in blist:
            alist.add(i)
        
        self.assertEqual(alist.size(), len(blist))
        self.assertEqual(alist.list_asc(), sorted(blist))
        self.assertEqual(alist.list_desc(), sorted(blist)[::-1])

        self.assertTrue(alist.search(4))
        self.assertFalse(alist.search(6))
        self.assertEqual(alist.pop(0), 1)
        self.assertTrue(alist.size(), len(blist) - 1)

        self.assertEqual(alist.index(2), 0)
        self.assertEqual(alist.index(10), None)
        

if __name__ == '__main__':
    unittest.main()
