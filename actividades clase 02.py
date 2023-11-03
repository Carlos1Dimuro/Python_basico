#primer ejercicio. area de un triangulo
print('primer ejercicio')
base= int(input('ingrese un numero para definir la base: '))
altura=base**2
resultado=(base*altura)/2
print('el area del triangulo es: ',resultado)
print("\n")
print("\n")
#segundo ejercicio. calculo del tiempo
print('segundo ejercicio')
distancia=800
velprom=122
print('la duracion del viaje es: {:.2f}'.format(distancia/velprom))
print("\n")
print("\n")
#tercer ejercicio. suma de cuadrados y promedio de sus cubos
print('tercer ejercicio')
a=2 
b=5
print('la suma de los cuadrados es: ',a*2+b*2)
print('el promedio del cubo es: ',(a*3+b*3)/2)
print("\n")
print("\n")
#cuarto ejercicio. calcular precio de venta de un articulo
print('cuarto ejercicio')
precio_lista = float(input("ingrese el precio de lista del articulo: "))
precio_contado = precio_lista * 0.95
precio_venta_tarjeta = precio_lista * 1.10
print(f"precio de contado: {precio_contado}")
print(f"precio de venta con tarjeta: {precio_venta_tarjeta}")
print("\n")
print("\n")
#quinto ejercicio. farmacia
print('quinto ejercicio')
precio_medicamento = float(input("ingresar el precio del medicamento: "))
descuento = precio_medicamento * 0.05
monto_final = precio_medicamento - descuento
print(f"precio del medicamento: {precio_medicamento}")
print(f"descuento (5%): {descuento}")
print(f"monto final a pagar: {monto_final}")
#fin
print("\n")
print("\n")
print('terminamos de realizar los ejercicios ✓ de la clase 02')