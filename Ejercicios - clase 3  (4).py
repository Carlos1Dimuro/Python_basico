# Cuarto ejercicio. Solicitar al usuario que ingrese tres números
numero1 = float(input("Ingrese el primer número: "))  # Solicita el primer número
numero2 = float(input("Ingrese el segundo número: "))  # Solicita el segundo número
numero3 = float(input("Ingrese el tercer número: "))  # Solicita el tercer número

numeros = [numero1, numero2, numero3]  # Crea una lista con los números ingresados

# Ordena la lista de números en orden descendente (de mayor a menor)
numeros.sort(reverse=True)

# Muestra los números ordenados de mayor a menor
print("Números ordenados de mayor a menor:", numeros)