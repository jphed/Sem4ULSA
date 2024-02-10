#Series de maclaurin por iteraciones
import math

def maclaurin(n, x):
    factorial_n = math.factorial(n)
    print(factorial_n)
    suma = 0
    for i in range(n):
        suma += (x**i) / math.factorial(i)
    return suma

n = int(input("Ingrese el número de iteraciones: "))
x = float(input("Ingrese el valor de x: "))
resultado = maclaurin(n, x)
print("El valor de e^x es: ", resultado)

