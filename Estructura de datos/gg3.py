import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)  # Crear un array de 100 puntos entre 0 y 10
y = np.sin(x)  # Calcular el seno de cada punto

plt.plot(x, y)  # Graficar x versus y
plt.xlabel('x')  # Etiqueta del eje x
plt.ylabel('sin(x)')  # Etiqueta del eje y
plt.title('Gráfico de Seno')  # Título del gráfico
plt.grid(True)  # Mostrar cuadrícula
plt.show()  # Mostrar el gráfico