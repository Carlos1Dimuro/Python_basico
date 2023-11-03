# Crear una lista de pares ordenados de números
pares_ordenados = [(1, 5), (8, 3), (12, 9), (6, 7), (15, 10), (4, 2), (11, 14), (20, 18), (25, 22), (17, 19),
                  (30, 28), (35, 33), (27, 29), (40, 37), (45, 43), (32, 34), (50, 48), (55, 53), (47, 49), (60, 58)]

# Iterar a través de los pares y calcular la diferencia
for par in pares_ordenados:
    diferencia = par[0] - par[1]
    print(f"Diferencia entre {par[0]} y {par[1]} es {diferencia}")