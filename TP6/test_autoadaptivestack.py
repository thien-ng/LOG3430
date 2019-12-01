import unittest
from app import *

class TestAutoAdaptiveStack(unittest.TestCase):

    def testInit(self):
        stack = AutoAdaptiveStack(1, 1, 1, 1)
        self.assertEqual(stack.max_trials, 1)
        self.assertEqual(stack.size_increment, 1)
        self.assertEqual(stack.trials, 0)

    def test_push_pop(self):
        stack = AutoAdaptiveStack(2, 1, 1, 1)
        stack.push("value")
        stack.push("value") #raises error, trial++
        self.assertEqual(stack.trials, 1)
    
        stack.push("value")
        item = stack.pop()

        self.assertEqual(item, "value")
        self.assertEqual(stack.trials, 0)
        self.assertEqual(stack.max_size, 2)

    # Test de la nouvelle fonction pop()
    def test_push_pop_with_rejected_queue(self):
        stack = AutoAdaptiveStack(max_trials=2, size_increment=1, max_size_rejected_queue=1, max_size=2)
        stack.push("value1")
        stack.push("value2") 
        stack.push("valueRejected1") #raises error, trials++, store in rejected
        self.assertEqual(stack.rejected.size(), 1)
        
        item = stack.pop() #rejected queue dequeues one item and enqueues it in the queue
        self.assertEqual(item, "value2")
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.rejected.size(), 0)

        stack.push("valueRejected2") #raises error, trials++, store in rejected, size is incremented
        #rejected queue emptied in the queue
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.rejected.size(), 0)

        item2 = stack.pop()
        self.assertEqual(item2, "valueRejected2")
        self.assertEqual(stack.size(), 2)

        item3 = stack.pop()
        self.assertEqual(item3, "valueRejected1")
        self.assertEqual(stack.size(), 1)

        item3 = stack.pop()
        self.assertEqual(item3, "value1")
        self.assertEqual(stack.size(), 0)


if __name__ == '__main__':
    unittest.main()
