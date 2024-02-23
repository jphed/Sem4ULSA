import math
import matplotlib.pyplot as plt
import numpy as np

for x in range(-5,10):

    if x >= 0:
        funcion = math.sin(math.sqrt(x)) - x
        print(f"iteracion = {x}, f(x) = {funcion:.5f}")
    else:
        print(f"iteracion = {x}, f(x) = no existe")


# Crear un array de valores x
x = np.arange(-5, 10, 0.1)

# Calcular los valores y correspondientes
y = np.empty_like(x)
for i, xi in np.ndenumerate(x):
    if xi >= 0:
        y[i] = math.sin(math.sqrt(xi)) - xi
    else:
        y[i] = np.nan  # Usamos NaN para valores no definidos

# Crear la gráfica
plt.figure()
plt.plot(x, y, label='y=sin(sqrt(x)) - x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de y=sin(sqrt(x)) - x')
plt.legend()
plt.grid(True)
plt.show()

print("-----------------------------------------")

xsub0 = 0.5
es = 0.01
ea = 0
previous_xsub0 = 0

for i in range(1, 100):
    xsub0 = math.sin(math.sqrt(xsub0))
    ea = (xsub0 - previous_xsub0)/xsub0 * 100
    print(f"iteracion = {i}, x0 = {xsub0:.1f}, ea = {ea:.2f}")
    previous_xsub0 = xsub0
    xsub0 += 0.5

    if abs(ea) <= 0.01:
        break