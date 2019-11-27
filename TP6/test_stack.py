import unittest
from app import *

class TestStack(unittest.TestCase):
    def testInit(self):
        stack = Stack(1)
        self.assertEqual(stack.max_size, 1)
        self.assertEqual(stack.n, 0)
    
    def test_isFull(self):
        stack = Stack(1)
        self.assertFalse(stack.isFull())
    
    def test_push_pop(self):
        stack = Stack(1)
        stack.push("value")
        item = stack.pop()
        self.assertEqual(item, "value")


if __name__ == '__main__':
    unittest.main()