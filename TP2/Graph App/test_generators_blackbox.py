from generators import *
import unittest
import models

class TestGeneratorsBlackBox(unittest.TestCase):
    
    def setUp(self):
        print("test")

    def test(self):
        print(eulerianCycle(10,7))

if __name__ == '__main__':
    unittest.main()
    