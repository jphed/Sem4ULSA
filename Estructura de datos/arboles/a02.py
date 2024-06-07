import matplotlib.pyplot as plt
import networkx as nx

# Crear un gráfico dirigido
G = nx.DiGraph()

# Agregar los nodos y las aristas al gráfico
G.add_edge('r', 'a')
G.add_edge('r', 'b')
G.add_edge('r', 'c')
G.add_edge('a', 'd')
G.add_edge('a', 'e')
G.add_edge('c', 'f')
G.add_edge('c', 'g')
G.add_edge('c', 'h')
G.add_edge('c', 'i')

# Dibujar el gráfico
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=False)

# Mostrar el gráfico
plt.show()