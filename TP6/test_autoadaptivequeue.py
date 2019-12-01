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

    #  Test de la nouvelle fonction dequeue()
    def test_dequeue(self):
        queue = AutoAdaptiveQueue(max_trials=2, size_increment=1, max_size_rejected_queue=1, max_size=2)
        queue.enqueue("value1")
        queue.enqueue("value2") 
        queue.enqueue("valueRejected1") #raises error, trials++, store in rejected
        self.assertEqual(queue.rejected.size(), 1)
        
        item = queue.dequeue() #rejected queue dequeues one item and enqueues it in the queue
        self.assertEqual(item, "value1")
        self.assertEqual(queue.size(), 2)
        self.assertEqual(queue.rejected.size(), 0)

        queue.enqueue("valueRejected2") #raises error, trials++, store in rejected, size is incremented
        #rejected queue emptied in the queue
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.rejected.size(), 0)

        item2 = queue.dequeue()
        self.assertEqual(item2, "value2")
        self.assertEqual(queue.size(), 2)

        item3 = queue.dequeue()
        self.assertEqual(item3, "valueRejected1")
        self.assertEqual(queue.size(), 1)

        item3 = queue.dequeue()
        self.assertEqual(item3, "valueRejected2")
        self.assertEqual(queue.size(), 0)


if __name__ == '__main__':
    unittest.main()
