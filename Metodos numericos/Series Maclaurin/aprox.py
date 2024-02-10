import math

true_value = 1.6487212707001282 #valor verdadero
iterations = 5 #numero de iteraciones
x = 0.5 #valor de x
Es = 0.5 * 10**(2-9) #tolerancia
aprox = 0
true_error = 0
relative_error_per = 0
true_relative_error_per = 0
previous_aprox = 0

for i in range(iterations):
    value_per_term = x**i / math.factorial(i)

    if previous_aprox == 0:
        true_relative_error_per = 0
    else:
        true_relative_error_per = (aprox - previous_aprox)/aprox * 100

    aprox += value_per_term
    previous_aprox = aprox

    true_error = abs(true_value - aprox)
    relative_error_per = (true_error / true_value) * 100
    
    #print the results
    print(f"{i}, {value_per_term}, {aprox}, {true_error}, {relative_error_per}%, {true_relative_error_per}%")




