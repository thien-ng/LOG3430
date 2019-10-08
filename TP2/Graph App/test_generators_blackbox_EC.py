from generators import *
import unittest
import models

class TestSimple(unittest.TestCase):
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
    # E(4):  E > V*(V-1)/2		[error]

    def setUp(self):
        self.exceptionRaised = False

    def test_when_generate_simple_graph_with_E1_and_V1(self):
        try:
            simple(4, 3)
        except:
            self.exceptionRaised = True
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_simple_graph_with_E2_and_V2(self):
        try:
            simple(0, 0)
        except:
            self.exceptionRaised = True
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_simple_graph_with_E3_and_V3(self):
        self.assertRaises(ValueError, simple, -1, -1)

    def test_when_generate_simple_graph_with_E4_and_V1(self):
        self.assertRaises(ValueError, simple, 3, 4)

class TestSimpleWithProbability(unittest.TestCase):
    # simple with probability (V, p)
    # Catégories:
    # -V: pour le nombres de sommets du graphe
    # -p: la probabilité d’avoir une arête entre deux sommets

    # Choix:
    # V(1) : V < 0		[erreur]
    # V(2) : V = 0		[properties: nbVertices0]
    # V(3) : V > 0		[properties: nbVerticesOk]

    # p(1) : p < 0		[erreur]
    # p(2) : p = 0		[si nbVertices0]
    # p(3) : 0 < p <= 1	[si nbVerticesOk]
    # p(4) : p > 1		[si nbVerticesOk]

    def setUp(self):
        self.exceptionRaised = False

    def test_when_generate_simple_graph_with_probability_with_p1_and_V1(self):
        self.assertRaises(ValueError, simple_with_probability, -1, -0.5)

    def test_when_generate_simple_graph_with_probability_with_p2_and_V2(self):
        try:
            simple_with_probability(0, 0)
        except:
            self.exceptionRaised = True
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_simple_graph_with_probability_with_p3_and_V3(self):
        try:
            simple_with_probability(3, 0.5)
        except:
            self.exceptionRaised = True
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_simple_graph_with_probability_with_p4_and_V3(self):
        self.assertRaises(ValueError, simple_with_probability, 3, 3)

class TestBipartite(unittest.TestCase):
    # bipartite (V1, V2, E)
    # Catégories: 
    # -V1 pour le nombre de sommets dans le premier sous-ensemble
    # -V2 pour le nombre de sommets dans le deuxième sous-ensemble
    # -E pour le nombre d’arêtes

    # Choix:                
    # V1(1) : {V1 < 0}	        [erreur]
    # V1(2) : {V1 = 0}	        [properties: nbV10]
    # V1(3) : {V1 > 0}	        [properties: nbVertices1Ok]

    # V2(1) : {V2 < 0}	        [erreur]
    # V2(2) : {V2 = 0}	        [if nbV10; properties: nbV20 ]
    # V2(3) : {V2 > 0}	        [properties: nbVertices2Ok]

    # E1 : {E < 0}		        [erreur]
    # E2 : {E = 0}		        [if nbV10 && nbV20]
    # E3 : {0 < E <= V1*V2}		[if nbVertices1Ok && nbVertices2Ok]
    # E4 : {E > V1*V2} 	        [erreur]

    def setUp(self):
        self.exceptionRaised = False


    def test_when_generate_bipartite_graph_with_V13_V23_E4(self):
        self.assertRaises(ValueError, bipartite, 1, 2, 6)

    def test_when_generate_bipartite_graph_with_V12_V22_E2(self):
        try:
            bipartite(0, 0, 0)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_bipartite_graph_with_V11_V21_E1(self):
        self.assertRaises(ValueError, bipartite, -1, -2, -6)

    def test_when_generate_bipartite_graph_with_V13_V23_E3(self):
        try:
            bipartite(3, 4, 9)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

