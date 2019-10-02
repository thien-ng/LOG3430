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
    
    def test_when_generate_eulerian_cycle_with_negative_vertex_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, -5, 2)

if __name__ == '__main__':
    unittest.main()
    