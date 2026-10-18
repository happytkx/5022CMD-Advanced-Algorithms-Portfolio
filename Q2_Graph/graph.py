class Graph:
    def __init__(self):
        self.adjacency = {}

    # Add new vertex
    def addVertex(self , vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []

