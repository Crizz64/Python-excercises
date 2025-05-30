# Bucle For

print("Comienzo")
for i in [0, 1, 2]:
    print("Hola ", end="") #End evita los saltos de linea e imprime horizontalmente
print("")  #esto genera un br o salto de linea
print("Final")


#Ejercicio 2

words = ['cat', 'window', 'defenestrate']

for w in words:

    print(w, len(w))
    
    
# Ejercicio 3
print("Comienzo")

for i in range(1000): #range "Permite elegir el rango de veces a recorrer"
    print(f"Hola {i}",)
print()
print("Final")

#Ejercicio 4
veces = int(input("¿Cuantas veces quiere que le salude?"))

for i in range(veces):
    print(f"Hola {i}")
print()
print("Adiós")            


#ejercicio 5

print("Mayores que el primero")
valores = int(input("¿Cuantos valores va a introducir?"))
if valores < 1:
    print("¡Imposibke!")
else:
    primero = int(input("Escribir un número: "))
    for i in range (valores - 1):
        numero = int(input(f"Escriba un número más grande que {primero}: "))
        if numero <= primero:
            print(f"!{numero} no es mayor que {primero}!")
    print("Gracias por su colaboración")



#ejercicio 6

nums = []

for x in range(1,51):
  nums.append(x)

print(nums)