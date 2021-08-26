# Peadar O'Connor 117302273
""" Sample solutions for first lab on graphs.

    Implements the graph as a map of (vertex,edge-map) pairs.
"""


class Vertex:
    """ A Vertex in a graph. """

    def __init__(self, element):
        """ Create a vertex, with a data element.

        Args:
            element - the data or label to be associated with the vertex
        """
        self._element = element

    def __str__(self):
        """ Return a string representation of the vertex. """
        return str(self._element)

    def __lt__(self, v):
        """ Return true if this element is less than v's element.

        Args:
            v - a vertex object
        """
        return self._element < v.element()

    def element(self):
        """ Return the data for the vertex. """
        return self._element


class Edge:
    """ An edge in a graph.

        Implemented with an order, so can be used for directed or undirected
        graphs. Methods are provided for both. It is the job of the Graph class
        to handle them as directed or undirected.
    """

    def __init__(self, v, w, element):
        """ Create an edge between vertices v and w, with a data element.

        Element can be an arbitrarily complex structure.

        Args:
            element - the data or label to be associated with the edge.
        """
        self._vertices = (v, w)
        self._element = element

    def __str__(self):
        """ Return a string representation of this edge. """
        return ('(' + str(self._vertices[0]) + '--'
                + str(self._vertices[1]) + ' : '
                + str(self._element) + ')')

    def vertices(self):
        """ Return an ordered pair of the vertices of this edge. """
        return self._vertices

    def start(self):
        """ Return the first vertex in the ordered pair. """
        return self._vertices[0]

    def end(self):
        """ Return the second vertex in the ordered pair. """
        return self._vertices[1]

    def opposite(self, v):
        """ Return the opposite vertex to v in this edge.

        Args:
            v - a vertex object
        """
        if self._vertices[0] == v:
            return self._vertices[1]
        elif self._vertices[1] == v:
            return self._vertices[0]
        else:
            return None

    def element(self):
        """ Return the data element for this edge. """
        return self._element


