cont1 = 0
cont2 = 0
total = 0

mayor = 0
nombre_mayor = ""
tecno_mayor = ""

for i in range(10):

    nombre = input("Nombre: ")

    edad = int(input("Edad: "))
    while edad < 18:
        edad = int(input("Edad otra vez: "))

    tecnologia = input("Tecnologia: ")
    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        tecnologia = input("Tecnologia otra vez: ")

    genero = input("Genero: ")
    while genero != "m" and genero != "f" and genero != "otro":
        genero = input("Genero otra vez: ")

    total += 1

    if genero == "m" and (tecnologia == "IA" or tecnologia == "IOT") and edad >= 25 and edad <= 50:
        cont1 += 1

    if tecnologia == "IA" and (genero != "f" or (edad >= 33 and edad <= 40)):
        cont2 += 1

    if genero == "m" and edad > mayor:
        mayor = edad
        nombre_mayor = nombre
        tecno_mayor = tecnologia

print("Punto 1:", cont1)

if mayor > 0:
    print("Mayor masculino:", nombre_mayor, tecno_mayor)

if total > 0:
    porcentaje = cont2 * 100 / total
    print("Punto 2:", porcentaje, "%")
