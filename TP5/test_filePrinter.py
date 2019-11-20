import unittest
from app import *

class TestFilePrinter(unittest.TestCase):

    def testInit(self):
        printer = FilePrinter("file.txt", "name")
        self.assertEqual(printer.file_path, "file.txt")
        self.assertEqual(printer.name, "name")

    def should_print_in_file_queue(self):
        queue = Queue(4)
        queue.enqueue(1)
        queue.enqueue(11)
        queue.enqueue(111)
        queue.enqueue(1111)
        printer = FilePrinter("file.txt", "name")
        queue.accept(printer)
        with open(printer.file_path, 'r') as testFile:
            self.assertEqual(testFile.read(), printer.name + "\n|1|11|111|1111\n")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
