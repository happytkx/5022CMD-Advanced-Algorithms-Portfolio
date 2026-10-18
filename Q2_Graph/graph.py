class Graph:
    def __init__(self):
        self.adjacency = {}

    # Adds a new vertex
    def addVertex(self , vertex):
        # Checks if the vertex already exist in the graph
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []

    # Adds a directed edge
    def addEdge(self, from_vertex, to_vertex):
        if from_vertex in self.adjacency and to_vertex in self.adjacency:
            # Prevents duplicate edges
            if to_vertex not in self.adjacency[from_vertex]:
                # Adds the vertex to the outgoing list of the starting vertex
                self.adjacency[from_vertex].append(to_vertex)

    # Lists all vertices with an incoming edge to the selected vertex
    def listIncomingAdjacentVertex(self, vertex):
        incoming_vertices = []

        for current_vertex in self.adjacency:
            if vertex in self.adjacency[current_vertex]:
                incoming_vertices.append(current_vertex)

        return incoming_vertices

    # Lists all vertices that the selected vertex points to
    def listOutgoingAdjacentVertex(self, vertex):
        if vertex in self.adjacency:
            return self.adjacency[vertex]

        return []