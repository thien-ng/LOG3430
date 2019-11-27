import unittest
from app import *

class TestAutoAdaptiveStack(unittest.TestCase):

    def testInit(self):
        stack = AutoAdaptiveStack(1, 1, 1)
        self.assertEqual(stack.max_trials, 1)
        self.assertEqual(stack.size_increment, 1)
        self.assertEqual(stack.trials, 0)

    def test_push_pop(self):
        stack = AutoAdaptiveStack(2, 1, 1)
        stack.push("value")
        stack.push("value") #raises error, trial++
        self.assertEqual(stack.trials, 1)
    
        stack.push("value")
        item = stack.pop()

        self.assertEqual(item, "value")
        self.assertEqual(stack.trials, 0)
        self.assertEqual(stack.max_size, 2)


if __name__ == '__main__':
    unittest.main()
