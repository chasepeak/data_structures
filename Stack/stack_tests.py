'''
Chase M. Peak
-stack abstract data structure testing
'''

import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    
    def test_errors(self):
        try:
            Stack(5.5)
        except ValueError as error:
            self.assertEqual(str(error), 'invalid capacity input')

        s = Stack(5)
        try:
            s.pop()
        except IndexError as error:
            self.assertEqual(str(error), 'stack is empty')
        try:
            for i in range(6):
                s.push(i)
        except IndexError as error:
            self.assertEqual(str(error), 'stack is full')
        try:
            s.resize(-1)
        except IndexError as error:
            self.assertEqual(str(error), 'invalid capacity input')
        try:
            s.resize(6.6)
        except ValueError as error:
            self.assertEqual(str(error), 'invalid capacity input')
    def test_functions(self):
        s = Stack(5)
        self.assertTrue(s.is_empty())
        self.assertEqual(5, s.size())

        for i in range(5):
            s.push(i)
        top_item = s.peek()
        self.assertEqual(top_item, 4)
        self.assertEqual(top_item, s.pop())

if __name__ == '__main__':
    unittest.main()
