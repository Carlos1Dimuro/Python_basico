#Quinto ejercicio. Solicitar al usuario que ingrese la categoría (A o B)
categoria = input("Ingrese la categoría (A o B): ")

# Validar la categoría ingresada
if categoria not in ['A', 'B']:
    print("Categoría no válida. Debe ser 'A' o 'B'.")
else:
    # Solicitar al usuario que ingrese el importe original a abonar
    importe_original = float(input("Ingrese el importe original a abonar: "))

    # Calcular el importe final a pagar según la categoría y las condiciones
    if categoria == 'A' and importe_original > 10000:
        descuento = importe_original * 0.05
    elif categoria == 'B' and 15000 <= importe_original <= 25000:
        descuento = importe_original * 0.02
    else:
        descuento = 0

    importe_final = importe_original - descuento

    # Mostrar el importe final a pagar
    print(f"Importe final a pagar: ${importe_final:.2f}")