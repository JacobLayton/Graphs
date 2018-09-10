"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    # def add_edge(self, edge):
    #     edge = set(edge)
    #     (vertex1, vertex2) = tuple(edge)
    #     if vertex1 in self.vertices:
    #         self.vertices[vertex1].append(vertex2)
    #     else:
    #         self.vertices[vertex1] = [vertex2]

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            print(f"Cannot create edge between {vertex1} and {vertex2}, vertex does not exist")
            return
        self.vertices[vertex1].add(vertex2)
        self.vertices[vertex2].add(vertex1)

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
graph.add_edge('0', '4')