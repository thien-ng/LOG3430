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
    

if __name__ == '__main__':
    unittest.main()