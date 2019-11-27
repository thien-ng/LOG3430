import unittest, sys, io
from app import *

class TestScreenPrinter(unittest.TestCase):
    
    def setUp(self):
        self.screenPrinter = ScreenPrinter("screenPrinter")
        self.list = List()
        self.stack = Stack(2)
        self.queue = Queue(2)
    
    def testInit(self):
        self.assertEqual(self.screenPrinter.name, "screenPrinter")

    def test_visitQueue(self):
        self.queue.enqueue("value1")
        self.queue.enqueue("value2")

        sys.stdout = io.StringIO() 
        self.queue.accept(ScreenPrinter(""))
        self.assertEqual(sys.stdout.getvalue(), "\n\n|value1|value2|\n\n")
        sys.stdout = sys.__stdout__  

    def test_visitStack(self):
        self.stack.push("value1")
        self.stack.push("value2")

        sys.stdout = io.StringIO() 
        self.stack.accept(ScreenPrinter(""))
        self.assertEqual(sys.stdout.getvalue(), "\n\n-------\n   value2   \n-------\n   value1   \n-------\n\n")
        sys.stdout = sys.__stdout__

    def test_visitlist(self):
        self.list.append("value1")
        self.list.append("value2")

        sys.stdout = io.StringIO() 
        self.list.accept(ScreenPrinter(""))
        self.assertEqual(sys.stdout.getvalue(), "\n\n(value1,value2)\n\n")
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()