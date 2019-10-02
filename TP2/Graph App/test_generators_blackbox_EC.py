from generators import *
import unittest
import models

class TestEulerianCycleEC(unittest.TestCase):

    # Categories:
    # V: V the number of vertices in the cycle
    # E: E the number of edges in the cycle

    # Choices:
    # V(1): {V < 0}	[Error]
    # V(2): {V = 0}	[Error]
    # V(3): {V > 0}	[properties: nbVerticesOk]

    # E(1): {E < 0}	[Error]
    # E(2): {E = 0}	[Error]
    # E(3): {E > 0}	[properties: nbEdgesOk]
    
    def test_when_generate_eulerian_cycle_with_negative_vertex_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, -5, 2)
        

if __name__ == '__main__':
    unittest.main()
    