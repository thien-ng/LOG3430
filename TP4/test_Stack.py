from Stack import *
import unittest

class TestStack(unittest.TestCase):

    def test_sequence_1_vide_vide(self):
        stack = Stack(100, 100, 10)
        self.assertRaises(ValueError, stack.pop)

    def test_sequence_2_vide_partiellement_plein(self):
        stack = Stack(100, 100, 10)
        stack.push("node")
        item = stack.pop()

        self.assertEqual(item, "node")
        self.assertIsNone(stack.first)
        self.assertEqual(stack.n, 0)

    def test_sequence_3_vide_partiellement_plein(self):
        stack = Stack(100, 100, 10)
        stack.push("node1")
        stack.push("node2")

        self.assertEqual(stack.first.value, "node2")
        self.assertEqual(stack.n, 2)

    def test_sequence_4_vide_partiellement_plein(self):
        stack = Stack(2, 5, 10)
        stack.push("node1")
        stack.push("node2")
        
        item = stack.pop()
        self.assertEqual(item, "node2")
        self.assertEqual(stack.first.value, "node1")
        self.assertEqual(stack.n, 1)
        
    def test_sequence_5_vide_plein(self):
        stack = Stack(2, 5, 10)
        stack.push("node1")
        stack.push("node2")

        self.assertTrue(stack.isFull())
    
if __name__ == '__main__':
    unittest.main()