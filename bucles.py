for i in range(10):
    print(i,end=" , ")


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