class Graph:
    """ Represent a simple graph.

    This version maintains only undirected graphs, and assumes no
    self loops.

    Implements the Adjacency Map style. Also maintains a top level
    dictionary of vertices.
    """

    # Implement as a Python dictionary
    #  - the keys are the vertices
    #  - the values are the sets of edges for the corresponding vertex.
    #    Each edge set is also maintained as a dictionary,
    #    with the opposite vertex as the key and the edge object as the value.

    def __init__(self):
        """ Create an initial empty graph. """
        self._structure = dict()

    def __str__(self):
        """ Return a string representation of the graph. """
        hstr = ('|V| = ' + str(self.num_vertices())
                + '; |E| = ' + str(self.num_edges()))
        vstr = '\nVertices: '
        for v in self._structure:
            vstr += str(v) + '-'
        edges = self.edges()
        estr = '\nEdges: '
        for e in edges:
            estr += str(e) + ' '
        return hstr + vstr + estr

    # -----------------------------------------------------------------------#

    # ADT methods to query the graph

    def num_vertices(self):
        """ Return the number of vertices in the graph. """
        return len(self._structure)

    def num_edges(self):
        """ Return the number of edges in the graph. """
        num = 0
        for v in self._structure:
            num += len(self._structure[v])  # the dict of edges for v
        return num // 2  # divide by 2, since each edege appears in the
        # vertex list for both of its vertices

    def vertices(self):
        """ Return a list of all vertices in the graph. """
        return [key for key in self._structure]

    def get_vertex_by_label(self, element):
        """ Return the first vertex that matches element. """
        for v in self._structure:
            if v.element() == element:
                return v
        return None

    def edges(self):
        """ Return a list of all edges in the graph. """
        edgelist = []
        for v in self._structure:
            for w in self._structure[v]:
                # to avoid duplicates, only return if v is the first vertex
                if self._structure[v][w].start() == v:
                    edgelist.append(self._structure[v][w])
        return edgelist

    def get_edges(self, v):
        """ Return a list of all edges incident on v.

        Args:
            v - a vertex object
        """
        if v in self._structure:
            edgelist = []
            for w in self._structure[v]:
                edgelist.append(self._structure[v][w])
            return edgelist
        return None

    def get_edge(self, v, w):
        """ Return the edge between v and w, or None.

        Args:
            v - a vertex object
            w - a vertex object
        """
        if (self._structure is not None
                and v in self._structure
                and w in self._structure[v]):
            return self._structure[v][w]
        return None

    def degree(self, v):
        """ Return the degree of vertex v.

        Args:
            v - a vertex object
        """
        return len(self._structure[v])

    # ----------------------------------------------------------------------#

    # ADT methods to modify the graph

    def add_vertex(self, element):
        """ Add a new vertex with data element.

        If there is already a vertex with the same data element,
        this will create another vertex instance.
        """
        v = Vertex(element)
        self._structure[v] = dict()
        return v

    def add_vertex_if_new(self, element):
        """ Add and return a vertex with element, if not already in graph.

        Checks for equality between the elements. If there is special
        meaning to parts of the element (e.g. element is a tuple, with an
        'id' in cell 0), then this method may create multiple vertices with
        the same 'id' if any other parts of element are different.

        To ensure vertices are unique for individual parts of element,
        separate methods need to be written.

        """
        for v in self._structure:
            if v.element() == element:
                return v
        return self.add_vertex(element)

    def add_edge(self, v, w, element):
        """ Add and return an edge between two vertices v and w, with  element.

        If either v or w are not vertices in the graph, does not add, and
        returns None.

        If an edge already exists between v and w, this will
        replace the previous edge.

        Args:
            v - a vertex object
            w - a vertex object
            element - a label
        """
        if v not in self._structure or w not in self._structure:
            return None
        e = Edge(v, w, element)
        self._structure[v][w] = e
        self._structure[w][v] = e
        return e

    def add_edge_pairs(self, elist):
        """ add all vertex pairs in elist as edges with empty elements.

        Args:
            elist - a list of pairs of vertex objects
        """
        for (v, w) in elist:
            self.add_edge(v, w, None)

    # ---------------------------------------------------------------------#

    # Additional methods to explore the graph

    def highestdegreevertex(self):
        """ Return the vertex with highest degree. """
        hd = -1
        hdv = None
        for v in self._structure:
            if self.degree(v) > hd:
                hd = self.degree(v)
                hdv = v
        return hdv

    def depthfirstsearch(self, v):
        """ Traverse through a graph from a given vertex. Moves along an edge until the
        branch runs out, then backtracks to find the next unvisited edge.

        Args:
            v - a vertex object
        """
        marked = {v: None}
        self._depthfirstsearch(v, marked)
        for k, v in marked.items():
            print(k, v)
        return marked

    def _depthfirstsearch(self, v, marked):
        for e in self.get_edges(v):
            w = e.opposite(v)
            if w not in marked:
                marked[w] = e
                self._depthfirstsearch(w, marked)

    def breadthfirstsearch(self, v):
        """ Traverse through a graph from a given vertex. Visits all vertices that are
        one edge away before visiting vertices two edges away etc.

        Args:
            v - a vertex object
        """
        marked = {v: None}
        v_list = [v]
        current_level = [0]
        num_moves = []
        self._breadthfirstsearch(v_list, marked, current_level, num_moves)
        max_distance = 0
        for item in num_moves:
            max_distance += item[1]
        return marked, num_moves, max_distance

    def _breadthfirstsearch(self, v_list, marked, current_level, num_moves):
        next_level = []
        for v in v_list:
            for e in self.get_edges(v):
                w = e.opposite(v)
                if w not in marked:
                    marked[w] = e
                    next_level.append(w)
                    num_moves.append((v, current_level[0] + 1))
        if next_level:
            current_level[0] += 1
            self._breadthfirstsearch(next_level, marked, current_level, num_moves)

    def paths_distances(self, search_tree):
        print("dont know")

    def determine_minimum_max(self):
        """ Runs breadth first search for each vertex, and then determines
        which vertex had the minimum max distance"""
        v_list = self.vertices()
        results_list = []
        for v in v_list:
            result = self.breadthfirstsearch(v)
            results_list.append((result, v))
        maximums_list = []
        # iterates through each tree made from BFS of each vertex
        for tuple in results_list:
            breadth_result = tuple[0][1]
            max_distance = 0
            # adds up distances from root to each vertex
            for item in breadth_result:
                max_distance += item[1]
            maximums_list.append((max_distance, tuple[1]))
        minimum = [maximums_list[0][0], maximums_list[1][0]]
        for item in maximums_list:
            if item[0] < minimum[0]:
                minimum = [item[0], item[1]]
        return minimum[0], str(minimum[1])

    def dijkstra(self, s):
        """ Prints and returns the shortest paths between nodes in a graph. Uses an adaptable
        priority queue to keep track of open vertices. It picks the open vertex with the lowest
        distance, expands to its neighbours and finds the cost to move to the neighbour through
        the open vertex, and updates the neighbours path cost if the cost found is lower.

        Args:
            s - a vertex object
        """
        open = AdaptablePriorityQueue()
        locs = {}
        closed = {}
        preds = {s: None}

        # add given vertex to apq
        element = open.add(0, s)
        locs[s] = element
        # code runs until there are no more open vertices
        while open.length() != 0:
            v = open.remove_min()
            v_cost = v._key
            v = v._value
            predecessor = preds.pop(v)
            closed[v] = (v_cost, predecessor)
            for e in self.get_edges(v):
                # finds all the neighbours
                w = e.opposite(v)
                if w not in closed:
                    newcost = v_cost + int(e.element())
                    # not yet added to open
                    if w not in locs:
                        preds[w] = v
                        elt = open.add(newcost, w)
                        locs[w] = elt
                    # if newcost is better than the neighbour's old cost
                    elif newcost < open.get_key(locs[w]):
                        preds[w] = v
                        open.update_key(locs[w], newcost)

        shortest_paths = ""
        for key, value in closed.items():
            shortest_paths += "Vertex %s -> Shortest path cost = %i, Preceding vertex = %s \n" % (key,
                                                                                                  value[0],
                                                                                                  value[1])
        print(shortest_paths)
        return closed



def graphreader(filename):
    """ Read and return the route map in filename. """
    graph = Graph()
    file = open(filename, 'r')
    entry = file.readline() #either 'Node' or 'Edge'
    num = 0
    while entry == 'Node\n':
        num += 1
        nodeid = int(file.readline().split()[1])
        vertex = graph.add_vertex(nodeid)
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'vertices and added into the graph')
    num = 0
    while entry == 'Edge\n':
        num += 1
        source = int(file.readline().split()[1])
        sv = graph.get_vertex_by_label(source)
        target = int(file.readline().split()[1])
        tv = graph.get_vertex_by_label(target)
        length = float(file.readline().split()[1])
        edge = graph.add_edge(sv, tv, length)
        file.readline() #read the one-way data
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'edges and added into the graph')
    print(graph)
    return graph


class Element:
    """ A key, value and index. For use in the Adaptable Priority Queue. """
    def __init__(self, k, v, i):
        self._key = k
        self._value = v
        self._index = i

    def __eq__(self, other):
        return self._key == other._key

    def __lt__(self, other):
        return self._key < other._key

    def __gt__(self, other):
        return self._key > other._key

    def __hash__(self):
        return hash(str(self))

    def _wipe(self):
        self._key = None
        self._value = None
        self._index = None

    def __str__(self):
        return "Key = %s Value = %s Index = %s" % (str(self._key),
                                                   str(self._value),
                                                   str(self._index))


