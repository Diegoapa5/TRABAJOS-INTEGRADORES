cant_elite_plano = 0
cont_experto = 0
total_jugadores = 0

menor_edad = 0
nombre_menor = ""
categoria_menor = ""

suma_edades_avanzado = 0
cont_avanzado = 0

plano = 0
liftado = 0
cortado = 0

seguir = "si"

while seguir == "si":

    nombre_jugador = input("Nombre: ")

    edad = int(input("Edad: "))
    while edad <= 0:
        edad = int(input("Ingrese edad nuevamente: "))

    puntos = int(input("Puntos: "))
    while puntos <= 0 or puntos > 60:
        puntos = int(input("Ingrese puntos nuevamente: "))

    partidos_ganados = int(input("Ganados: "))
    while partidos_ganados <= 0 or partidos_ganados > 35:
        partidos_ganados = int(input("Ingrese ganados nuevamente: "))

    tipo_saque = input("Saque: ")
    while tipo_saque != "plano" and tipo_saque != "liftado" and tipo_saque != "cortado":
        tipo_saque = input("Ingrese saque nuevamente: ")

    categoria = input("Categoria: ")
    while categoria != "elite" and categoria != "experto" and categoria != "avanzado":
        categoria = input("Ingrese categoria nuevamente: ")

    total_jugadores += 1

    if categoria == "elite" and tipo_saque == "plano" and edad >= 19 and edad <= 25:
        cant_elite_plano += 1

    if puntos > 50:
        if menor_edad == 0 or edad < menor_edad:
            menor_edad = edad
            nombre_menor = nombre_jugador
            categoria_menor = categoria

    if categoria == "experto":
        cont_experto += 1

    if categoria == "avanzado":
        suma_edades_avanzado += edad
        cont_avanzado += 1

    if categoria == "elite":
        if tipo_saque == "plano":
            plano += 1
        if tipo_saque == "liftado":
            liftado += 1
        if tipo_saque == "cortado":
            cortado += 1

    seguir = input("Seguir? ")

    print("Cantidad de jugadores elite con saque plano entre 19 y 25:", cant_elite_plano)

if menor_edad != 0:
    print("Jugador más joven con más de 50 puntos:", nombre_menor, "-", categoria_menor)

if total_jugadores > 0:
    print("Porcentaje de expertos:", cont_experto * 100 / total_jugadores, "%")

if cont_avanzado > 0:
    print("Promedio de edad de avanzados:", suma_edades_avanzado / cont_avanzado)

if plano > liftado and plano > cortado:
    print("El saque más usado en elite es plano")
elif liftado > plano and liftado > cortado:
    print("El saque más usado en elite es liftado")
else:
    print("El saque más usado en elite es cortado")
