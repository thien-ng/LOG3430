from generators import *
import unittest
import models

# Simple (V, E)
# Catégories:
# -V: pour le nombres de sommets du graphe
# -E: le nombre d’arêtes

# Choix:
# V(1) : V > 0			    [properties: nbVerticesOk]
# V(2) : V = 0			    [properties: nbVertices0]
# V(3) : V < 0			    [error]

# E(1) : 0 < E < V*(V-1)/2	[si nbVerticesOk]
# E(2) : E = 0			    [si nbVertices0]
# E(3) : E < 0			    [error]
# E(4):  E > V*(V-1)/2		[erreur]

class TestGraphSimple(unittest.TestCase):
    def setUp(self):
        self.simpleGraph = None
        self.exceptionRaised = False

    def test_when_generate_simple_graph_with_positive_nb_of_edges_and_positive_nb_of_vertices(self):
        try:
            self.simpleGraph = simple(3, 3)
        except:
            self.exceptionRaised = True
        self.assertFalse(self.exceptionRaised)

class TestEulerianCycleEC(unittest.TestCase):
    
    def test_when_generate_eulerian_cycle_with_negative_vertex_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, -5, 2)

if __name__ == '__main__':
    unittest.main()
    