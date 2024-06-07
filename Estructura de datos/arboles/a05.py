import matplotlib.pyplot as plt
import networkx as nx

# Crear un gráfico dirigido
G = nx.DiGraph()

# Agregar los nodos y las aristas al gráfico
G.add_edge(4, 2)
G.add_edge(4, 6)
G.add_edge(2, 1)
G.add_edge(2, 3)
G.add_edge(6, 5)
G.add_edge(6, 7)

# Dibujar el gráfico
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=False)

# Mostrar el gráfico
plt.show()