import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
    
    def test_errors(self):
        try:
            Queue(5.5)
        except ValueError as error:
            self.assertEqual(str(error), 'invalid capacity input')

        q = Queue(5)
        try:
            q.dequeue()
        except IndexError as error:
            self.assertEqual(str(error), 'queue is empty')
        try:
            for i in range(6):
                q.enqueue(i)
        except IndexError as error:
            self.assertEqual(str(error), 'queue is full')
        try:
            q.change_cap_to(-1)
        except IndexError as error:
            self.assertEqual(str(error), 'invalid capacity input')
        try:
            q.change_cap_to(6.6)
        except ValueError as error:
            self.assertEqual(str(error), 'invalid capacity input')

    def test_functions(self):
        q = Queue(5)
        self.assertTrue(q.is_empty())
        self.assertEqual(5, q.size())

        for i in range(5):
            q.enqueue(i)
        self.assertTrue(q.is_full())
        q.change_cap_to(6)

        self.assertFalse(q.is_full())
        self.assertEqual(0, q.front)
        
        top_item = q.peek()
        self.assertEqual(top_item, q.dequeue())

if __name__ == '__main__':
    unittest.main()
