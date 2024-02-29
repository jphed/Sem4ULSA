'''
parcial 1 - Jorge Parra Hidalgo - ITIT - matricula: 13104

La expansion de la serie de maclaurin para cos(x) se define como: (-1)**n/(2n+1)! * x**(2n+1)

paso 1: comenzando con la version mas simple, sen(x) = x, agruegue terminos uno a la vez para estimar el valor de sen(pi/5) 
considerando 4 cifras significativas.

paso 2: despues de agregar cada nuevo termino, calcule los errores porcentuales relativos verdaderos y aproximados.

ejercicio 2:halle una aproximacion de la raiz f(x) = 3x**3 - 2x**2 - 8 = 0 consideranco 3 cifras significativas.
por medio del metodo  de aproximaciones sucesivas
graficamente por medio del metodo del intervalo medio, identifique la raiz  senanela.

'''
print(f"PRIMER PROBLEMA -----------------------------------------")
print("")

import math

# Paso 1
valor_verdadero = math.sin(math.pi/5)
suma = 0
x = math.pi/5
ea = 0
cifras = 4 #numero de cifras significativas
es = 0.5*10**(2-cifras) #tolerancia
prev_suma = 0
et = 0 #error_relativo_porcentual_verdadero

for n in range(100):
    # Calcular el término
    termino = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    
    # Agregar el término a la suma
    suma += termino
    
    # Paso 2
    # Calcular los errores porcentuales relativos verdaderos y aproximados
    if suma != 0:
        ea = ((suma - prev_suma) / suma) * 100
    et = ((valor_verdadero - suma) / valor_verdadero) * 100
    
    print(f"Iteracion = {n}, x = {suma:.4f}, ea = {ea:.4f}%  et = {et:.4f}%")
    
    prev_suma = suma

    # Verificar si la suma tiene 4 cifras significativas
    if abs(ea) < es:
        break

print("")

print("SEGUNDO PROBLEMA -----------------------------------------")
print("")
import matplotlib.pyplot as plt
import numpy as np
import math

# Definir la función
def f(x):
    return 3*x**3 - 2*x + 8

# Imprimir la función para diferentes valores de x
for x in range(-3, 4):
    print(f"Para x={x}, la funcion es: {f(x)}")

xsub0 = 0
error_aproximado = 0
n = 4 #numero de cifras significativas
es = 0.5*10**(2-n) #tolerancia
previous_xsub0 = 0
valor_verdadero = 1.3376 # raíz aproximada obtenida de la gráfica
et = 0 #error_relativo_porcentual_verdadero

for i in range(30):
    xsub0 = (3*xsub0**3+8)/2
    if abs(xsub0) > 1e100:  # or some other large number
        print("...")
        break
    if xsub0 != 0:
        error_aproximado = (xsub0 - previous_xsub0)/xsub0 * 100
    et = (valor_verdadero - xsub0)/valor_verdadero
    print(f"iteracion = {i}, x = {xsub0:.5f}, ea = {error_aproximado:.5f},  et = {et:.5f}")
    previous_xsub0 = xsub0

# Graficar la función
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect

# Define the function
def f(x):
    return 3*x**3 - 2*x + 8

# Define the bisection method
def bisection(a, b, tol):
    if f(a)*f(b) > 0:
        print("No hay raíz en el intervalo dado.")
        return None
    else:
        while (b - a) / 2.0 > tol:
            midpoint = (a + b) / 2.0
            if f(midpoint) == 0:
                return(midpoint) 
            elif f(a)*f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
        return (a + b) / 2.0

# Choose the interval [a, b]
a = -10
b = 10

# Apply the bisection method
root = bisection(a, b, tol=1e-5)

# Plot the function and mark the root
x = np.linspace(a, b, 400)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x)=3x^3 - 2x + 8')
plt.plot(root, f(root), 'ro', label=f'Root = {root:.5f}')
plt.title('Plot of the function f(x)=3x^3 - 2x + 8')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black',linewidth=0.6)
plt.axvline(0, color='black',linewidth=0.6)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()

print("")
print("-----------------------------------------")

# graficar por medio del metodo del intervalo medio, identificar raiz y senalar de f()