class BinaryHeap:
    def __init__(self):
        """ Construct an empty binary heap. """
        self._heap = []
        self._last_pos = 0
        self._size = 0

    def __str__(self):
        full_string = ""
        for item in self._heap:
            full_string += "%s, " % str(item)
        return full_string

    def length(self):
        return self._size

    def is_empty(self):
        if self._size == 0:
            return True
        return False

    def get_root(self):
        if not self._heap:
            return None
        return self._heap[0]

    def left_child(self, index):
        """ Locate the left child of the item at the provided index. """
        return (2 * index) + 1

    def right_child(self, index):
        """ Locate the right child of the item at the provided index. """
        return (2 * index) + 2

    def parent(self, index):
        """ Locate the parent of the item at the provided index. """
        return (index - 1) // 2

    def checkLeaf(self, index):
        """ Check if the element at this index is a leaf. """
        if ((2 * index) + 1) <= self._size - 2:
            return False
        return True

    def checkTwoChildren(self, index):
        """ Check if the element at this index has two children. """
        if ((2 * index) + 2) <= self._size - 2:
            return True
        return False

    def swap(self, first, second):
        """ Swap two different items in the heap using their indexes. """
        first_value = self._heap[first]
        self._heap[first] = self._heap[second]
        self._heap[second] = first_value

    def swap_index(self, first, second):
        """ Swap the index values of two elements in the heap. """
        first_value = self._heap[first]._index
        self._heap[first]._index = self._heap[second]._index
        self._heap[second]._index = first_value

    def add(self, key, value):
        """ Add something to the end of the heap, then bubble up to
        the right place in the heap. """
        element = Element(key, value, self._last_pos)
        self._heap.append(element)
        self.bubble_up(self._last_pos)
        self._last_pos += 1
        self._size += 1
        return element

    def remove_root(self):
        """ Remove the root of the heap, then re-balance by bubbling down """
        old_root = self._heap[0]
        self._heap[0] = self._heap[self._last_pos - 1]
        self.get_root()._index = 0
        self._heap.pop()
        self.bubble_down(0)
        self._last_pos -= 1
        self._size -= 1
        return old_root

    def bubble_up(self, index):
        """ Put the element in the right position by recursively moving it up the heap """
        if index > 0:
            if self._heap[index] < self._heap[self.parent(index)]:
                self.swap_index(index, self.parent(index))
                self.swap(index, self.parent(index))
                self.bubble_up(self.parent(index))

    def bubble_down(self, index):
        """ Put the element in the right position by recursively moving it down the heap """
        if not self.checkLeaf(index):
            if self.checkTwoChildren(index):
                left = self._heap[self.left_child(index)]
                right = self._heap[self.right_child(index)]
                if left < right:
                    target = self.left_child(index)
                else:
                    target = self.right_child(index)
            else:
                target = self.left_child(index)
            if self._heap[index] > self._heap[target]:
                self.swap_index(index, target)
                self.swap(index, target)
                self.bubble_down(target)


class AdaptablePriorityQueue:
    def __init__(self):
        """ Construct an empty APQ """
        self._heap = BinaryHeap()
        self._reference_dict = {}

    def add(self, key, item):
        """ Add element to the APQ with given key and item """
        return self._heap.add(key, item)

    def min(self):
        """ Return element with lowest key. """
        return self._heap.get_root()

    def remove_min(self):
        """ Remove element with lowest key. """
        return self._heap.remove_root()

    def length(self):
        return self._heap.length()

    def update_key(self, element, new_key):
        """ Change the provided element's key to a given new one, and re-balance the
        Heap if needed. """
        element._key = new_key
        if element < self._heap._heap[self._heap.parent(element._index)]:
            self._heap.bubble_up(element._index)
        else:
            self._heap.bubble_down(element._index)

    def get_key(self, element):
        """ Return a given elements key. """
        return self._heap._heap[element._index]._key

    def remove(self, element):
        """ Remove a given element from the APQ, and re-balance the Heap if needed. """
        original_index = element._index
        self._heap.swap(element._index, self._heap._last_pos - 1)
        self._heap.swap_index(element._index, self._heap._last_pos - 1)
        print(self._heap)
        if self._heap._heap[original_index] < self._heap._heap[self._heap.parent(original_index)]:
            self._heap.bubble_up(original_index)
        else:
            self._heap.bubble_down(original_index)
        self._heap._heap.pop()
        self._heap._last_pos -= 1
        self._heap._size -= 1
        return element._key, element._value

    def __str__(self):
        return str(self._heap)


