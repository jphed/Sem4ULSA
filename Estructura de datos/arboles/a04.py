import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

# Crear un gráfico dirigido
G = nx.DiGraph()

# Agregar los nodos y las aristas al gráfico
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(4, 7)
G.add_edge(4, 8)
G.add_edge(3, 5)
G.add_edge(3, 6)
G.add_edge(5, 9)
G.add_edge(9, 11)
G.add_edge(6, 10)

# Dibujar el gráfico
pos = graphviz_layout(G, prog='dot')
nx.draw(G, pos, with_labels=True, arrows=False)

# Mostrar el gráfico
plt.show()