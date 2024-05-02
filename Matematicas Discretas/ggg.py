import random
from collections import defaultdict
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacenciesList = []
        self.predecessor = None
        self.minDistance = float('inf')

class Edge:
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

class Graph:
    def __init__(self):
        self.nodes = defaultdict(Node)
        self.edges = []

    def add_node(self, name):
        self.nodes[name] = Node(name)

    def add_edge(self, start, end):
        weight = random.randint(1, 10)
        edge = Edge(weight, self.nodes[start], self.nodes[end])
        self.edges.append(edge)
        self.nodes[start].adjacenciesList.append(edge)

    def shortest_path(self, start, end):
        heap = []
        start_node = self.nodes[start]
        start_node.minDistance = 0
        heapq.heappush(heap, start_node)

        while len(heap) > 0:
            actual_node = heapq.heappop(heap)

            for edge in actual_node.adjacenciesList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    heapq.heappush(heap, v)

        path = []
        actual_node = self.nodes[end]

        while actual_node is not None:
            path.append(actual_node.name)
            actual_node = actual_node.predecessor

        return path[::-1]

graph = Graph()

node_names = ['A', 'B', 'C', 'D', 'E']
for node_name in node_names:
    graph.add_node(node_name)

for node_name in node_names:
    connected_nodes = random.sample(node_names, random.randint(1, len(node_names)))
    connected_nodes = [node for node in connected_nodes if node != node_name]  # A node cannot connect to itself
    for connected_node in connected_nodes:
        graph.add_edge(node_name, connected_node)

G = nx.Graph()

for node in graph.nodes.values():
    G.add_node(node.name)

for edge in graph.edges:
    G.add_edge(edge.startVertex.name, edge.targetVertex.name, weight=edge.weight)

pos = {node: (random.random(), random.random()) for node in G.nodes()}
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()