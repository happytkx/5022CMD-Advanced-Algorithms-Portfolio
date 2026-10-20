class Graph:
    def __init__(self):
        # Each vertex maps to a list of vertices it points to
        self.adjacency = {}

    # Adds a new vertex
    def addVertex(self, vertex):
        # Checks if the vertex already exists in the graph
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []

    # Adds a directed edge
    def addEdge(self, from_vertex, to_vertex):
        if from_vertex in self.adjacency and to_vertex in self.adjacency:
            # Prevents duplicate edges
            if to_vertex not in self.adjacency[from_vertex]:
                # Adds the vertex to the outgoing list of the starting vertex
                self.adjacency[from_vertex].append(to_vertex)

    # Finds all vertices that point to the selected vertex
    def listIncomingAdjacentVertex(self, vertex):
        incoming_vertices = []

        for current_vertex in self.adjacency:
            if vertex in self.adjacency[current_vertex]:
                incoming_vertices.append(current_vertex)

        return incoming_vertices

    # Lists all vertices directly reached from the selected vertex
    def listOutgoingAdjacentVertex(self, vertex):
        if vertex in self.adjacency:
            return self.adjacency[vertex]

        return []

    # Checks whether a path exists from one vertex to another
    def hasPath(self, start_vertex, target_vertex):
        if start_vertex not in self.adjacency or target_vertex not in self.adjacency:
            return False

        # Stores vertices that have already been checked
        visited = []
        # Stores vertices that still need to be checked
        stack = [start_vertex]

        while len(stack) > 0:
            # Takes the most recently added vertex from the stack
            current_vertex = stack.pop()

            # Target reached, so a path exists
            if current_vertex == target_vertex:
                return True

            if current_vertex not in visited:
                visited.append(current_vertex)

                # Add unvisited outgoing neighbours to the stack
                for adjacent_vertex in self.adjacency[current_vertex]:
                    if adjacent_vertex not in visited:
                        stack.append(adjacent_vertex)

        return False