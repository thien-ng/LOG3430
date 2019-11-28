import unittest
from app import *

class TestAutoAdaptiveQueue(unittest.TestCase):
    def setUp(self):
        self.queue = AutoAdaptiveQueue(3, 2, 2, 2)
    
    def testInit(self):
        self.assertEqual(self.queue.max_trials, 3)
        self.assertEqual(self.queue.size_increment, 2)
        self.assertEqual(self.queue.trials, 0)
        self.assertEqual(self.queue.rejected.size(), 0)

    def test_enqueue(self):       
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertTrue(self.queue.isFull())
        self.assertEqual(self.queue.trials,0)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.trials,1)
        self.assertEqual(self.queue.rejected.list[0], 3)
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        self.assertEqual(self.queue.trials,0)
        self.assertEqual(self.queue.max_size,4)
        self.assertEqual(self.queue.size(), 4)

    #  Test de la nouvelle fonction
    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.rejected.size(), 1)
        self.assertTrue(self.queue.isFull())
        item = self.queue.dequeue()
        self.assertEqual(item, 1)
        self.assertTrue(self.queue.isFull())
        self.assertEqual(self.queue.list[0], 2)
        self.assertEqual(self.queue.size(), 2)
        self.assertEqual(self.queue.list[1], 3)
        self.assertEqual(self.queue.rejected.size(), 0)


if __name__ == '__main__':
    unittest.main()
