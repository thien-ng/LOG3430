import unittest
from app import *

def printqueue(liste):
    noeud = liste.first
    print(noeud)

    while noeud.next:
        noeud = noeud.next
        print(noeud)

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

        print("merged")
        printqueue(merged)
        # print("queue1")
        # printqueue(queue1)
        # print("queue2")
        # printqueue(queue2)

        # for i in range(len(queues)):
        #     for i in range(queues[i].max_size):
        #         print(merged.dequeue())
        #         print(queues[i].dequeue())
        
        
    

if __name__ == '__main__':
    unittest.main()