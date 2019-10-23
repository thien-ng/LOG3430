from Queue import *
import unittest

class testNode(unittest.TestCase):

    def test_value_constructeur_init(self):
        node = Node("testValue")

        self.assertEqual(node.value, "testValue")

    def test_value_autre_str(self):
        node = Node(1)

        self.assertEqual(node.__str__(), "1")

    def test_next_constructor_init(self):
        node = Node("testValue")

        self.assertIsNone(node.next)

class TestQueue(unittest.TestCase):

    def test_first_rapporteur_checkFirst(self):
        queue = Queue()

        self.assertIsNone(queue.check_first)

    def test_first_constructeur__init(self):
        queue = Queue()

        self.assertIsNone(queue.first)
    
    def test_first_transformateur_enqueue(self):
        queue = Queue()
        queue.enqeue("item")

        self.assertEqual(queue.first.value, "item")

        


if __name__ == '__main__':
    unittest.main()
  