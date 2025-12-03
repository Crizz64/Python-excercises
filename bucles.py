for i in range(10): #esto es un bucle
    print(i,end=" , ") # aca se inprme en pantalla 10 veces el bucle


#ejercicio 2

limite=int(input("ingrese la cantidad de números que desea sumar: "))
x = 0
for i in range(limite):
   numero = int(input("ingrese un número: "))
   x=x+numero #variable acumuladora
print(f"la sumatoría es: {x}") 



#ejercicio

palabra = input("Ingrese una palabra: ").lower()
x=0
for i in palabra:
   if i=='a' or i=='e' or i=='i' or i=='0' or i=='u':
        x=x+1
        print(f"{palabra} tiene vocales")
else:
    print(f"{palabra} no tiene vocales")


#ejercicio 4

frase = input("ingrese una palabra: ")

for i in frase:
    if i in ('a','e','i','o', 'u'):
        print(f"{frase} continee vocales")
    else:
        print(f"{frase} No contiene vocales")


#ejercicio 5


frase = input("Ingrese una palabra: ").lower()
x = 0
for i in frase:
    if i in 'aeiou':
        x=x+1

if x > 0:
    print(f"{frase} contiene vocales")
else:
    print(f"{frase} no contiene vocales")



#ejercicio 6

age = 22
if age >= 18:
  print("Regular price")
else:
  print("Discount")


#ejercicio 7

age = 30
if age >= 18:
  print("Regular price")
else:
  print("Discount")
print("Proceed to payment")




#ejercicio 8

age = 32
is_student = True
if age < 18 or is_student:
  print("Discount")
else: 
  print("Regular price")


#ejercicio 9

age = 32
is_student = True
if age < 18 or is_student:
  print("Discount")
else: 
  print("Regular price")


  
#ejercicio 10
age = 75
if age < 18: 
  print("Junior discount")
elif age >= 75: 
  print("Senior discount")
else:
  print("No discount")
print("Proceed to payment")



#ejercicio 11

age = 16
is_student = True

if age < 18:
  #se ejecuta si la edad es menor de 18
  if is_student:
    #se ejecuta si es menor de 18 y también es estudiante
    print("20% discount")
  else:
    #se ejecuta si es menor de 18 y no es estudiante
    print("10% discount")
else:
  #se ejecuta este código si el cliente tiene 18 años o más
  print("Regular price")


#ejercicio 12
age = 29
if age < 18:
  if is_student:
    print("20% discount")
else:
  print("Regular price")
print("Proceed to payment")