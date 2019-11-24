import unittest
from app import *

class TestFilePrinter(unittest.TestCase):
    def setUp(self):
        self.printer = FilePrinter("file.txt", "name")
        self.queue = Queue(4)
        self.stack = Stack(4)
        self.linkedlist = LinkedList()

    def testInit(self):
        self.assertEqual(self.printer.file_path, "file.txt")
        self.assertEqual(self.printer.name, "name")

    def test_should_print_in_file_Queue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(11)
        self.queue.enqueue(111)
        self.queue.enqueue(1111)
        open(self.printer.file_path, 'w').close()
        self.queue.accept(self.printer)
        with open(self.printer.file_path, 'r') as testFile:
            self.assertEqual(testFile.read(), self.printer.name + "\n|1|11|111|1111|\n")
        self.assertTrue(True)

    def test_should_print_in_file_Stack(self):
        self.stack.push(1)
        self.stack.push(11)
        self.stack.push(111)
        self.stack.push(1111)
        self.printer = FilePrinter("file.txt", "name")
        open(self.printer.file_path, 'w').close()
        self.stack.accept(self.printer)
        with open(self.printer.file_path, 'r') as testFile:
            self.assertEqual(testFile.read(), self.printer.name + "\n-------\n   1111   \n-------\n   111   \n-------\n   11   \n-------\n   1   \n-------\n")
        self.assertTrue(True)

    def test_should_print_in_file_LinkedList(self):
        self.linkedlist.append(1)
        self.linkedlist.append(11)
        self.linkedlist.append(111)
        self.linkedlist.append(1111)
        self.printer = FilePrinter("file.txt", "name")
        open(self.printer.file_path, 'w').close()
        self.linkedlist.accept(self.printer)
        with open(self.printer.file_path, 'r') as testFile:
            self.assertEqual(testFile.read(), self.printer.name + "\n(1,11,111,1111)\n")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
