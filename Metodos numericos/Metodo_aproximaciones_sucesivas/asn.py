#aproximacion de sucesion numerica
import math
import math
import matplotlib.pyplot as plt
import numpy as np

for x in range(-5,6):
    funcion = (math.e**-x) - x
    print(f"Para x={x}, la funcion es: {funcion}")

print("-----------------------------------------")


# Crear un array de valores x
x = np.linspace(-5, 5, 100)

# Calcular los valores y correspondientes
y = np.exp(-x) - x

# Crear la gráfica
plt.figure()
plt.plot(x, y, label='y=e^-x - x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de y=e^-x - x')
plt.legend()
plt.grid(True)
plt.show()