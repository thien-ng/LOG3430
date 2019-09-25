from models import Graph
import random as rand
import utils

'''
This module provides static methods for creating
various graphs, including Erdos-Renyi random graphs, random bipartite
graphs, random k-regular graphs, and random rooted trees.
'''

def simple(V, E):
    '''
    Returns a random simple graph containing V vertices and E edges.
    @param V the number of vertices
    @param E the number of vertices
    @return a random simple graph on V vertices, containing a total of E edges
    @raises ValueError if no such simple graph exists
    '''
    if E > V*(V-1)/2:
        raise ValueError("Too many edges")
    if E < 0:
        raise ValueError("Too few edges")
    G = Graph(V)
    edges = []
    while G.E() < E:
        v = rand.randrange(V)
        w = rand.randrange(V)
        e = (v , w)
        if v != w and e not in edges:
            edges.append(e)
            G.add_edge(e)
    return G

def simple_with_probability(V, p):
    '''
    Returns a random simple graph on V vertices, with an 
    edge between any two vertices with probability p. This is sometimes
    referred to as the Erdos-Renyi random graph model.
    @param V the number of vertices
    @param p the probability of choosing an edge
    @return a random simple graph on V vertices, with an edge between
         any two vertices with probability p
    @raises ValueError if probability is not between 0 and 1
    '''
    if p < 0.0 or p > 1.0:
        raise ValueError('Probability must be between 0 and 1')
    G = Graph(V)
    for v in range(V):
        for w in range(v+1,V,1):
            if utils.bernoulli(p):
                G.add_edge((v , w))
    return G

def bipartite(V1, V2, E):
    '''
     * Returns a random simple bipartite graph on V1 and V2 vertices
     * with E edges.
     * @param V1 the number of vertices in one partition
     * @param V2 the number of vertices in the other partition
     * @param E the number of edges
     * @return a random simple bipartite graph on V1 and V2 vertices,
     *    containing a total of E edges
     * @raises ValueError if no such simple bipartite graph exists
    '''
    if E > V1*V2:
        raise ValueError('Too many edges')
    if E < 0:
        raise ValueError('Too few edges')
    G = Graph(V1+V2)
    vertices = [i for i in range(V1+V2)]
    rand.shuffle(vertices)
    edges = []
    while G.E() < E:
        i = rand.randrange(V1)
        j = V1 + rand.randrange(V2)
        e = (vertices[i] , vertices[j])
        if e not in edges:
            edges.append(e)
            G.add_edge(e)
    return G

def bipartite_with_probability(V1, V2, p):
    '''
    Returns a random simple bipartite graph on V1 and V2 vertices,
    containing each possible edge with probability p.
    @param V1 the number of vertices in one partition
    @param V2 the number of vertices in the other partition
    @param p the probability that the graph contains an edge with one endpoint in either side
    @return a random simple bipartite graph on V1 and V2 vertices,
     containing each possible edge with probability p
    @raises ValueError if probability is not between 0 and 1
    '''
    if p < 0.0 or p > 1.0:
        raise ValueError('Probability must be between 0 and 1')
    vertices = [i for i in range(V1 + V2)]
    rand.shuffle(vertices)
    G = Graph(V1 + V2)
    for i in range(V1):
        for j in range(V2):
            if utils.bernoulli(p):
                G.add_edge((vertices[i], vertices[V1+j]))
    return G


def path(V):
    '''
    Returns a path graph on V vertices.
    @param V the number of vertices in the path
    @return a path graph on V vertices
    '''
    G = Graph(V)
    vertices = [i for i in range(V)]
    rand.shuffle(vertices)
    for i in range(V-1):
        G.add_edge((vertices[i],vertices[i+1]))
    return G

def cycle(V):
    '''
    Returns a cycle graph on V vertices.
    @param V the number of vertices in the cycle
    @return a cycle graph on V vertices
    '''
    G = Graph(V)
    vertices = [i for i in range(V)]
    rand.shuffle(vertices)
    for i in range(V-1):
        G.add_edge((vertices[i], vertices[i+1]))
    G.add_edge((vertices[V-1], vertices[0]))
    return G


def eulerianCycle(V, E):
    '''
    Returns an Eulerian cycle graph on V vertices.
    @param  V the number of vertices in the cycle
    @param  E the number of edges in the cycle
    @return a graph that is an Eulerian cycle on V vertices and E edges
    @raises ValueError if either V <= 0 or E <= 0
    '''
    if E <= 0:
        raise ValueError("An Eulerian cycle must have at least one edge")
    if V <= 0:
        raise ValueError("An Eulerian cycle must have at least one vertex")
    G = Graph(V)
    vertices = [rand.randrange(V) for i in range(E)]
    for i in range(E-1):
        G.add_edge((vertices[i], vertices[i+1]))
    G.add_edge((vertices[E-1], vertices[0]))
    return G

def eulerianPath(V, E):
    '''
    Returns an Eulerian path graph on V vertices.
    @param  V the number of vertices in the path
    @param  E the number of edges in the path
    @return a graph that is an Eulerian path on V vertices and E edges
    @raises ValueError if either V <= 0 or E < 0
    '''
    if E < 0:
        raise ValueError("negative number of edges")
    if V <= 0:
        raise ValueError("An Eulerian path must have at least one vertex")
    G = Graph(V)
    vertices = []
    for i in range(E+1):
        vertices[i] = rand.randrange(V)
    for i in range(E):
        G.add_edge((vertices[i], vertices[i+1]))
    return G

def wheel(V):
    '''
    Returns a wheel graph on V vertices.
    @param V the number of vertices in the wheel
    @return a wheel graph on V vertices: a single vertex connected to
    every vertex in a cycle on V-1 vertices
    '''
    if V <= 1:
        raise ValueError("Number of vertices must be at least 2")
    G = Graph(V)
    vertices = [i for i in range(V)]
    rand.shuffle(vertices)
    # simple cycle on V-1 vertices
    for i in range(V-1):
        G.add_edge((vertices[i], vertices[i+1]))
    G.add_edge((vertices[V-1], vertices[1]))
    # connect vertices[0] to every vertex on cycle
    for i in range(V):
        G.add_edge((vertices[0], vertices[i]))

    return G

def star(V):
    '''
    Returns a star graph on V vertices.
    @param V the number of vertices in the star
    @return a star graph on V vertices: a single vertex connected to
     every other vertex
    '''
    if V <= 0:
        raise ValueError("Number of vertices must be at least 1")
    G = Graph(V)
    vertices = [i for i in range(V)]
    rand.shuffle(vertices)
    # connect vertices[0] to every other vertex
    for i in range(V):
        G.add_edge((vertices[0], vertices[i]))    
    return G

def regular(V, k):
    '''
    Returns a uniformly random k-regular graph on V vertices
    (not necessarily simple). The graph is simple with probability only about e^(-k^2/4),
    which is tiny when k = 14.
    @param V the number of vertices in the graph
    @param k degree of each vertex
    @return a uniformly random k-regular graph on V vertices.
    '''
    if V*k % 2 != 0:
        raise ValueError("Number of vertices * k must be even")
    G = Graph(V)
    # create k copies of each vertex
    vertices = [0 for _ in range(V*k)]
    for v in range(V):
        for j in range(k):
            vertices[v + V*j] = v

    # pick a random perfect matching
    rand.shuffle(vertices)
    for i in range(V*k//2):
        G.add_edge((vertices[2*i], vertices[2*i + 1]))
    return G