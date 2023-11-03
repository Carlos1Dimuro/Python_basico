# Segundo ejercicio. Solicitar al usuario que ingrese tres temperaturas
temperatura1 = float(input("Ingrese la temperatura 1: "))  # Solicita la primera temperatura
temperatura2 = float(input("Ingrese la temperatura 2: "))  # Solicita la segunda temperatura
temperatura3 = float(input("Ingrese la temperatura 3: "))  # Solicita la tercera temperatura

promedio = (temperatura1 + temperatura2 + temperatura3) / 3  # Calcula el promedio de las temperaturas
mayor_que_promedio = False

# Comprueba si alguna temperatura es mayor que el promedio
if temperatura1 > promedio:
    mayor_que_promedio = True
if temperatura2 > promedio:
    mayor_que_promedio = True
if temperatura3 > promedio:
    mayor_que_promedio = True

# Muestra el promedio y si alguna temperatura es mayor que el promedio
print("El promedio de las temperaturas es:", promedio)
if mayor_que_promedio:
    print("Al menos una de las temperaturas es mayor que el promedio.")
else:
    print("Ninguna de las temperaturas es mayor que el promedio.")