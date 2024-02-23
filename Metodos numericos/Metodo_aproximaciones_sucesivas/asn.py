#aproximacion de sucesion numerica
import math
import matplotlib.pyplot as plt
import numpy as np

for x in range(-5,6):
    funcion = (math.e**-x) - x
    print(f"Para x={x}, la funcion es: {funcion}")

print("-----------------------------------------")

xsub0 = 0
error_aproximado = 0
n = 4 #numero de cifras significativas
es = 0.5*10**(2-n) #tolerancia que dio geogebra
previous_xsub0 = 0
valor_verdadero = 0.56713549
et = 0 #error_relativo_porcentual_verdadero


for i in range(30):
    xsub0 = math.e**-xsub0
    error_aproximado = (xsub0 - previous_xsub0)/xsub0 * 100
    et = (valor_verdadero - xsub0)/valor_verdadero
    print(f"iteracion = {i}, x = {xsub0:.5f}, ea = {error_aproximado:.5f},  et = {et:.5f}")
    previous_xsub0 = xsub0

    if abs(error_aproximado) <= es:
        break

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

print("-----------------------------------------")
#convergencia
# f(x) = e^-x - x
# f(x1) = e^-x1
# f(x2) = x
x = 0;y1 = 0;y2 = 0

for i in range(1, 12):
    y1 = math.e**-x
    y2 = x

    print(f"x = {x:.1f}, y1 = {y1:.4f}, y2 = {y2:.4f}")
    x += 0.1

print("-----------------------------------------") 

# Crear un array de valores x
x = np.arange(0, 1.1, 0.1)

# Calcular los valores y correspondientes
y1 = np.exp(-x)
y2 = x

# Crear la gráfica
plt.figure()
plt.plot(x, y1, label='y=e^-x')
plt.plot(x, y2, label='y=x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de y=e^-x y y=x')
plt.legend()
plt.grid(True)
plt.show()