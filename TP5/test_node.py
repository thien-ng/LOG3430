import unittest
from app import *

class TestNode(unittest.TestCase):

    def testInit(self):
        node = Node("value")
        self.assertEqual(node.value, "value")
        self.assertIsNone(node.next)
    
    def testStr(self):
        node = Node("value")
        self.assertEqual(node.__str__(), "value")

if __name__ == '__main__':
    unittest.main()