def routemapreader(filename):
    """ Read and return the route map in filename. """
    routemap = RouteMap()
    file = open(filename, 'r')
    entry = file.readline() #either 'Node' or 'Edge'
    num = 0
    while entry == 'Node\n':
        num += 1
        nodeid = int(file.readline().split()[1])
        coordinates = file.readline().split()
        lat = float(coordinates[1])
        long = float(coordinates[2])
        vertex = routemap.add_vertex(nodeid)
        routemap.add_coordinates(vertex, lat, long)
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'vertices and added into the routemap')
    num = 0
    while entry == 'Edge\n':
        num += 1
        source = int(file.readline().split()[1])
        sv = routemap.get_vertex_by_label(source)
        target = int(file.readline().split()[1])
        tv = routemap.get_vertex_by_label(target)
        length = float(file.readline().split()[1])
        time = float(file.readline().split()[1])
        edge = routemap.add_edge(sv, tv, time)
        file.readline() #read the one-way data
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'edges and added into the routemap')
    print(routemap)
    return routemap

'''
class Coordinates:
    """  Co-ordinates for a location in the route map. """
    def __init__(self, latitude, longitude):
        self._latitude = float(latitude)
        self._longitude = float(longitude)

    def latitude(self):
        """ Return data for latitude """
        return self._latitude

    def longitude(self):
        """ Return data for longitude """
        return self._longitude

    def __str__(self):
        """ Return string representation of lat and long"""
        return "Latitude = %+.6f, Longitude = %+.6f" % (self.latitude(), self.longitude())
'''

