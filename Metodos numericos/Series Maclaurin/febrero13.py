'''
Estimación de errores
La expansión en serie de Maclaurin para cos x es:

cos x = 1 - x^2/2! + x^4/4! - x^6/6! + ...

Iniciando con el primer térmico cos x =1, agregue los términos uno a
uno para estimar cos (1/3). Después de que agregue cada uno de los
términos, calcule los errores relativos porcentuales verdaderos y
aproximados. Agregue términos hasta que el valor absoluto del error
aproximado se encuentre dentro de cierto criterio de error,
considerando dos cifras significativas.
'''

import math

true_value = math.cos(1/3) #valor verdadero
iterations = 5 #numero de iteraciones
x = 1/3 #valor de x
Es = 0.5 * 10**(2-9) #tolerancia
aprox = 0
true_error = 0
relative_error_per = 0
true_relative_error_per = 0
previous_aprox = 0

print("{:<12} {:<15} {:<10} {:<16} {:<6} {:<6}".format('iteraciones', 'valor termino', 'aprox', 'error verdadero', 'et', 'ea'))

for i in range(iterations+1 ):
    value_per_term = ((-1)**i) * (x**(2*i)) / math.factorial(2*i)
    aprox += value_per_term
    if previous_aprox == 0:
        true_relative_error_per = 0
    else:
        true_relative_error_per = ((aprox - previous_aprox)/aprox) * 100

    previous_aprox = aprox
    true_error = abs(true_value - aprox)
    relative_error_per = (true_error / true_value) * 100
    
    #resultados
    print("{:<12} {:<15.9f} {:<10.9f} {:<16.9f} {:<6.2f}% {:<6.4f}%".format(i, value_per_term, aprox, true_error, relative_error_per, true_relative_error_per))