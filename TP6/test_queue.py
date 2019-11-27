import unittest
from app import *

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.Queue = Queue(2)
    
    def testInit(self):
        self.assertTrue(self.Queue)

    def testEnqueue(self):
        self.Queue.enqueue(2)
        self.assertEqual(self.Queue.first.__str__(),'2')

    def testDequeue(self):
        self.Queue.enqueue(1)
        self.Queue.enqueue(2)
        self.assertEqual(self.Queue.dequeue(),1)

    def testisFull(self):
        self.Queue.enqueue(1)
        self.Queue.enqueue(2)
        self.assertTrue(self.Queue.isFull())




if __name__ == '__main__':
    unittest.main()