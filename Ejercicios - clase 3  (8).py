#Octavo. Inicializar variables para almacenar las sumas de X y Y
suma_x = 0
suma_y = 0

# Leer los diez pares ordenados (X, Y)
for i in range(10):
    x = float(input(f"Ingrese el valor de X para el par {i + 1}: "))
    y = float(input(f"Ingrese el valor de Y para el par {i + 1}: "))
    
    # Sumar X e Y a las variables de suma
    suma_x += x
    suma_y += y

# Mostrar la suma de todas las X y la suma de todas las Y
print(f"La suma de todas las X es: {suma_x}")
print(f"La suma de todas las Y es: {suma_y}")