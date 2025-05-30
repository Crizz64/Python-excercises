# condicionales, ejercicio 1

edad = int(input("Ingrese su edad"))

if edad >= 18:
    print(f"eres mayor de edad")
else:
    print(f"eres menor de edad")


#condicionales, ejercicio 2

numero = int(input("Escriba un número positivo"))

if numero < 0:
    print("¡le he dicho que escriba un número positivo")
    print("ha escrito el número ", numero)
    
    
#condicionalles ejercico 3

print("Este programa mezcla dos colores")
print("r. Rojo   a. Azul")

primera = input("Elija un color (r o a): ")

if primera == "r":
    print("a. Azul     v. Verde")

    segunda = input("Elija otro color (a o v): ")
    
    if segunda== "a":
     print("La mezla de Rojo y Azul produce Magenta.")
    
    else:
     print("La mezcla Rojo y Verde  produce Amarillo.")
    
else:
    print(" v. Verde    r. Rojo")
    segunda = input(" Elija otro color (v o r): ")
    
    if segunda == "v":
        print("La mezcla de Azul Y Verde produce Cian.")
        
    else:
        print("La mezcla Azul y Rojo produce Magenta")
        
        
#Condicionales ejercicio 4

edad = int(input("¿Cuántos años tienes?"))

if edad < 0:
    print("No se puede tener una edad negativa")
    
elif edad < 18:
    print("Usted es menor de edad.")

else:
    print("Usted es mayor edad.")    
    

#Condicionales ejercicio 5

nombre = input("Ingrese su Nombre: ").lower()
apellido = input("Ingrese su Apellido").lower()

if nombre == "Crizz" and apellido == "Valencia":
    print(f"Hola {nombre + apellido}")
else:
    print(f"no te conozco {nombre}")
        
    
     
#condicionales prueba 1

Contraseña = "Año2024"

Password = input("Ingrese la contraseña")
if Password == Contraseña:
    print(f"Su contraseña {Password} es correcta")
else:
    print(f"Su contraseña {Password} es incorrecta")


#condicionales prueba 2

num1 = int(input("Ingrese el primer valor"))
num2 = int(input("Ingrese el segundo Valor"))

if num2 == 0:
    print("Ingrese un valor que no sea el número 0 en el Segundo número")
else:
    print(f"el resultado de la división es :", num1 / num2)
    

#condicional prueba 3
    
num1 = int(input("ingrese un entero"))

if num1 %2 == 0:
    print("El número es par")
else:
    print("el número es impar")
    

#condicional prueba 4
    
    
edad = int(input("Ingrese su edad"))
ingresos = int(input("Ingrese el total de su salario"))

if edad >=18 and ingresos >= 3000000:
    print("Debe tributar")
else:
    print("No debes tibutar")



#condicional prueba 5

edad = int(input("Ingrese su edad: "))

entradaAdultos = 100000
entradaAdolecentes = 80000
entradaNinos = 5000

if edad <= 4:
    print(f"Debe pagar la entrada para niños, el valor es {entradaNinos}")
elif edad >= 5 and edad <= 18:
    print(f"Debe pagar la entrada para adolescentes, el valor es {entradaAdolecentes}")
else:
    print(f"Debe pagar la entrada para adultos, el valor es {entradaAdultos}")
     