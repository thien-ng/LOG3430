from generators import *
import unittest
import models

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

    def test_when_generate_bipartite_graph_with_V11_V21_E1(self):
        self.assertRaises(ValueError, bipartite, -4, -2, -6)

    def test_when_generate_bipartite_graph_with_V11_V21_E2(self):
        self.assertRaises(ValueError, bipartite, -4, -2, 0)

    def test_when_generate_bipartite_graph_with_V11_V21_E3(self):
        self.assertRaises(ValueError, bipartite, -4, -2, 6)

    def test_when_generate_bipartite_graph_with_V11_V21_E4(self):
        self.assertRaises(ValueError, bipartite, -4, -2, 10) 

    def test_when_generate_bipartite_graph_with_V11_V22_E1(self):
        self.assertRaises(ValueError, bipartite, -4, 0, -6)

    def test_when_generate_bipartite_graph_with_V11_V22_E2(self):
        self.assertRaises(ValueError, bipartite, -4, 0, 0)

    def test_when_generate_bipartite_graph_with_V11_V22_E3(self):
        #à vérifier
        self.assertRaises(ValueError, bipartite, -4, 0, 0)

    def test_when_generate_bipartite_graph_with_V11_V22_E4(self):
        self.assertRaises(ValueError, bipartite, -4, 0, 10) 
    
    def test_when_generate_bipartite_graph_with_V11_V23_E1(self):
        self.assertRaises(ValueError, bipartite, -4, 2, -6)

    def test_when_generate_bipartite_graph_with_V11_V23_E2(self):
        self.assertRaises(ValueError, bipartite, -4, 2, 0)

    def test_when_generate_bipartite_graph_with_V11_V23_E3(self):
        #cas impossible??
        self.assertRaises(ValueError, bipartite, -4, 2, 6)

    def test_when_generate_bipartite_graph_with_V11_V23_E4(self):
        self.assertRaises(ValueError, bipartite, -4, 0, 10) 

    def test_when_generate_bipartite_graph_with_V12_V21_E1(self):
        self.assertRaises(ValueError, bipartite, 0, -2, -6)

    def test_when_generate_bipartite_graph_with_V12_V21_E2(self):
        self.assertRaises(ValueError, bipartite, 0, -2, 0)

    def test_when_generate_bipartite_graph_with_V12_V21_E3(self):
        #à vérifier
        self.assertRaises(ValueError, bipartite, 0, -2, 6)

    def test_when_generate_bipartite_graph_with_V12_V21_E4(self):
        self.assertRaises(ValueError, bipartite, 0, -2, 10) 
    
    def test_when_generate_bipartite_graph_with_V12_V22_E1(self):
        self.assertRaises(ValueError, bipartite, 0, 0, -6)

    def test_when_generate_bipartite_graph_with_V12_V22_E2(self):
        try:
            bipartite(0, 0, 0)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_bipartite_graph_with_V12_V22_E3(self):
        #à vérifier
        self.assertRaises(ValueError, bipartite, 0, 0, 6)

    def test_when_generate_bipartite_graph_with_V12_V22_E4(self):
        self.assertRaises(ValueError, bipartite, 0, 0, 10) 
    
    def test_when_generate_bipartite_graph_with_V12_V23_E1(self):
        self.assertRaises(ValueError, bipartite, 0, 4, -6)

    def test_when_generate_bipartite_graph_with_V12_V23_E2(self):
        try:
            bipartite(0, 4, 0)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_bipartite_graph_with_V12_V23_E3(self):
        #à vérifier
        self.assertRaises(ValueError, bipartite, 0, 4, 6)

    def test_when_generate_bipartite_graph_with_V12_V23_E4(self):
        self.assertRaises(ValueError, bipartite, 0, 4, 10) 
    
    def test_when_generate_bipartite_graph_with_V13_V21_E1(self):
        self.assertRaises(ValueError, bipartite, 6, -2, -6)

    def test_when_generate_bipartite_graph_with_V13_V21_E2(self):
        self.assertRaises(ValueError, bipartite, 6, -2, 0)

    def test_when_generate_bipartite_graph_with_V13_V21_E3(self):
        #cas impossible?
        self.assertRaises(ValueError, bipartite, 6, -2, 6)

    def test_when_generate_bipartite_graph_with_V13_V21_E4(self):
        self.assertRaises(ValueError, bipartite, 6, -2, 10)
    
    def test_when_generate_bipartite_graph_with_V13_V22_E1(self):
        self.assertRaises(ValueError, bipartite, 6, 0, -6)

    def test_when_generate_bipartite_graph_with_V13_V22_E2(self):
        try:
            bipartite(6, 0, 0)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_bipartite_graph_with_V13_V22_E3(self):
        #à vérifier
        self.assertRaises(ValueError, bipartite, 6, 0, 6)

    def test_when_generate_bipartite_graph_with_V13_V22_E4(self):
        self.assertRaises(ValueError, bipartite, 6, 0, 10)
    
    def test_when_generate_bipartite_graph_with_V13_V23_E1(self):
        self.assertRaises(ValueError, bipartite, 6, 2, -6)

    def test_when_generate_bipartite_graph_with_V13_V23_E2(self):
        try:
            bipartite(6, 2, 0)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_bipartite_graph_with_V13_V23_E3(self):
        try:
            bipartite(6, 2, 6)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_bipartite_graph_with_V13_V23_E4(self):
        self.assertRaises(ValueError, bipartite, 6, 2, 14)

