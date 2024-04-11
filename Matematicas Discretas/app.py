# Jorge Parra y Jose Holguin - ITIT

def and_gate(a, b):
    return a and b

def or_gate(a, b):
    return a or b

def not_gate(a):
    return not a

def main():
    while True:
        print("\n1. AND Gate")
        print("2. OR Gate")
        print("3. NOT Gate")
        print("4. Salir")

        choice = int(input("Elige una opción: "))

        if choice == 1:
            print("AND Gate:")
            print(and_gate(True, True))  # Devuelve True
            print(and_gate(True, False))  # Devuelve False
            print(and_gate(False, True))  # Devuelve False
            print(and_gate(False, False))  # Devuelve False

        elif choice == 2:
            print("OR Gate:")
            print(or_gate(True, True))  # Devuelve True
            print(or_gate(True, False))  # Devuelve True
            print(or_gate(False, True))  # Devuelve True
            print(or_gate(False, False))  # Devuelve False

        elif choice == 3:
            print("NOT Gate:")
            print(not_gate(True))  # Devuelve False
            print(not_gate(False))  # Devuelve True

        elif choice == 4:
            break
        
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()