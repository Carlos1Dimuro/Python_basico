#Sexto ejercicio. Inicializar una variable para contar cuántos números son mayores que 100
contador_mayores_100 = 0

# Leer cincuenta números enteros
for i in range(50):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    if numero > 100:
        contador_mayores_100 += 1

# Mostrar cuántos números son mayores que 100
print(f"De los cincuenta números ingresados, {contador_mayores_100} son mayores que 100.")