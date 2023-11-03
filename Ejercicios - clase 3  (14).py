n = int(input("Ingrese la cantidad de puntos a registrar: "))

cuadrante1 = 0  # Contador de puntos en el primer cuadrante
cuadrante3 = 0  # Contador de puntos en el tercer cuadrante

for i in range(n):
    x = float(input(f"Ingrese la coordenada x del punto {i+1}: "))
    y = float(input(f"Ingrese la coordenada y del punto {i+1}: "))
    
    if x > 0 and y > 0:
        cuadrante = 1
        cuadrante1 += 1
    elif x < 0 and y > 0:
        cuadrante = 2
    elif x < 0 and y < 0:
        cuadrante = 3
        cuadrante3 += 1
    elif x > 0 and y < 0:
        cuadrante = 4
    else:
        cuadrante = "el origen"
    
    print(f"El punto {i+1} ({x}, {y}) se encuentra en el cuadrante {cuadrante}.")

print(f"Total de puntos en el primer cuadrante: {cuadrante1}")
print(f"Total de puntos en el tercer cuadrante: {cuadrante3}")