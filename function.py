
#-- ejercicio inicial

#Una función puede requerir argumentos para completar sus tareas. Los argumentos se colocan dentro de los paréntesis () después del nombre de la función.

#definición de la función
def personal_greet(name): 
  print("Hello", name)
  print("Have a great day")


#llamadas a la función
personal_greet("Sarah") 
personal_greet("Henry")


#-- Ejemplo con valor de retorno

#Definir función
def bmi(weight, height):
  index = weight / (height * height)
  return index  #sends the return value back

#Llamando a una función y usando el valor de retorno
patient_5 = bmi(61, 1.83) #stores return value
print("underweight:", patient_5 < 18.5)

#Otra llamada
patient_7 = bmi(75, 1.74)
print("underweight:", patient_7 < 18.5)



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



# Ejercicio 11

#tomar el peso como entrada
weight = int(input())

#completar la función
def shipping_cost(weight):
    x = weight * 5
    print(x)


#llamar a la función
shipping_cost(weight)



# Ejercicio 12

def rect(length, width):
  area = length * width
  perimeter = 2 * length + 2 * width
  return area, perimeter #2 valores

x, y = rect(50, 100) #2 variables
print(x, y)



#tomar una palabra como entrada
word = input()

def hashtag(word):
    #completar el cuerpo de la función
    return "#" + word

#mostrar el resultado
print(hashtag(word))