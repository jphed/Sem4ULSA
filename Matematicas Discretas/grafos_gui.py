import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def get_all_paths(G, source, target, path=[]):
    path = path + [source]
    if source == target:
        return [path]
    paths = []
    for node in set(G[source]) - set(path):
        paths.extend(get_all_paths(G, node, target, path))
    return paths

def get_path_weight(G, path):
    weight = 0
    for i in range(len(path) - 1):
        weight += G[path[i]][path[i+1]]['weight']
    return weight

# Create a directed graph
G = nx.DiGraph()

# Add edges with weights
G.add_edge('A', 'B', weight=2)
G.add_edge('B', 'C', weight=4)
G.add_edge('A', 'C', weight=1)
G.add_edge('C', 'D', weight=7)
G.add_edge('D', 'E', weight=5)
G.add_edge('E', 'A', weight=4)

# Calculate the shortest path
shortest_path = nx.dijkstra_path(G, 'A', 'E')
print('Shortest path: ', shortest_path)
print('Total weight of shortest path: ', get_path_weight(G, shortest_path))

# Calculate all paths from 'A' to 'E'
all_paths = get_all_paths(G, 'A', 'E')

# Find the path with the maximum weight
max_weight_path = max(all_paths, key=lambda path: get_path_weight(G, path))
print('Path with maximum weight: ', max_weight_path)
print('Total weight of maximum weight path: ', get_path_weight(G, max_weight_path))

# Create a tkinter window
root = tk.Tk()

# Create a figure and a subplot
fig, ax = plt.subplots()

# Draw the graph on the subplot
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, ax=ax)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

# Create a canvas and add it to the tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Run the tkinter main loop
root.mainloop()