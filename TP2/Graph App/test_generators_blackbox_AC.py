from generators import *
import unittest
import models

class TestEulerianCycle(unittest.TestCase):

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
    
    def test_when_generate_eulerian_cycle_with_negative_vertex_and_negative_edge_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, -5, -1)
    
    def test_when_generate_eulerian_cycle_with_negative_vertex_and_0_edge_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, -5, 0)

    def test_when_generate_eulerian_cycle_with_negative_vertex_and_positive_edge_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, -5, 5)
    
    def test_when_generate_eulerian_cycle_with_0_vertex_and_negative_edge_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, 0, -1)

    def test_when_generate_eulerian_cycle_with_0_vertex_and_0_edge_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, 0, 0)

    def test_when_generate_eulerian_cycle_with_0_vertex_and_positive_edge_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, 0, 5)

    def test_when_generate_eulerian_cycle_with_positive_vertex_and_negative_edge_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, 5, -1)

    def test_when_generate_eulerian_cycle_with_positive_vertex_and_0_edge_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, 5, 0)

    def test_when_generate_eulerian_cycle_with_positive_vertex_and_positive_edge_should_return_graph(self):
        
        isExceptionRaised = False
        
        try:
            eulerianCycle(5,5)
        except:
            isExceptionRaised = True
        
        self.assertFalse(isExceptionRaised)

class TestRegular(unittest.TestCase):

    # Categories:
    # V: V Nombre de sommet dans le graph
    # K: K degree du sommet

    # Choices
    # V(1): {V nombre pair negatif}
    # V(2): {V nombre impair negatif}
    # V(3): {V = 0}
    # V(4): {V nombre pair positive}
    # V(5): {V nombre impair positive}

    # K(1): {K nombre pair negatif}
    # K(2): {K nombre impair negatif}
    # K(3): {K = 0}
    # K(4): {K nombre pair positive}
    # K(5): {K nombre impair positive}

    def test_when_generate_regular_with_negative_even_vertex_and_negative_even_degree_should_raise_ValueError(self):
        self.assertRaises(ValueError, regular, -2, -2)

    def test_when_generate_regular_with_negative_even_vertex_and_negative_odd_degree_should_raise_ValueError(self):
        self.assertRaises(ValueError, regular, -2, -1)

    def test_when_generate_regular_with_negative_even_vertex_and_0_degree_should_raise_ValueError(self):
        self.assertRaises(ValueError, regular, -2, 0)

    def test_when_generate_regular_with_negative_even_vertex_and_positive_even_degree_should_raise_ValueError(self):
        self.assertRaises(ValueError, regular, -2, 2)

    def test_when_generate_regular_with_negative_even_vertex_and_positive_odd_degree_should_raise_ValueError(self):
        self.assertRaises(ValueError, regular, -2, 1)

    def test_when_generate_regular_with_negative_odd_vertex_and_negative_even_degree_should_raise_ValueError(self):
        self.assertRaises(ValueError, regular, -1, -2)

    def test_when_generate_regular_with_negative_odd_vertex_and_negative_odd_degree_should_raise_ValueError(self):
        self.assertRaises(ValueError, regular, -1, -1)

    def test_when_generate_regular_with_negative_odd_vertex_and_0_degree_should_raise_ValueError(self):
        self.assertRaises(ValueError, regular, -1, 0)

    def test_when_generate_regular_with_negative_odd_vertex_and_positive_even_degree_should_raise_ValueError(self):
        self.assertRaises(ValueError, regular, -1, 2)

    def test_when_generate_regular_with_negative_odd_vertex_and_positive_odd_degree_should_raise_ValueError(self):
        self.assertRaises(ValueError, regular, -1, 1)

    def test_when_generate_regular_with_0_vertex_and_negative_even_degree_should_raise_ValueError(self):
        isExceptionRaised = False
        try:
            regular(0,-2)
        except:
            isExceptionRaised = True
        self.assertFalse(isExceptionRaised)

    def test_when_generate_regular_with_0_vertex_and_negative_odd_degree_should_raise_ValueError(self):
        isExceptionRaised = False
        try:
            regular(0,-1)
        except:
            isExceptionRaised = True
        self.assertFalse(isExceptionRaised)

    def test_when_generate_regular_with_0_vertex_and_0_degree_should_raise_ValueError(self):
        isExceptionRaised = False
        try:
            regular(0,0)
        except:
            isExceptionRaised = True
        self.assertFalse(isExceptionRaised)

    def test_when_generate_regular_with_0_vertex_and_positive_even_degree_should_raise_ValueError(self):
        isExceptionRaised = False
        try:
            regular(0,2)
        except:
            isExceptionRaised = True
        self.assertFalse(isExceptionRaised)

    def test_when_generate_regular_with_0_vertex_and_positive_odd_degree_should_raise_ValueError(self):
        isExceptionRaised = False
        try:
            regular(0,1)
        except:
            isExceptionRaised = True
        self.assertFalse(isExceptionRaised)

    def test_when_generate_regular_with_positive_even_vertex_and_negative_even_degree_should_raise_ValueError(self):
        isExceptionRaised = False
        try:
            regular(2,-2)
        except:
            isExceptionRaised = True
        self.assertFalse(isExceptionRaised)

    def test_when_generate_regular_with_positive_even_vertex_and_negative_odd_degree_should_raise_ValueError(self):
        isExceptionRaised = False
        try:
            regular(2,-1)
        except:
            isExceptionRaised = True
        self.assertFalse(isExceptionRaised)

    def test_when_generate_regular_with_positive_even_vertex_and_0_degree_should_raise_ValueError(self):
        isExceptionRaised = False
        try:
            regular(2,0)
        except:
            isExceptionRaised = True
        self.assertFalse(isExceptionRaised)

    def test_when_generate_regular_with_positive_even_vertex_and_positive_even_degree_should_raise_ValueError(self):
        isExceptionRaised = False
        try:
            regular(2,2)
        except:
            isExceptionRaised = True
        self.assertFalse(isExceptionRaised)

    def test_when_generate_regular_with_positive_even_vertex_and_positive_odd_degree_should_raise_ValueError(self):
        isExceptionRaised = False
        try:
            regular(2,1)
        except:
            isExceptionRaised = True
        self.assertFalse(isExceptionRaised)

    def test_when_generate_regular_with_positive_odd_vertex_and_negative_even_degree_should_raise_ValueError(self):
        isExceptionRaised = False
        try:
            regular(1,-2)
        except:
            isExceptionRaised = True
        self.assertFalse(isExceptionRaised)

    def test_when_generate_regular_with_positive_odd_vertex_and_negative_odd_degree_should_raise_ValueError(self):
        self.assertRaises(ValueError, regular, 1, -1)

    def test_when_generate_regular_with_positive_odd_vertex_and_0_degree_should_raise_ValueError(self):
        isExceptionRaised = False
        try:
            regular(1,0)
        except:
            isExceptionRaised = True
        self.assertFalse(isExceptionRaised)

    def test_when_generate_regular_with_positive_odd_vertex_and_positive_even_degree_should_raise_ValueError(self):
        isExceptionRaised = False
        try:
            regular(1,2)
        except:
            isExceptionRaised = True
        self.assertFalse(isExceptionRaised)

    def test_when_generate_regular_with_positive_odd_vertex_and_positive_odd_degree_should_raise_ValueError(self):
        self.assertRaises(ValueError, regular, 1, 1)

if __name__ == '__main__':
    unittest.main()
    