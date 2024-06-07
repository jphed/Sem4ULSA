# Importando las bibliotecas necesarias
import networkx as nx
import matplotlib.pyplot as plt
import random

# Creando un grafo dirigido
G = nx.DiGraph()

# Añadiendo nodos y aristas al grafo de manera aleatoria
nodos = random.randint(3, 7)
for i in range(nodos):
    G.add_node(i)
    if i > 0:
        G.add_edge(i, random.randint(0, i-1))

# Dibujando el grafo
nx.draw(G, with_labels=True)
plt.show()