class RouteMap:
    """ Represent a simple route map.

    This version maintains only undirected graphs, and assumes no
    self loops.

    Implements the Adjacency Map style. Also maintains a top level
    dictionary of vertices.
    """

    # Implement as a Python dictionary
    #  - the keys are the vertices
    #  - the values are the sets of edges for the corresponding vertex.
    #    Each edge set is also maintained as a dictionary,
    #    with the opposite vertex as the key and the edge object as the value.

    def __init__(self):
        """ Create an initial empty graph. """
        self._structure = dict()
        # dictionary to associate each vertex with a latitude and longitude
        self._vertex_coordinates = dict()
        # dictionary to speed up getting the vertex by label
        self._vertex_ref = dict()

    def __str__(self):
        """ Return a string representation of the graph. """
        hstr = ('|V| = ' + str(self.num_vertices())
                + '; |E| = ' + str(self.num_edges()))
        vstr = '\nVertices: '
        i = 0
        for v in self._structure:
            # only prints the first 100
            if i >= 100:
                break
            vstr += str(v) + '-'
            i += 1
        edges = self.edges()
        estr = '\nEdges: '
        j = 0
        for e in edges:
            if j >= 100:
                break
            estr += str(e) + ' '
            j += 1
        return hstr + vstr + estr

    # -----------------------------------------------------------------------#

    # ADT methods to query the graph

    def num_vertices(self):
        """ Return the number of vertices in the graph. """
        return len(self._structure)

    def num_edges(self):
        """ Return the number of edges in the graph. """
        num = 0
        for v in self._structure:
            num += len(self._structure[v])  # the dict of edges for v
        return num // 2  # divide by 2, since each edege appears in the
        # vertex list for both of its vertices

    def vertices(self):
        """ Return a list of all vertices in the graph. """
        return [key for key in self._structure]

    def get_vertex_by_label(self, element):
        """ Return the first vertex that matches element. """
        try:
            return self._vertex_ref[element]
        except KeyError:
            return None

    def edges(self):
        """ Return a list of all edges in the graph. """
        edgelist = []
        for v in self._structure:
            for w in self._structure[v]:
                # to avoid duplicates, only return if v is the first vertex
                if self._structure[v][w].start() == v:
                    edgelist.append(self._structure[v][w])
        return edgelist

    def get_edges(self, v):
        """ Return a list of all edges incident on v.

        Args:
            v - a vertex object
        """
        if v in self._structure:
            edgelist = []
            for w in self._structure[v]:
                edgelist.append(self._structure[v][w])
            return edgelist
        return None

    def get_edge(self, v, w):
        """ Return the edge between v and w, or None.

        Args:
            v - a vertex object
            w - a vertex object
        """
        if (self._structure is not None
                and v in self._structure
                and w in self._structure[v]):
            return self._structure[v][w]
        return None

    def get_coordinates(self, v):
        """ Return a given vertex's latitude and longitude """
        return self._vertex_coordinates[v]

    def degree(self, v):
        """ Return the degree of vertex v.

        Args:
            v - a vertex object
        """
        return len(self._structure[v])

    # ----------------------------------------------------------------------#

    # ADT methods to modify the graph

    def add_vertex(self, element):
        """ Add a new vertex with data element.

        If there is already a vertex with the same data element,
        this will create another vertex instance.
        """
        v = Vertex(element)
        self._structure[v] = dict()
        self._vertex_ref[element] = v
        return v

    def add_vertex_if_new(self, element):
        """ Add and return a vertex with element, if not already in graph.

        Checks for equality between the elements. If there is special
        meaning to parts of the element (e.g. element is a tuple, with an
        'id' in cell 0), then this method may create multiple vertices with
        the same 'id' if any other parts of element are different.

        To ensure vertices are unique for individual parts of element,
        separate methods need to be written.

        """
        for v in self._structure:
            if v.element() == element:
                return v
        return self.add_vertex(element)

    def add_edge(self, v, w, element):
        """ Add and return an edge between two vertices v and w, with  element.

        If either v or w are not vertices in the graph, does not add, and
        returns None.

        If an edge already exists between v and w, this will
        replace the previous edge.

        Args:
            v - a vertex object
            w - a vertex object
            element - a label
        """
        if v not in self._structure or w not in self._structure:
            return None
        e = Edge(v, w, element)
        self._structure[v][w] = e
        self._structure[w][v] = e
        return e

    def add_edge_pairs(self, elist):
        """ add all vertex pairs in elist as edges with empty elements.

        Args:
            elist - a list of pairs of vertex objects
        """
        for (v, w) in elist:
            self.add_edge(v, w, None)

    def add_coordinates(self, vertex, lat, long):
        """ Associates a vertex with some co-ordinates """
        self._vertex_coordinates[vertex] = (lat, long)

    # ---------------------------------------------------------------------#

    # Additional methods to explore the graph

    def highestdegreevertex(self):
        """ Return the vertex with highest degree. """
        hd = -1
        hdv = None
        for v in self._structure:
            if self.degree(v) > hd:
                hd = self.degree(v)
                hdv = v
        return hdv

    def depthfirstsearch(self, v):
        """ Traverse through a graph from a given vertex. Moves along an edge until the
        branch runs out, then backtracks to find the next unvisited edge.

        Args:
            v - a vertex object
        """
        marked = {v: None}
        self._depthfirstsearch(v, marked)
        for k, v in marked.items():
            print(k, v)
        return marked

    def _depthfirstsearch(self, v, marked):
        for e in self.get_edges(v):
            w = e.opposite(v)
            if w not in marked:
                marked[w] = e
                self._depthfirstsearch(w, marked)

    def breadthfirstsearch(self, v):
        """ Traverse through a graph from a given vertex. Visits all vertices that are
        one edge away before visiting vertices two edges away etc.

        Args:
            v - a vertex object
        """
        marked = {v: None}
        v_list = [v]
        current_level = [0]
        num_moves = []
        self._breadthfirstsearch(v_list, marked, current_level, num_moves)
        max_distance = 0
        for item in num_moves:
            max_distance += item[1]
        return marked, num_moves, max_distance

    def _breadthfirstsearch(self, v_list, marked, current_level, num_moves):
        next_level = []
        for v in v_list:
            for e in self.get_edges(v):
                w = e.opposite(v)
                if w not in marked:
                    marked[w] = e
                    next_level.append(w)
                    num_moves.append((v, current_level[0] + 1))
        if next_level:
            current_level[0] += 1
            self._breadthfirstsearch(next_level, marked, current_level, num_moves)

    def paths_distances(self, search_tree):
        print("dont know")

    def determine_minimum_max(self):
        """ Runs breadth first search for each vertex, and then determines
        which vertex had the minimum max distance"""
        v_list = self.vertices()
        results_list = []
        for v in v_list:
            result = self.breadthfirstsearch(v)
            results_list.append((result, v))
        maximums_list = []
        # iterates through each tree made from BFS of each vertex
        for tuple in results_list:
            breadth_result = tuple[0][1]
            max_distance = 0
            # adds up distances from root to each vertex
            for item in breadth_result:
                max_distance += item[1]
            maximums_list.append((max_distance, tuple[1]))
        minimum = [maximums_list[0][0], maximums_list[1][0]]
        for item in maximums_list:
            if item[0] < minimum[0]:
                minimum = [item[0], item[1]]
        return minimum[0], str(minimum[1])

    def dijkstra(self, s):
        """ Prints and returns the shortest paths between nodes in a graph. Uses an adaptable
        priority queue to keep track of open vertices. It picks the open vertex with the lowest
        distance, expands to its neighbours and finds the cost to move to the neighbour through
        the open vertex, and updates the neighbours path cost if the cost found is lower.

        Args:
            s - a vertex object
        """
        open = AdaptablePriorityQueue()
        locs = {}
        closed = {}
        preds = {s: None}

        # add given vertex to apq
        element = open.add(0, s)
        locs[s] = element
        # code runs until there are no more open vertices
        while open.length() != 0:
            v = open.remove_min()
            v_cost = v._key
            v = v._value
            predecessor = preds.pop(v)
            closed[v] = (v_cost, predecessor)
            for e in self.get_edges(v):
                # finds all the neighbours
                w = e.opposite(v)
                if w not in closed:
                    newcost = v_cost + e.element()
                    # not yet added to open
                    if w not in locs:
                        preds[w] = v
                        elt = open.add(newcost, w)
                        locs[w] = elt
                    # if newcost is better than the neighbour's old cost
                    elif newcost < open.get_key(locs[w]):
                        preds[w] = v
                        open.update_key(locs[w], newcost)

        shortest_paths = ""
        for key, value in closed.items():
            shortest_paths += "Vertex %s -> Shortest path cost = %f, Preceding vertex = %s \n" % (key,
                                                                                                  value[0],
                                                                                                  value[1])
        return closed

    def sp(self, v, w):
        """ Calls for dijkstra's algorithm to be done on v, and returns a list of
        each vertex and their cost in the path from v to w.

        Args:
            v - a vertex object
            w - a different vertex object
        """
        dijkstra_result = self.dijkstra(v)
        route_list_backwards = []
        vertex_of_path = w
        # will run until break is reached.
        while True:
            # one result from the full dijkstra algorithm
            single_result = dijkstra_result[vertex_of_path]
            # finds the edge between the current and preceding vertex
            edge = self.get_edge(vertex_of_path, single_result[1])
            # is none only if its the first vertex in the path
            if edge is not None:
                edge_value = edge.element()
            else:
                edge_value = 0
            vertex_info = (vertex_of_path, edge_value)
            route_list_backwards.append(vertex_info)
            # if it reaches the first vertex in the path
            if vertex_of_path == v:
                break
            # single_result[1] is the previous vertex in the path
            vertex_of_path = single_result[1]
        route_list = route_list_backwards[::-1]
        return route_list

    def printvlist(self, path_list):
        """ Prints the path returned in the sp method. Prints the latitude and longitude
        of each vertex as well.

        Args:
            v - a vertex object
            w - a different vertex object
        """
        print("type\tlatitude\tlongitude\telement\tcost")
        for item in path_list:
            coords = self.get_coordinates(item[0])
            vertex_str = "W\t%f\t%f\t%i\t%f" % (coords[0], coords[1], item[0].element(), item[1])
            print(vertex_str)