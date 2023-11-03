#Noveno. Inicializar una variable para el total de comisiones
total_comisiones = 0

while True:
    # Solicitar al usuario que ingrese la categoría del vendedor
    categoria = int(input("Ingrese la categoría del vendedor (1, 2 o 3, o 0 para salir): "))
    
    if categoria == 0:
        break  # Si se ingresa 0, salir del bucle
    
    # Solicitar al usuario que ingrese el total de la venta
    total_venta = float(input("Ingrese el total de la venta: "))
    
    # Calcular la comisión según la categoría del vendedor
    if categoria == 1:
        comision = total_venta * 0.05  # Categoría 1: 5% de comisión
    elif categoria == 2:
        comision = total_venta * 0.10  # Categoría 2: 10% de comisión
    elif categoria == 3:
        comision = total_venta * 0.15  # Categoría 3: 15% de comisión
    else:
        print("Categoría no válida. Debe ser 1, 2 o 3.")
        continue
    
    # Acumular la comisión al total de comisiones
    total_comisiones += comision

# Mostrar el total de comisiones a pagar a los vendedores
print(f"El total de comisiones a pagar a los vendedores es: ${total_comisiones:.2f}")