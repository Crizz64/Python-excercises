#tipos de datos

seats= 500 # número inicial de asientos
while seats > 0: # ¿hay asientos disponibles?
  print("Sell ticket") # boleto vendido
  seats -= 1 # número de asientos actualizado


#ejercicio 1

# Toma el número como entrada
number = int(input())

while number >= 0:
    print(number)
    number -= 1
# Usa un bucle while para la cuenta regresiva


#ejercicio 1 parte 2


contador = 0

while True:
    numero = (input("ingrese un entero para terminar"))

    if numero:
        contador = contador + int(numero)
        
else:
    print(f"sumatoria terminada, el resultado es : {contador}")
    condicion = False



    
#ejercicio 2

for i in range(1,100):
    if i %3 == 0:
        print("el número es " ,i)

    elif i == [15,30,45,60,75,90]:
        print("estos números no son divisibles con 5 ", i)
            
  
            
#Ejercicio #3

i = 1 #Variable de control
while i <= 3:    #la condición también podría hacerlo infinito
    print(i)
    i += 1 #contador, debe existir el contador para que no sea infinito
print("programa terminado")



#ejercicio #4

i = 1
while i <= 50:
    print(i)
    i = 3* + 1
print("el programa termino")


#ejercicio #5

numero = int(input("Escriba un número positivo"))
while numero < 0:
    print("¡Ha escrito un número negativo! inténtelo de nuevo")
    numero = int(input("Escriba un número positivo"))
print("Gracias por su colabración")


#ejercicio 6

x = input("Escriba si o no?").lower()
while x == 'si':
    print("respuesta incorrecta")
    x = input("Escriba si o no")
print("El programa a terminado")

#ejercicio 7

print("Diga Si para continuar")
respuesta = input("Desea continuar el programa?: ")

while respuesta == 'si':
    respuesta = input("¿Desea continuar el programa?")

print("El programa terminó")


#ejercicio 8

print("Diga Si para continuar")
respuesta = input("Desea continuar el programa?: ")

while respuesta == 'S' or respuesta == 'si':
    respuesta = input("¿Desea continuar el programa?")

print("El programa terminó")