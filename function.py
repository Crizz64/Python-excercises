num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

def suma(num1, num2):
    resultado = num1+num2
    return resultado

print(f"la suma es {suma(num1, num2)}")

def potencia ():
    valor = suma (2,4)
    potencia = 2
    resultado = valor**potencia
    print(f"la potencia es {resultado}")

potencia()

#--------- solo learn
def shout(text):  
    return text.upper()
yell = shout
print(yell("Hello"))

#ejercicio 1 - funciones que imprimen un valor

def saludar(nombre):
    print("hola ", nombre)


saludar("Cristian")


#ejercicio 2 - Funciones que retornan un valor

def sumar(a, b):
    return a + b

resultado = sumar(26 + 45)
print("el resultado: ", resultado)


#ejercicio 3 

def sumar(x, y):
    return x + y

x = int(input("ingrese un número"))
y = int(input("ingrese el segundo número"))
resultado = sumar(x, y)

print(f"el resultado es {resultado}")



#ejercicio 4

def dividir(x , y):
    
    if y != 0:
        print(f"el resultado es {x/y}")
    else:
        print("No se puede divir")

dividir(45 , 0)



#ejercicio 5

def digite(a):
    return a*a
a = int(input("ingrese un número"))
resultado = digite(a)
print(f"la potencia es {resultado}")


#ejercicio 6

def sumar(lista):
    total = 0
    for i in lista:
        if i %2==0:
            total += i
    return total

lista_numeros = []
validar = input("desea agregar números?").lower()
while validar != "no":
    agregar_num = int(input('agrega un nuevo número: '))
    lista_numeros.append(agregar_num)
    validar = input('desea agregar otro número?').lower()

resultado = sumar(lista_numeros)
print(f"el resultado es {resultado}")



# Ejercicio 7
#Functions can take other functions as arguments.


def welcome(name):
  return "Welcome, " + name

def process_user(name, func):
    return func(name)

print(process_user("Alice", welcome))


# Ejercicio 8

def order(dish):
    return "Your order: " + dish

def process_order(dish, func):
    print(func(dish))


# Ejercicio 9

def welcome(name):
  return "Welcome, " + name

def bye(name):
  return "Goodbye, " + name

def process_user(name, func):
  return func(name)

print(process_user("Alice", welcome))
print(process_user("Bob", bye))


# Ejercicio 10

def book_title(title):
  return "Book title: " + title
def info(title, func):
  return func(title)

print(info("The Great Gatsby", book_title))