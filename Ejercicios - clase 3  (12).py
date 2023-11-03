n = int(input("Ingrese la cantidad de números enteros a ingresar: "))
total_numeros = 0  # Inicializamos el contador de números ingresados
total_mayores_100 = 0  # Inicializamos el contador de números mayores a 100

# Inicializamos la suma de los números para calcular el promedio
suma_numeros = 0

for i in range(n):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    total_numeros += 1
    suma_numeros += numero
    
    if numero > 100:
        total_mayores_100 += 1

promedio = suma_numeros / total_numeros
porcentaje_mayores_100 = (total_mayores_100 / total_numeros) * 100

print(f"El promedio de los números ingresados es: {promedio}")
print(f"El porcentaje de números mayores a 100 es: {porcentaje_mayores_100}%")