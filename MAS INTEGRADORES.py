
##################### EJERCICIO 1  REGISTRO DE INTERNACIONES HOSPITAL ####################

total_bruto = 0
total_final = 0

tipo_urgencia = 0
tipo_control = 0
tipo_cirugia = 0

dias_urgencia = 0
dias_control = 0
dias_cirugia = 0
pago_efectivo = 0
pago_tarjeta = 0
pago_transferencia = 0

nombre_mayor = ""
costo_mayor = 0

mas_10_dias = 0
cantidad_pacientes = 0

seguir = "si"

while seguir == "si":

    nombre = input("Ingrese nombre paciente: ")

    tipo = input("Ingrese tipo (urgencia, control, cirugia): ")
    while tipo != "urgencia" and tipo != "control" and tipo != "cirugia":
        tipo = input("Ingrese nuevamente tipo: ")

    dias = int(input("Ingrese dias internado: "))
    while dias < 1 or dias > 60:
        dias = int(input("Ingrese nuevamente dias: "))

    costo_dia = float(input("Ingrese costo por dia: "))
    while costo_dia <= 0:
        costo_dia = float(input("Ingrese nuevamente costo: "))

    edad = int(input("Ingrese edad: "))
    while edad < 0 or edad > 120:
        edad = int(input("Ingrese nuevamente edad: "))

    pago = input("Ingrese pago (efectivo, tarjeta, transferencia): ")
    while pago != "efectivo" and pago != "tarjeta" and pago != "transferencia":
        pago = input("Ingrese nuevamente pago: ")

    importe = dias * costo_dia

    if edad > 65:
        importe = importe - (importe * 20 / 100)

    if dias > 15:
        importe = importe + (importe * 10 / 100)

    if tipo == "cirugia":
        importe = importe + (importe * 25 / 100)

    total_bruto += dias * costo_dia
    total_final += importe
    cantidad_pacientes += 1

    if tipo == "urgencia":
        tipo_urgencia += 1
        dias_urgencia += dias
    elif tipo == "control":
        tipo_control += 1
        dias_control += dias
    else:
        tipo_cirugia += 1
        dias_cirugia += dias

    if pago == "efectivo":
        pago_efectivo += 1
    elif pago == "tarjeta":
        pago_tarjeta += 1
    else:
        pago_transferencia += 1

    if dias > 10:
        mas_10_dias += 1

    if importe > costo_mayor:
        costo_mayor = importe
        nombre_mayor = nombre

seguir = input("Desea ingresar otro paciente (si, no): ")

promedio = total_final / cantidad_pacientes

if tipo_urgencia > tipo_control and tipo_urgencia > tipo_cirugia:
    tipo_mas = "urgencia"
elif tipo_control > tipo_urgencia and tipo_control > tipo_cirugia:
    tipo_mas = "control"
else:
    tipo_mas = "cirugia"

if dias_urgencia > dias_control and dias_urgencia > dias_cirugia:
    dias_mas = "urgencia"
elif dias_control > dias_urgencia and dias_control > dias_cirugia:
    dias_mas = "control"
else:
    dias_mas = "cirugia"

if pago_efectivo > pago_tarjeta and pago_efectivo > pago_transferencia:
    pago_mas = "efectivo"
elif pago_tarjeta > pago_efectivo and pago_tarjeta > pago_transferencia:
    pago_mas = "tarjeta"
else:
    pago_mas = "transferencia"

print("total bruto:", total_bruto)
print("total final:", total_final)
print("pacientes urgencia:", tipo_urgencia)
print("pacientes control:", tipo_control)
print("pacientes cirugia:", tipo_cirugia)
print("tipo con mas pacientes:", tipo_mas)
print("tipo con mas dias:", dias_mas)
print("paciente mayor costo:", nombre_mayor, costo_mayor)
print("promedio costo:", promedio)
print("forma de pago mas usada:", pago_mas)
print("pacientes mas de 10 dias:", mas_10_dias)



