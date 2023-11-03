# Primer ejercicio. Pedir al usuario que ingrese tres números
numero1 = float(input("Ingrese el primer número: "))  # Solicita el primer número al usuario
numero2 = float(input("Ingrese el segundo número: "))  # Solicita el segundo número al usuario
numero3 = float(input("Ingrese el tercer número: "))  # Solicita el tercer número al usuario
suma = numero1 + numero2 + numero3  # Calcula la suma de los tres números

# Verifica si la suma es mayor a 50 y aplica una operación en consecuencia
if suma > 50:
    resultado = suma / 2  # Si la suma es mayor a 50, divide por 2
else:
    resultado = suma ** 3  # Si no, eleva al cubo

# Muestra el resultado final
print("El resultado es:", resultado)