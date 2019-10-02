from generators import *
import unittest
import models

class TestEulerianCycleEC(unittest.TestCase):
    
    def test_when_generate_eulerian_cycle_with_negative_vertex_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, -5, 2)

if __name__ == '__main__':
    unittest.main()
    