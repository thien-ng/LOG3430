from Queue import *
import unittest

class testNode(unittest.TestCase):

    def test_value_constructor_init(self):
        node = Node("testValue")

        self.assertEqual(node.value, "testValue")

    def test_value_autre_str(self):
        node = Node(1)

        self.assertEqual(node.__str__(), "1")

    def test_next_constructor_init(self):
        node = Node("testValue")

        self.assertIsNone(node.next);

class TestQueue(unittest.TestCase):

    def test_first_rapporteur_checkFirst(self):
        queue = Queue()

        self.assertEqual()

        


if __name__ == '__main__':
    unittest.main()
  