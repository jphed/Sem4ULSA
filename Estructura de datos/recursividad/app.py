#Jorge Parra Hidalgo ITIT 13104

def suma(n):
    if n == 0:
        return 0
    else:
        return n + suma(n-1)

def print_numeros(n):
    if n > 0:
        print_numeros(n-1)
        print(n)

def print_numeros_inverso(n):
    if n > 0:
        print(n)
        print_numeros_inverso(n-1)

def num_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + num_digitos(n // 10)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def potencia(base, n):
    if n == 0:
        return 1
    else:
        return base * potencia(base, n-1)

def is_ordenado(palabra):
    if len(palabra) < 2:
        return True
    else:
        return palabra[0] <= palabra[1] and is_ordenado(palabra[1:])

def palindromo(palabra):
    if len(palabra) < 2:
        return True
    else:
        return palabra[0] == palabra[-1] and palindromo(palabra[1:-1])

def binario(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * binario(n // 2)

def is_binario(n):
    if n == 0:
        return True
    elif n % 10 > 1:
        return False
    else:
        return is_binario(n // 10)

def main():
    while True:
        print("\n1. Suma de 1 a N")
        print("2. Mostrar números de 1 a N")
        print("3. Mostrar números de N a 1")
        print("4. Número de dígitos de un número")
        print("5. Factorial de un número")
        print("6. Potencia de un número")
        print("7. Verificar si una palabra está ordenada alfabéticamente")
        print("8. Verificar si una palabra es un palíndromo")
        print("9. Convertir un número a binario")
        print("10. Verificar si un número es binario")
        print("0. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 0:
            break
        elif opcion == 1:
            n = int(input("Ingrese N: "))
            print(suma(n))
        elif opcion == 2:
            n = int(input("Ingrese N: "))
            print_numeros(n)
        elif opcion == 3:
            n = int(input("Ingrese N: "))
            print_numeros_inverso(n)
        elif opcion == 4:
            n = int(input("Ingrese un número: "))
            print(num_digitos(n))
        elif opcion == 5:
            n = int(input("Ingrese un número: "))
            print(factorial(n))
        elif opcion == 6:
            base = int(input("Ingrese la base: "))
            n = int(input("Ingrese la potencia: "))
            print(potencia(base, n))
        elif opcion == 7:
            palabra = input("Ingrese una palabra: ")
            print(is_ordenado(palabra))
        elif opcion == 8:
            palabra = input("Ingrese una palabra: ")
            print(palindromo(palabra))
        elif opcion == 9:
            n = int(input("Ingrese un número: "))
            print(binario(n))
        elif opcion == 10:
            n = int(input("Ingrese un número: "))
            print(is_binario(n))

if __name__ == "__main__":
    main()