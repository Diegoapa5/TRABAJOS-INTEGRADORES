#Estructura FOR Actividades

#Ejercicio 1
for i in range (1, 11):
    print (i)



#Ejercicio 2
for i in range (10, 0, -1 ):
    print (i)



#Ejercicio 3
numero = int(input("Ingrese un numero: "))
for i in range(0, numero +1):
    print (i)



#Ejercicio 4
numero = int(input("Ingrese un numero: "))
for i in range(0, 11, ):
    print(numero, "x", i, "=", numero * i)



#Ejercicio 5
suma = 0
contador = 0

while contador < 10:
    numero = float(input("Ingrese los numeros: "))

    if numero == 0:
        break

    suma = suma + numero
    contador = contador + 1

if contador > 0:
    promedio = suma / contador
    print("Su promedio es: ", promedio)



#Ejercicio 6
for i in range(3, 11, 3):
    print(i)



#Ejercicio 7
for i in range (2, 51 , 2):
    print (i)



#Ejercicio 8
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()



#Ejercicio 9
contador = 0

numero = int(input("Ingrese un numero: "))

for i in range(1, numero+1):
    if numero % i == 0:
        print (i)
        contador = contador + 1
print("La cantidad de divisores encontrados es:", contador)



#Ejercicio 10
contador = 0

numero = int(input("Ingrese un numero: "))

for i in range(1, numero+1):
    if numero % i == 0:
        contador = contador + 1

if contador == 2:
    print("Es un numero primo: ")
else:
    print("No es un nummero primo: ")



#Ejercicio 11
primos_encontrados = 0

numero = int(input("Ingrese un numero: "))

for i in range(1, numero+1):
    contador = 0

for j in range(1, i+1):
        if i % j == 0:
            contador = contador + 1

if contador == 2:
        print(i)
        primos_encontrados = primos_encontrados + 1

print("La cantidad de primos es:", primos_encontrados)
