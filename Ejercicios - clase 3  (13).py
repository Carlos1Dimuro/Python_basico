# Inicializamos las variables
total_ventas = 0
importe_total_ventas = 0
ventas_entre_100_y_300 = 0
ventas_inferiores_a_50 = False

# Solicitamos al usuario la cantidad de ventas a ingresar
n = int(input("Ingrese la cantidad de ventas a registrar: "))

for i in range(n):
    codigo_producto = input(f"Ingrese el código del producto para la venta {i+1}: ")
    cantidad_vendida = int(input(f"Ingrese la cantidad vendida para el producto {codigo_producto}: "))
    precio_unitario = float(input(f"Ingrese el precio unitario para el producto {codigo_producto}: "))
    
    importe_venta = cantidad_vendida * precio_unitario
    total_ventas += 1
    importe_total_ventas += importe_venta
    
    if 100 <= cantidad_vendida <= 300:
        ventas_entre_100_y_300 += 1
    
    if cantidad_vendida < 50:
        ventas_inferiores_a_50 = True

print(f"Cantidad de ventas ingresadas: {total_ventas}")
print(f"Importe total de ventas: ${importe_total_ventas}")
print(f"Cantidad de ventas entre 100 y 300 unidades: {ventas_entre_100_y_300}")
if ventas_inferiores_a_50:
    print("Hubo ventas con una cantidad inferior a 50 unidades.")