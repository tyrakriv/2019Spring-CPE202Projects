from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.color = None


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        
        self.graph = {}

        try:
            fin = open(filename,'r')

            for line in fin:
                readvertex = line.split()
                self.add_vertex(readvertex[0])
                self.add_vertex(readvertex[1])
                self.add_edge(readvertex[0],readvertex[1])

            fin.close()

        except FileNotFoundError:
            raise FileNotFoundError

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if key not in self.graph:
            v = Vertex(key)
            self.graph[key] = v

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key in self.graph:
            return self.graph[key]
        else:
            return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.graph[v1].adjacent_to.append(v2)
        self.graph[v1].adjacent_to.sort()
        self.graph[v2].adjacent_to.append(v1)
        self.graph[v2].adjacent_to.sort()

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        lst = []
        for item in self.graph:
            lst.append(self.graph[item].id)
        lst.sort()
        return lst

    def conn_components(self): 
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        lst = []
        stack = Stack(len(self.graph))
        vert = self.get_vertices()

        while len(vert) > 0:
            inside = []
            stack.push(self.get_vertex(vert[0]))
            while not stack.is_empty():
                item = stack.pop()
                if item.id not in inside:
                    inside.append(item.id)
                    vert.remove(item.id)

                adjlist = self.graph[item.id].adjacent_to
                for val in adjlist:
                    if val not in inside:
                        stack.push(self.get_vertex(val))
            inside.sort()
            lst.append(inside)
        lst.sort()
        return lst

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST Breadth First Search logic!'''
        vert = self.get_vertices()
        # if len(vert) == 0:
        #     return True
        q = Queue(len(vert))
        first = self.get_vertex(vert[0])
        first.color = 'b'
        q.enqueue(first)
        while not q.is_empty():
            cur = q.dequeue()
            if cur.id in vert:
                adjlist = cur.adjacent_to
                if cur.color is 'b':
                    for item in adjlist:
                        if self.get_vertex(item).color == 'b':
                            return False
                        self.get_vertex(item).color = 'r'
                        q.enqueue(self.get_vertex(item))
                elif cur.color == 'r':
                    for item in adjlist:
                        if self.get_vertex(item).color == 'r':
                            return False
                        self.get_vertex(item).color == 'b'
                        q.enqueue(self.get_vertex(item))
                vert.remove(cur.id)
        return True