class TestBipartiteWithProbability(unittest.TestCase):
    # bipartite_with_probability (V1, V2, p)
    # Catégories: 
    # -V1 pour le nombre de sommets dans le premier sous-ensemble
    # -V2 pour le nombre de sommets dans le deuxième sous-ensemble
    # -p pour la probabilité d’avoir un arête entre deux sommets de deux sous-ensembles différents

    # Choix:                
    # V1(1) : {V1 < 0}	        [erreur]
    # V1(2) : {V1 = 0}	        [properties: nbV10]
    # V1(3) : {V1 > 0}	        [properties: nbVertices1Ok]

    # V2(1) : {V2 < 0}	        [erreur]
    # V2(2) : {V2 = 0}	        [if nbV10; properties: nbV20 ]
    # V2(3) : {V2 > 0}	        [properties: nbVertices2Ok]

    # p1 : {p < 0}       		[erreur]
    # p2 : {p = 0}		        [if nbV10 && nbV20]
    # p3 : {0 < p <= 1}		    [if nbVertices1Ok && nbVertices2Ok]
    # p4 : {p > 1}		        [erreur]

    def setUp(self):
        self.exceptionRaised = False

    def test_when_generate_bipartite_with_probability_graph_with_V11_V22_p3(self):
        self.assertRaises(ValueError, bipartite_with_probability, -2, 0, 0.6)

    def test_when_generate_bipartite_with_probability_graph_with_V12_V22_p2(self):
        try:
            bipartite_with_probability(0, 0, 0)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_bipartite_graph_with_V11_V21_p1(self):
        self.assertRaises(ValueError, bipartite_with_probability, -1, -2, -0.8)

    def test_when_generate_bipartite_graph_with_V13_V23_p4(self):
        self.assertRaises(ValueError, bipartite_with_probability, 5, 2, 8)

    #test boite blanche à rajouter pour compléter la couverture
    def test_when_generate_bipartite_graph_with_V13_V23_p3(self):
        try:
            bipartite_with_probability(5, 2, 0.8)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

class TestEulerianCycle(unittest.TestCase):
    # eulerianCycle(V, E)
    # Categories:
    # V: V Nombre de sommet dans le cycle
    # E: E Nombre d'arret dans le cycle

    # Choices:
    # V(1): {V < 0}	[Error]
    # V(2): {V = 0}	[Error]
    # V(3): {V > 0}	[properties: nbVerticesOk]

    # E(1): {E < 0}	[Error]
    # E(2): {E = 0}	[Error]
    # E(3): {E > 0}	[properties: nbEdgesOk]
    
    def test_when_generate_eulerian_cycle_with_negative_vertex_and_negative_edge_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, -5, -1)
    
    def test_when_generate_eulerian_cycle_with_0_vertex_and_0_edge_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, 0, 0)
    
    def test_when_generate_eulerian_cycle_with_positive_vertex_and_positive_edge_should_return_graph(self):
        
        isExceptionRaised = False
        
        try:
            eulerianCycle(2,2)
        except:
            isExceptionRaised = True
        
        self.assertFalse(isExceptionRaised)
    
    # Test added for uncovered line when running coverage run of EC
    def test_when_generate_eulerian_cycle_with_positive_vertex_and_negative_edge_should_raise_ValueError(self):
        self.assertRaises(ValueError, eulerianCycle, -1, 2)

class TestRegular(unittest.TestCase):
    # regular(V, K)
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

    def test_when_generate_regular_with_negative_odd_vertex_and_negative_odd_degree_should_raise_ValueError(self):
        self.assertRaises(ValueError, regular, -1, -1)

    def test_when_generate_regular_with_0_vertex_and_0_degree_should_raise_ValueError(self):
    
        isExceptionRaised = False
        
        try:
            regular(0,0)
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

    def test_when_generate_regular_with_positive_odd_vertex_and_positive_odd_degree_should_raise_ValueError(self):
        self.assertRaises(ValueError, regular, 1, 1)

if __name__ == '__main__':
    unittest.main()
    