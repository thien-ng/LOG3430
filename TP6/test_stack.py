import unittest
from app import *

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(4)

    def test_init(self):
        self.assertEqual(self.stack.max_size, 4)
        self.assertEqual(self.stack.n, 0)
        self.assertEqual(self.stack.list, [])           

    def test_isFull(self):
        self.assertFalse(self.stack.isFull())
    
    def test_push(self):
        self.stack.push("value")
        self.assertEqual(self.stack.size(), 1)
if __name__ == '__main__':
    unittest.main()