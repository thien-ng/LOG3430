import unittest
from app import *

class TestLinkedList(unittest.TestCase):
    
    def setUp(self): 
        self.LinkedList = LinkedList()

    def testInit(self):
        self.assertIsNone(self.LinkedList.first)
        self.assertEqual(self.LinkedList.n, 0)

    def test_isEmpty(self):
        self.assertTrue(self.LinkedList.isEmpty())

    def test_size(self):
        self.LinkedList.append("value")
        self.LinkedList.append("value2")
        self.assertEqual(self.LinkedList.size(), 2)

    def test_check(self):
        self.LinkedList.append("value")
        self.LinkedList.append("value2")
        self.assertEqual(self.LinkedList.check(), self.LinkedList.first)

    def test_peek(self):
        self.LinkedList.append("value")
        self.LinkedList.append("value2")
        self.assertEqual(self.LinkedList.peek(), "value")

    def test_append(self):
        self.LinkedList.append("value3")
        self.assertEqual(self.LinkedList.size(), 1)

    def test_prepend(self):
        self.LinkedList.prepend("value4")
        self.assertEqual(self.LinkedList.size(), 1)


if __name__ == '__main__':
    unittest.main()

