#condicionales

num1 = int(input("ingrese un valor entero: "))
num2 = int(input("Ingrese otro número"))
num3 = int(input("Ingrese otro dato"))
num4 = int(input("Ingrese otro campo"))

if num1 <= num4:
    print(f"el número {num4} es igual o mayor a: {num1}")
elif num2 >= num3:
    print(f"el número {num4} no es mayor o igual a: {num1}")
else:
    largest_num = max(num1, num2, num3, num4)
    print(f"el número más grande de todos es: {largest_num}")



#ejercicio 1

num1 = int(input("Ingrese un número"))


numPar = {2,4,6,8,10}
numImpar = {1,3,5,7,9}

if num1 in numPar:
    print(f"el Número {num1} es par")
else:
    print(f"El número {num1} es Impar")


#ejercicio 2

Name = input("Ingrese su nombre")
correo = input("Ingrese su correo")

jr = 500000
senior = 1000000
master = 1500000

puesto = input("Ingrese su puesto en la empresa(jr, senior, master)")

if puesto == "jr":
        print(f"Su nombre es {Name}, su correo es {correo}, Su salario es {jr}")
elif puesto == "senior":
        print(f"Su nombre es {Name}, su correo es {correo}, Su salario es {senior}")
else:
        print(f"Su nombre es {Name}, su correo es {correo}, Su salario es {master}")




#ejercicio 3

 




#ejercicio 5

num1 = int(input("por ingrese los últimos 4 digitos de su tarjeta"))
print(num1)


cifraUno = num1//1000 #descompone el número on el operador de división de enteros que extrae el primer digito
cifraDos = (num1//100)%10 
cifraTres = (num1%100)//10
cifraCuatro = num1%10

if cifraUno>cifraCuatro:
    print(f"la cifra ({cifraUno}) es mayor a la cifra ({cifraCuatro})")
elif cifraUno<cifraCuatro:
    print(f"la cifra ({cifraUno}) es menor a la cifra ({cifraCuatro})")
else:
    print(f"la cifra ({cifraCuatro}) es mayor")


if cifraDos %2 == 0: 
     print(f"la cifra ({cifraDos}) es par")
else:
     print(f"la cifra ({cifraDos}) es impar")