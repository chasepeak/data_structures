'''
Chase M. Peak
-binary tree  abstract data structure testing
'''

import unittest
from binary_tree import *

class TestBinaryTree(unittest.TestCase):

    def test_01(self):
        tree = BinaryTree()
        self.assertTrue(tree.is_empty())
        tree.insert(4,'data0')
        tree.insert(3,'data1')
        tree.insert(2,'data2')
        print(tree)
        self.assertFalse(tree.search(1))
        #self.assertEqual(tree.get_data(3), 'data1')

        tree.insert(5,'data3')
        self.assertTrue(tree.search(5))
        self.assertEqual(tree.get_data(5), 'data3')
        self.assertEqual(tree.find_min(), 2)
        self.assertEqual(tree.find_max(), 5)

if __name__ == '__main__':
    unittest.main()
