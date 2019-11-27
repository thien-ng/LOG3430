import unittest
from app import *

class TestAutoAdaptiveQueue(unittest.TestCase):
    
    def testInit(self):
        queue = AutoAdaptiveQueue(1,2,2)
        self.assertEqual(queue.max_trials, 1)
        self.assertEqual(queue.size_increment, 2)
        self.assertEqual(queue.trials, 0)

    def test_enqueue(self):
        queue = AutoAdaptiveQueue(2,2,2)
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertTrue(queue.isFull())
        self.assertEqual(queue.trials,0)
        queue.enqueue(3)
        self.assertEqual(queue.trials,1)
        queue.enqueue(4)
        self.assertEqual(queue.trials,0)
        self.assertEqual(queue.max_size,4)


if __name__ == '__main__':
    unittest.main()
