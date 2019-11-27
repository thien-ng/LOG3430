import unittest
from app import *

def containsValue(list1, value):
    return value in list1.list

class TestCalculator(unittest.TestCase):

    
    def test_union_queue_queue(self):
        calc = Calculator()
        queue1 = Queue(4)
        queue2 = Queue(4)

        for i in range(1,5):
            queue1.enqueue(i)
            queue2.enqueue(i + 4)

        queues = [queue1, queue2]
        merged = calc.union(queue1, queue2)

        self.assertEqual(merged.max_size, queue1.max_size + queue2.max_size)

        for i in range(len(queues)):
            for j in range(queues[i].max_size):
                self.assertEqual(merged.dequeue(), queues[i].dequeue())
        
        
    def test_union_queue_linkedList(self):
        calc = Calculator()
        queue = Queue(4)
        linked = List()

        for i in range(1,5):
            queue.enqueue(i)
            linked.append(i + 4)  

        merged = calc.union(queue, linked)

        self.assertEqual(merged.size(), queue.max_size + linked.size())

        for i in range(queue.max_size):
            self.assertTrue(containsValue(merged, queue.dequeue()))

        for i in range(linked.size()):
            self.assertTrue(containsValue(merged, linked.peek()))

    def test_union_stack_stack(self):
        calc = Calculator()
        stack1 = Stack(4)
        stack2 = Stack(4)

        for i in range(1,5):
            stack1.push(i)
            stack2.push(i + 4)

        lists = [stack1, stack2]
        merged = calc.union(stack1, stack2)

        self.assertEqual(merged.size(), stack1.size() + stack2.size())
        
        for i in range(len(lists)):
            for j in range(lists[i].size()):
                self.assertTrue(containsValue(merged, lists[i].peek()))


if __name__ == '__main__':
    unittest.main()