#################### EJERCICIO 2  REGISTRO ALQUILER VEHICULOS ####################


total_bruto = 0
total_final = 0

alquiler_moto = 0
alquiler_auto = 0
alquiler_camioneta = 0

cliente_mas_dias = ""
max_dias = 0

total_kilometros = 0
cantidad_alquileres = 0

kilometro_moto = 0
kilometro_auto = 0
kilometro_camioneta = 0
pago_tarjeta = 0
alquiler_mayor = 0
cliente_mayor = ""

seguir = "si"

while seguir == "si":

    nombre_cliente = input("Ingrese nombre cliente: ")

    tipo_vehiculo = input("Ingrese tipo vehiculo (moto, auto, camioneta): ")
    while tipo_vehiculo != "moto" and tipo_vehiculo != "auto" and tipo_vehiculo != "camioneta":
        tipo_vehiculo = input("Ingrese nuevamente tipo: ")

    dias_alquiler = int(input("Ingrese dias alquiler: "))
    while dias_alquiler < 1 or dias_alquiler > 30:
        dias_alquiler = int(input("Ingrese nuevamente dias: "))

    precio_por_dia = float(input("Ingrese precio por dia: "))
    while precio_por_dia <= 0:
        precio_por_dia = float(input("Ingrese nuevamente precio: "))

    kilometros = int(input("Ingrese kilometros recorridos: "))
    while kilometros < 0 or kilometros > 5000:
        kilometros = int(input("Ingrese nuevamente kilometros: "))

    formadepago = input("Ingrese pago (efectivo, tarjeta, transferencia): ")

    cliente_frecuente = input("Cliente frecuente (SI, NO): ")

    importe = dias_alquiler * precio_por_dia

    if cliente_frecuente == "SI":
        importe = importe - (importe * 15 / 100)

    if tipo_vehiculo == "camioneta":
        importe = importe + (importe * 20 / 100)

    total_kilometros += kilometros

    if total_kilometros > 20000:
        importe = importe + (importe * 10 / 100)

    total_bruto += dias_alquiler * precio_por_dia
    total_final += importe

    if tipo_vehiculo == "moto":
        alquiler_moto += 1
        kilometro_moto += kilometros
    elif tipo_vehiculo == "auto":
        alquiler_auto += 1
        kilometro_auto += kilometros
    else:
        alquiler_camioneta += 1
        kilometro_camioneta += kilometros

    cantidad_alquileres += 1

    if dias_alquiler > max_dias:
        max_dias = dias_alquiler
        cliente_mas_dias = nombre_cliente

    if formadepago == "tarjeta":
        pago_tarjeta += 1

    if importe > alquiler_mayor:
        alquiler_mayor = importe
        cliente_mayor = nombre_cliente

    seguir = input("Desea ingresar otro alquiler (si, no): ")

promedio = total_kilometros / cantidad_alquileres

if alquiler_moto > alquiler_auto and alquiler_moto > alquiler_camioneta:
    tipo_mas_alquilado = "moto"
elif alquiler_auto > alquiler_moto and alquiler_auto > alquiler_camioneta:
    tipo_mas_alquilado = "auto"
else:
    tipo_mas_alquilado = "camioneta"

if kilometro_moto > kilometro_auto and kilometro_moto > kilometro_camioneta:
    tipo_mas_km = "moto"
elif kilometro_auto > kilometro_moto and kilometro_auto > kilometro_camioneta:
    tipo_mas_km = "auto"
else:
    tipo_mas_km = "camioneta"

print("total bruto:", total_bruto)
print("total final:", total_final)
print("tipo mas alquilado:", tipo_mas_alquilado)
print("cliente con mas dias:", cliente_mas_dias)
print("promedio kilometros:", promedio)
print("tipo con mas kilometros:", tipo_mas_km)
print("pagos con tarjeta:", pago_tarjeta)
print("mayor alquiler:", cliente_mayor, alquiler_mayor)



