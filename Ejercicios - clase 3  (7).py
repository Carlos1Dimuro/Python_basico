#Septimo. Inicializar una lista para almacenar los números
numeros = []

# Inicializar una variable para contar cuántos números son mayores que 100
contador_mayores_100 = 0

# Leer números hasta que se ingrese un valor negativo o se alcance el límite de veinte elementos
for i in range(20):
    numero = int(input("Ingrese un número (o un número negativo para detener): "))
    if numero < 0:
        break  # Detener el proceso si se ingresa un número negativo
    numeros.append(numero)
    if numero > 100:
        contador_mayores_100 += 1

# Mostrar cuántos números son mayores que 100
print(f"De los números ingresados, {contador_mayores_100} son mayores que 100.")