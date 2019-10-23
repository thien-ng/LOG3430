from Queue import *
import unittest

class testNode(unittest.TestCase):

    def test_value_constructeur_init(self):
        node = Node("testValue")

        self.assertEqual(node.value, "testValue")

    def test_value_autre_str(self):
        node = Node(1)

        self.assertEqual(node.__str__(), "1")

    def test_next_constructeur_init(self):
        node = Node("testValue")

        self.assertIsNone(node.next)

class TestQueue(unittest.TestCase):

    def test_first_rapporteur_checkFirst(self):
        queue = Queue()
        queue.empty = False

        self.assertIsNone(queue.check_first())

    def test_first_constructeur__init(self):
        queue = Queue()

        self.assertIsNone(queue.first)
    
    def test_first_transformateur_enqueue(self):
        queue = Queue()
        queue.enqeue("item")

        self.assertEqual(queue.first.value, "item")

    # def test_first_transformateur_dequeue(self):

    def test_n_rapporteur_size(self):
        queue = Queue()

        self.assertEqual(queue.size(), 0)    

    def test_n_constructeur_init(self):
        queue = Queue()

        self.assertEqual(queue.n, 0)

    def test_n_transformateur_enqueue(self):
        queue = Queue()
        queue.enqeue("item")
        queue.enqeue("item2")

        self.assertEqual(queue.n, 2)

    def test_n_transformateur_dequeue(self):
        queue = Queue()
        queue.enqeue("item")
        queue.enqeue("item2")
        queue.dequeue()

        self.assertEqual(queue.n, 1)

    def test_n_autre_check_last(self):
        queue = Queue()
        queue.enqeue("item")
        self.assertRaises(ValueError, queue.check_last)
    
    def test_n_autre_hasOne(self):
        queue = Queue()
        queue.enqeue("item")
        self.assertTrue(queue.hasOne())



if __name__ == '__main__':
    unittest.main()
  