#################### EJERCICIO 3  REGISTRO VENTAS GIMNASIO ####################


total_bruto = 0
total_final = 0
plan_mensual = 0
plan_trimestral = 0
plan_anual = 0

turno_manana = 0
turno_tarde = 0
turno_noche = 0

pago_efectivo = 0
pago_tarjeta = 0
pago_transferencia = 0

menores_18 = 0

cliente_mayor_pago = ""
mayor_pago = 0

total_precios = 0
cantidad_ventas = 0

seguir = "si"

while seguir == "si":

    nombre_cliente = input("Ingrese nombre del cliente: ")

    tipo_plan = input("Ingrese tipo de plan (mensual, trimestral, anual): ")
    while tipo_plan != "mensual" and tipo_plan != "trimestral" and tipo_plan != "anual":
        tipo_plan = input("Ingrese nuevamente tipo de plan: ")

    edad = int(input("Ingrese edad: "))
    while edad < 12 or edad > 80:
        edad = int(input("Ingrese nuevamente edad: "))

    precio = float(input("Ingrese precio del plan: "))
    while precio <= 0:
        precio = float(input("Ingrese nuevamente precio: "))

    formadepago = input("Ingrese forma de pago (efectivo, tarjeta, transferencia): ")

    turno = input("Ingrese turno (mañana, tarde, noche): ")

    alumno_nuevo = input("Es alumno nuevo (si, no): ")

    importe = precio

    if alumno_nuevo == "si":
        importe = importe - (importe * 10 / 100)

    if tipo_plan == "anual":
        importe = importe + (importe * 15 / 100)

    cantidad_ventas += 1

    if cantidad_ventas > 50:
        importe = importe - (importe * 5 / 100)

    total_bruto += precio
    total_final += importe
    total_precios += precio

    if tipo_plan == "mensual":
        plan_mensual += 1
    elif tipo_plan == "trimestral":
        plan_trimestral += 1
    else:
        plan_anual += 1

    if turno == "mañana":
        turno_manana += 1
    elif turno == "tarde":
        turno_tarde += 1
    else:
        turno_noche += 1

    if formadepago == "efectivo":
        pago_efectivo += 1
    elif formadepago == "tarjeta":
        pago_tarjeta += 1
    else:
        pago_transferencia += 1

    if edad < 18:
        menores_18 += 1

    if importe > mayor_pago:
        mayor_pago = importe
        cliente_mayor_pago = nombre_cliente

    seguir = input("Desea ingresar otra venta (si, no): ")

promedio = total_precios / cantidad_ventas

if plan_mensual > plan_trimestral and plan_mensual > plan_anual:
    tipo_mas_vendido = "mensual"
elif plan_trimestral > plan_mensual and plan_trimestral > plan_anual:
    tipo_mas_vendido = "trimestral"
else:
    tipo_mas_vendido = "anual"

if turno_manana > turno_tarde and turno_manana > turno_noche:
    turno_mas_clientes = "mañana"
elif turno_tarde > turno_manana and turno_tarde > turno_noche:
    turno_mas_clientes = "tarde"
else:
    turno_mas_clientes = "noche"

if pago_efectivo > pago_tarjeta and pago_efectivo > pago_transferencia:
    pago_mas_usado = "efectivo"
elif pago_tarjeta > pago_efectivo and pago_tarjeta > pago_transferencia:
    pago_mas_usado = "tarjeta"
    else:
    pago_mas_usado = "transferencia"

print("total bruto:", total_bruto)
print("total final:", total_final)
print("ventas por tipo de plan:")
print("mensual:", plan_mensual)
print("trimestral:", plan_trimestral)
print("anual:", plan_anual)
print("turno con mas clientes:", turno_mas_clientes)
print("cliente que pago el plan mas caro:", cliente_mayor_pago, mayor_pago)
print("promedio precios:", promedio)
print("forma de pago mas usada:", pago_mas_usado)
print("clientes menores de 18:", menores_18)