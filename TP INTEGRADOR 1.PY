total_bruto = 0
importe_final = 0
total_unidades = 0
venta_mas_cara_tarjeta = 0
suma_precios = 0

efectivo = 0
tarjeta = 0
transferencia = 0

for i in range(25):

    producto = input("Ingrese el tipo de producto (alimento, limpieza, perfumeria): ")
    while producto != "alimento" and producto != "limpieza" and producto != "perfumeria":
        producto = input("Ingrese el producto nuevamente: ")

    unidadesvendidas = int(input("Ingrese las unidades vendidas (entre 1 y 20): "))
    while unidadesvendidas < 1 or unidadesvendidas > 20:
        unidadesvendidas = int(input("Ingrese nuevamente las unidades: "))

    preciounitario = float(input("Ingrese el valor unitario: "))
    while preciounitario <= 0:
        preciounitario = float(input("Ingrese el valor nuevamente: "))

    formadepago = input("Ingrese la forma de pago (efectivo, tarjeta, transferencia): ")
    while formadepago != "efectivo" and formadepago != "tarjeta" and formadepago != "transferencia":
        formadepago = input("Ingrese la forma de pago nuevamente: ")

    subtotal = unidadesvendidas * preciounitario

    total_bruto = total_bruto + subtotal
    total_unidades = total_unidades + unidadesvendidas
    suma_precios = suma_precios + preciounitario


    if formadepago == "efectivo":
        subtotal = subtotal - (subtotal * 0.05)

    importe_final = importe_final + subtotal

    if formadepago == "efectivo":
        efectivo = efectivo + 1
    elif formadepago == "tarjeta":
        tarjeta = tarjeta + 1
    elif formadepago == "transferencia":
        transferencia = transferencia + 1

    if formadepago == "tarjeta":
        if subtotal > venta_mas_cara_tarjeta:
            venta_mas_cara_tarjeta = subtotal

    if efectivo >= tarjeta and efectivo >= transferencia:
        mas_usada = "efectivo"
    elif tarjeta >= efectivo and tarjeta >= transferencia:
        mas_usada = "tarjeta"
    else:
        mas_usada = "transferencia"

    print("La forma de pago más usada fue:", mas_usada)

    promedio = suma_precios / 25

    if total_unidades > 400:
        importe_final = importe_final - (importe_final * 0.20)
    elif total_unidades > 200:
        importe_final = importe_final - (importe_final * 0.10)

print("Total bruto:", total_bruto)
print("Importe final con descuentos:", importe_final)
print("Promedio de precios:", promedio)
print("Venta más cara con tarjeta:", venta_mas_cara_tarjeta)
print("Forma de pago más usada:", mas_usada)
        




   


   
