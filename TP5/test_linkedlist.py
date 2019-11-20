import unittest
from app import *

class TestLinkedList(unittest.TestCase):
     def setUp(self):
        self.LinkedList = LinkedList()

    def testInit(self):
        self.assertIsNone(self.LinkedList.first)
        self.assertEqual(self.LinkedList.n, 0)

    def test_isEmpty(self):
        self.assertEqual(self.LinkedList.isEmpty(), 0)

    def test_size(self):
        self.LinkedList.append("value")
        self.LinkedList.append("value2")
        self.assertEqual(self.LinkedList.size(), 2)

    def test_check(self):
        self.assertEqual(linkedList.check(), linkedList.first)

    def test_peek(self):
        self.assertEqual(linkedList.peek(), "value")

    def test_append(self):
        self.LinkedList.append("value3")
        self.assertEqual(self.LinkedList.size(), 2)

    def test_prepend(self):
        self.LinkedList.prepend("value4")
        self.assertEqual(self.LinkedList.size(), 3)

    def test_accept(self): # comment faut il le tester?

if __name__ == '__main__':
    unittest.main()

