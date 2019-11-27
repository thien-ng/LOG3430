import unittest
from app import *

class TestList(unittest.TestCase):
    
    def setUp(self): 
        self.list = List()

    # Modifier le test pour ne pas prendre les nodes
    def testInit(self):
        self.assertEqual(self.list.n, 0)

    def test_isEmpty(self):
        self.assertTrue(self.list.isEmpty())

    def test_size(self):
        self.list.append("value")
        self.list.append("value2")
        self.assertEqual(self.list.size(), 2)

    def test_check(self):
        self.list.append("value")
        self.list.append("value2")
        self.assertEqual(self.list.check(), self.list.list[0])

    def test_peek(self):
        self.list.append("value")
        self.list.append("value2")
        self.assertEqual(self.list.peek(), "value")

    def test_append(self):
        self.list.append("value3")
        self.assertEqual(self.list.size(), 1)

    def test_prepend(self):
        self.list.prepend("value4")
        self.assertEqual(self.list.size(), 1)


if __name__ == '__main__':
    unittest.main()

