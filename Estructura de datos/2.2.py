import random

# Inicializar lista de artículos
nombres_articulos = ['taladro', 'desarmador', 'martillo', 'cinta canela', 'llave inglesa']
articulos = [{'id': i, 'nombre': nombres_articulos[i], 'precio': random.randint(1, 100)} for i in range(5)]

def mostrar_articulos():
    for articulo in articulos:
        print(articulo)

def ordenar_burbuja():
    n = len(articulos)
    for i in range(n):
        for j in range(0, n-i-1):
            if articulos[j]['nombre'] > articulos[j+1]['nombre']:
                articulos[j], articulos[j+1] = articulos[j+1], articulos[j]

def ordenar_articulo():
    articulos.sort(key=lambda x: x['nombre'])

def ordenar_precio():
    articulos.sort(key=lambda x: x['precio'])

def desordenar():
    random.shuffle(articulos)

def buscar_secuencial(id):
    for articulo in articulos:
        if articulo['id'] == id:
            return articulo
    return None

def buscar_binaria(id):
    izq, der = 0, len(articulos) - 1
    while izq <= der:
        mid = (izq + der) // 2
        if articulos[mid]['id'] == id:
            return articulos[mid]
        elif articulos[mid]['id'] < id:
            izq = mid + 1
        else:
            der = mid - 1
    return None

def compresion_lista(id):
    return [articulo for articulo in articulos if articulo['id'] == id]

def seleccionar_precio_mayor(x):
    return [articulo for articulo in articulos if articulo['precio'] > x]

# Menú
while True:
    print("\n1. Mostrar artículos")
    print("2. Ordenar la lista de artículos utilizando la función burbuja")
    print("3. Ordenar por artículo utilizando método sort de las listas de Python")
    print("4. Ordenar por precio utilizando método sort de las listas de Python")
    print("5. Desordenar la lista, utilizar la función random.shuffle")
    print("6. Buscar un artículo por id utilizando búsqueda secuencial")
    print("7. Buscar un artículo por id utilizando búsqueda binaria")
    print("8. Compresión de Listas")
    print("9. Seleccionar los artículos con precio mayor a x")
    print("0. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        mostrar_articulos()
    elif opcion == 2:
        ordenar_burbuja()
    elif opcion == 3:
        ordenar_articulo()
    elif opcion == 4:
        ordenar_precio()
    elif opcion == 5:
        desordenar()
    elif opcion == 6:
        id = int(input("Ingrese el id del artículo: "))
        print(buscar_secuencial(id))
    elif opcion == 7:
        id = int(input("Ingrese el id del artículo: "))
        print(buscar_binaria(id))
    elif opcion == 8:
        id = int(input("Ingrese el id del artículo: "))
        print(compresion_lista(id))
    elif opcion == 9:
        x = int(input("Ingrese el precio: "))
        print(seleccionar_precio_mayor(x))
    elif opcion == 0:
        break
    else:
        print("Opción inválida")