from generators import *
import unittest
import models


# bipartite (V1, V2, E)
# Catégories: 
# -V1 pour le nombre de sommets dans le premier sous-ensemble
# -V2 pour le nombre de sommets dans le deuxième sous-ensemble
# -E pour le nombre d’arêtes

# Choix:                
# V1(1) = {V1 < 0}	        [erreur]
# V1(2) = {V1 = 0}	        [properties: nbV10]
# V1(3) = {V1 > 0}	        [properties: nbVertices1Ok]

# V2(1) = {V2 < 0}	        [erreur]
# V2(2) = {V2 = 0}	        [if nbV10; properties: nbV20 ]
# V2(3) = {V2 > 0}	        [properties: nbVertices2Ok]

# E1 = {E < 0}		        [erreur]
# E2 = {E = 0}		        [if nbV10 && nbV20]
# E3 = {0 < E <= V1*V2}		[if nbVertices1Ok && nbVertices2Ok]
# E4 = {E > V1*V2} 	        [erreur]
class TestBipartite(unittest.TestCase):
    def setUp(self):
        self.bipartiteGraph = None
        self.exceptionRaised = False


    def test_when_generate_bipartite_graph_with_V13_V23_E4(self):
        self.assertRaises(ValueError, bipartite, 1, 2, 6)

class TestEulerianCycleEC(unittest.TestCase):
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
    
    def test_when_generate_eulerian_cycle_with_negative_vertex_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, -5, -1)
    
    def test_when_generate_eulerian_cycle_with_vertex_equal_to_0_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, 0, 0)
    
    def test_when_generate_eulerian_cycle_with_positive_vertex_should_return_graph(self):
        
        isExceptionRaised = False
        
        try:
            eulerianCycle(2,2)
        except:
            isExceptionRaised = True
        
        self.assertFalse(isExceptionRaised)

if __name__ == '__main__':
    unittest.main()
    