class TestBipartiteWithProbability(unittest.TestCase):
    # Catégories: 
    # -V1 pour le nombre de sommets dans le premier sous-ensemble
    # -V2 pour le nombre de sommets dans le deuxième sous-ensemble
    # -p pour la probabilité d’avoir un arête entre deux sommets de deux sous-ensembles différents

    # Choix:                
    # V1(1) : {V1 < 0}	        [erreur]
    # V1(2) : {V1 = 0}	        [properties: nbV10]
    # V1(3) : {V1 > 0}	        [properties: nbVertices1Ok]

    # V2(1) : {V2 < 0}	        [erreur]
    # V2(2) : {V2 = 0}	        [properties: nbV20 ]
    # V2(3) : {V2 > 0}	        [properties: nbVertices2Ok]

    # p1 : {p < 0}       		[erreur]
    # p2 : {p = 0}		        [if nbV10 || nbV20]
    # p3 : {0 < p <= 1}		    [if nbVertices1Ok && nbVertices2Ok]
    # p4 : {p > 1}		        [erreur]

    def setUp(self):
        self.exceptionRaised = False

    def test_when_generate_bipartite_with_probability_graph_with_V11_V21_p1(self):
         self.assertRaises(ValueError, bipartite_with_probability, -6, -2, -0.8)

    def test_when_generate_bipartite_with_probability_graph_with_V11_V21_p2(self):
         self.assertRaises(ValueError, bipartite_with_probability, -6, -2, 0)

    def test_when_generate_bipartite_with_probability_graph_with_V11_V21_p3(self):
         self.assertRaises(ValueError, bipartite_with_probability, -6, -2, 0.6)

    def test_when_generate_bipartite_with_probability_graph_with_V11_V21_p4(self):
         self.assertRaises(ValueError, bipartite_with_probability, -6, -2, 1.8)

    def test_when_generate_bipartite_with_probability_graph_with_V11_V22_p1(self):
         self.assertRaises(ValueError, bipartite_with_probability, -6, 0, -0.8)

    def test_when_generate_bipartite_with_probability_graph_with_V11_V22_p2(self):
         self.assertRaises(ValueError, bipartite_with_probability, -6, 0, 0)

    def test_when_generate_bipartite_with_probability_graph_with_V11_V22_p3(self):
         self.assertRaises(ValueError, bipartite_with_probability, -6, 0, 0.6)

    def test_when_generate_bipartite_with_probability_graph_with_V11_V22_p4(self):
         self.assertRaises(ValueError, bipartite_with_probability, -6, 0, 1.8) 

    def test_when_generate_bipartite_with_probability_graph_with_V11_V23_p1(self):
         self.assertRaises(ValueError, bipartite_with_probability, -6, 4, -0.8)

    def test_when_generate_bipartite_with_probability_graph_with_V11_V23_p2(self):
         self.assertRaises(ValueError, bipartite_with_probability, -6, 4, 0)

    def test_when_generate_bipartite_with_probability_graph_with_V11_V23_p3(self):
         self.assertRaises(ValueError, bipartite_with_probability, -6, 4, 0.6)

    def test_when_generate_bipartite_with_probability_graph_with_V11_V23_p4(self):
         self.assertRaises(ValueError, bipartite_with_probability, -6, 4, 1.8)   

    def test_when_generate_bipartite_with_probability_graph_with_V12_V21_p1(self):
         self.assertRaises(ValueError, bipartite_with_probability, 0, -2, -0.8)

    def test_when_generate_bipartite_with_probability_graph_with_V12_V21_p2(self):
         self.assertRaises(ValueError, bipartite_with_probability, 0, -2, 0)

    def test_when_generate_bipartite_with_probability_graph_with_V12_V21_p3(self):
         self.assertRaises(ValueError, bipartite_with_probability, 0, -2, 0.6)

    def test_when_generate_bipartite_with_probability_graph_with_V12_V21_p4(self):
         self.assertRaises(ValueError, bipartite_with_probability, 0, -2, 1.8)

    def test_when_generate_bipartite_with_probability_graph_with_V12_V22_p1(self):
         self.assertRaises(ValueError, bipartite_with_probability, 0, 0, -0.8)

    def test_when_generate_bipartite_with_probability_graph_with_V12_V22_p2(self):
        try:
            bipartite_with_probability(0, 0, 0)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_bipartite_with_probability_graph_with_V12_V22_p3(self):
        try:
            bipartite_with_probability(0, 0, 0.6)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)
    def test_when_generate_bipartite_with_probability_graph_with_V12_V22_p4(self):
         self.assertRaises(ValueError, bipartite_with_probability, 0, 0, 1.8) 

    def test_when_generate_bipartite_with_probability_graph_with_V12_V23_p1(self):
         self.assertRaises(ValueError, bipartite_with_probability, 0, 4, -0.8)

    def test_when_generate_bipartite_with_probability_graph_with_V12_V23_p2(self):
        try:
            bipartite_with_probability(0, 4, 0)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)
    def test_when_generate_bipartite_with_probability_graph_with_V12_V23_p3(self):
        try:
            bipartite_with_probability(0, 4, 0.6)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_bipartite_with_probability_graph_with_V12_V23_p4(self):
         self.assertRaises(ValueError, bipartite_with_probability, 0, 4, 1.8)   

    def test_when_generate_bipartite_with_probability_graph_with_V13_V21_p1(self):
         self.assertRaises(ValueError, bipartite_with_probability, 6, -2, -0.8)

    def test_when_generate_bipartite_with_probability_graph_with_V13_V21_p2(self):
        try:
            bipartite_with_probability(6, -2, 0)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_bipartite_with_probability_graph_with_V13_V21_p3(self):
        try:
            bipartite_with_probability(6, -2, 0.6)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_bipartite_with_probability_graph_with_V13_V21_p4(self):
         self.assertRaises(ValueError, bipartite_with_probability, 6, -2, 1.8)

    def test_when_generate_bipartite_with_probability_graph_with_V13_V22_p1(self):
         self.assertRaises(ValueError, bipartite_with_probability, 6, 0, -0.8)

    def test_when_generate_bipartite_with_probability_graph_with_V13_V22_p2(self):
        try:
            bipartite_with_probability(6, 0, 0)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_bipartite_with_probability_graph_with_V13_V22_p3(self):
        try:
            bipartite_with_probability(6, 0, 0.6)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_bipartite_with_probability_graph_with_V13_V22_p4(self):
         self.assertRaises(ValueError, bipartite_with_probability, 6, 0, 1.8) 

    def test_when_generate_bipartite_with_probability_graph_with_V13_V23_p1(self):
         self.assertRaises(ValueError, bipartite_with_probability, 6, 4, -0.8)

    def test_when_generate_bipartite_with_probability_graph_with_V13_V23_p2(self):
        try:
            bipartite_with_probability(6, 4, 0)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_bipartite_with_probability_graph_with_V13_V23_p3(self):
        try:
            bipartite_with_probability(6, 4, 0.6)
        except:
            self.exceptionRaised = True
        
        self.assertFalse(self.exceptionRaised)

    def test_when_generate_bipartite_with_probability_graph_with_V13_V23_p4(self):
         self.assertRaises(ValueError, bipartite_with_probability, 6, 4, 1.8)  

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
    