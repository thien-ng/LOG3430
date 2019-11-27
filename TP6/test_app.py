import unittest

# from test_node              import TestNode
# from test_linkedlist        import TestLinkedList
# from test_queue             import TestQueue
from test_stack             import TestStack
from test_calculator        import TestCalculator
from test_autoAdaptiveQueue import TestAutoAdaptiveQueue
from test_autoAdaptiveStack import TestAutoAdaptiveStack
from test_screenPrinter     import TestScreenPrinter
from test_filePrinter       import TestFilePrinter

suite = unittest.TestSuite()

# suite.addTest(unittest.makeSuite(TestNode))
# suite.addTest(unittest.makeSuite(TestLinkedList))
# suite.addTest(unittest.makeSuite(TestQueue))
suite.addTest(unittest.makeSuite(TestStack))
suite.addTest(unittest.makeSuite(TestCalculator))
suite.addTest(unittest.makeSuite(TestAutoAdaptiveQueue))
suite.addTest(unittest.makeSuite(TestAutoAdaptiveStack))
suite.addTest(unittest.makeSuite(TestScreenPrinter))
suite.addTest(unittest.makeSuite(TestFilePrinter))

unittest.TextTestRunner(verbosity=2).run(suite)