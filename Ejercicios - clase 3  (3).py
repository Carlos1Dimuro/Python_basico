# Tercer ejercicio. Solicitar al usuario que ingrese la edad mínima requerida para el trabajo
edad_minima = int(input("Ingrese la edad mínima requerida para el trabajo: "))

edades_postulantes = []

# Solicita al usuario que ingrese la edad de 3 postulantes
for i in range(3):
    edad = int(input(f"Ingrese la edad del postulante {i + 1}: "))
    edades_postulantes.append(edad)

# Comprueba si todos los postulantes cumplen con la edad mínima requerida
cumplen_con_edad_minima = all(edad >= edad_minima for edad in edades_postulantes)

# Muestra si todos los postulantes cumplen con la edad mínima o no
if cumplen_con_edad_minima:
    print("Todos los postulantes cumplen con la edad mínima requerida.")
else:
    print("Al menos uno de los postulantes no cumple con la edad mínima requerida.")