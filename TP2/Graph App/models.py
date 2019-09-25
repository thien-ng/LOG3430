
class Graph(object):

    def __init__(self, V, graph_dict=None):
        """ initializes a graph object with V vertices
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if V < 0:
            raise ValueError("Number of vertices must be nonnegative")
        self.__V = V
        self.__E = 0
        if graph_dict == None:
            graph_dict = {i:[] for i in range(V)}
        self.__graph_dict = graph_dict

    def V(self):
        return self.__V      
    
    def E(self):
        return self.__E

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        self.validate_vertex(vertex)
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
    
    def validate_vertex(self, vertex):
        '''raises ValueError unless 0 <= v < V'''
        if vertex < 0 or vertex >= self.__V:
            raise ValueError("vertex " + vertex + " is not between 0 and " + (self.__V-1))

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        if set(edge) not in self.__generate_edges():
            self.__E += 1
            vertex1, vertex2 = edge
            if vertex1 in self.__graph_dict:
                self.__graph_dict[vertex1].append(vertex2)
            else:
                self.validate_vertex(vertex1)
                self.__graph_dict[vertex1] = [vertex2]
            if vertex1 != vertex2:
                if vertex2 in self.__graph_dict:
                    self.__graph_dict[vertex2].append(vertex1)
                else:
                    self.validate_vertex(vertex2)
                    self.__graph_dict[vertex2] = [vertex1]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res