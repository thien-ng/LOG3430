import unittest
from app import *

def containsValue(list1, value):
    n = list1.first
    while n.value != value:
        if n.next:
            n = n.next
        else:
            return False

    return True

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
        linked = LinkedList()

        for i in range(1,5):
            queue.enqueue(i)
            linked.append(i + 4)  

        merged = calc.union(queue, linked)

        self.assertEqual(merged.size(), queue.max_size + linked.size())

        for i in range(queue.max_size):
            self.assertTrue(containsValue(merged, queue.dequeue()))

        for i in range(linked.size()):
            self.assertTrue(containsValue(merged, linked.peek()))

    def test_union_linkedList_linkedList(self):
        calc = Calculator()
        linked1 = LinkedList()
        linked2 = LinkedList()

        for i in range(1,5):
            linked1.append(i)
            linked2.append(i + 4)

        lists = [linked1, linked2]
        merged = calc.union(linked1, linked2)

        self.assertEqual(merged.size(), linked1.size() + linked2.size())
        
        for i in range(len(lists)):
            for j in range(lists[i].size()):
                self.assertTrue(containsValue(merged, lists[i].peek()))


if __name__ == '__main__':
    unittest.main()