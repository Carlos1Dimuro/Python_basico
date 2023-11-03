n = int(input("Ingresa la cantidad de elementos en la serie: "))

for i in range(n):
    numero = float(input(f"Ingrese el número {i+1}: "))
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}")