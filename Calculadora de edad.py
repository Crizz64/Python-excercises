anoactual= int(2025)
anodenacimiento= int(input('Ingrese su ano de nacimiento: '))
edad= anoactual-anodenacimiento

print('Usted nacio en el ano',edad)

numero1=int(input("Ingrese un numero que desee sumar: "))
numero2=int(input("Ingrese un numero que desee sumar: "))

suma=numero1+numero2

print('La sumatoria de ',numero1, 'y',numero2, 'es: ', suma)

edad=int(input('Ingrese su edad: '))
if edad>= 18:
    print('Usted es mayor de edad')
else: 
    print('Usted es menor de edad')


numero= int(input('Escriba un numero positivo: '))
if numero<0:
    print('He dicho que escriba un numero positivo !')
print('Ha escrito  el numero ',numero)    

'''Ejercicio de clase ciclos if anidadoos'''

print ('Este programa mezcla dos colores')
print("  r. Rojo    a. Azul")
primera= input("elija un color (r o a): ")
if primera == 'r':
    print(' a. Azul   v. Verde')
    segunda = input('Elija otro color (a o v): ')
    if segunda == 'a':
        print('La mezcla de rojo y azul produce magenta.')
    else: 
        print('La mezcla de rojo y verde produce amarillo')
else:
    print(' v. Verde    r. Rojo')
    segunda = input('Elija otro color (v o r): ')
    if segunda == 'v':
        print('La mezcla de azul y verde produce cian.')
    else: 
         print('La mezcla azul y rojo produce magenta.')
         
'''ejercicio de clase if y elif'''

edad= int(input('Cuantos anios tiene? : '))
if edad<0:
    print('No se puede tener una edad negativa')
elif edad < 18:
    print('Usted es menor de edad')
else: 
    print('Usted es mayor de edad')
    
''' ejercicio de contrasena'''

contrasena= 'Harold'
password= input('Digite su contrasena: ')
if password==contrasena:
    print(f'Su contasena {password} es correcta')
else:
    print(f'Su contasena {password} es incorrecta')
    
'''Division con condicion'''

num1= int(input('Ingrese un numero: '))
num2= int(input('Ingrese un numero: '))

if num2 == 0:
    print('No se puede dividir por cero')
else:
    print(f'el resultado es {num1/num2}')
    
''' Numero entero par o impar'''
n1=int(input('Ingrese un numero entero: '))

if n1 % 2==0:
    print('El numero es par')
else:
    print('El numero es impar')
    
'''Tributar o no '''

edad=int(input('ingrese su edad'))
salario=int(input('ingrese su salario'))

if edad>=18 and salario>3000000:
    print('Usted debe tributar')
else:
    print('Usted no puede tributar')

'''calculo de precios por edad'''

edad= int(input('Por Favor ingrese su edad: '))

if edad<=4:
    print('Entra gratis')
elif edad > 4 and edad<18:
    print('Paga 5k')
else:
    print('paga 10k')
    
'''Tablas de multiplicar'''

numero=int(input('Ingrese un numero: '))

for j in range(1,numero+1):
    
    for i in range(1,11):
        resultado=i*j
        print(f'{j}x{i}={resultado}')
        
    print('')
    
'''Funcion para desconponer cualquier numero'''

def descomponer_numero(numero):
    digitos = []
    while numero > 0:
        digito = numero % 10  # Obtener el último dígito
        digitos.append(digito) #anade elementos a una lista
        numero = numero // 10  # Eliminar el último dígito
    digitos.reverse()  # Invertir la lista para obtener el orden correcto
    return digitos

descomponer = int(input('Ingrese un numero que desee descomponer: '))
resultado = descomponer_numero(descomponer)
print(f"Los dígitos de {descomponer} son: {resultado}")

'''Clase 4 de febrero de 2024'''
'''Cliclo while'''

i=1
while i <=50:
    print(i)
    i=3*i+1
print('Programa terminado')

numero= int(input('Escriba un numero positivo: '))
while numero <0:
    print(' Ha escrito un numero negativo! Intentelo de nuevo')
    numero= int(input('Escriba un numero positivo'))
print('Gracias por su colabracion')

palabra= input(' Desea continuar')
while palabra == 'SI':
    palabra= input('Desea continuar')
print('Gracias por su colabracion')

'''ciclo for'''

print('Comienzo')
for i in [0, 1, 2]:
    print('Hola', end=" ") #'''print('texto', end=) imprime horizontalmente'''
print() #'''Salto de linea'''
print('Final')

print('Comienzo')
for i in range(10):
    print('Hola', end=' ')
print()
print('Final')

numero= int(input('Cuantos numeros desea introducir'))
primernumero=int(input('Ingrese un numero: '))
for i in range(numero-1):
    numeropedido=int(input("ingrese otro numero: "))
    if primernumero<numeropedido:
        print(f'El numero {numeropedido} es mayor a {primernumero} ')

'''Clase 5 de febrero 2025'''
'''Listas (Mutables [entre corchetes]) 
    tuplas(inmutables (entre parentesis)) y range '''

'''Ejemplo lista'''
lista_compras=['leche','huevos','pan','lechuga']
numeros_loteria=[2114,728,4932,4114,3666,]

print(lista_compras[2])

print(lista_compras)
print(numeros_loteria)

'''Ejemplo tupla'''
objetos=('sombrilla','cuaderno','detergente')
numeros_loteria=(187,215,363,447,559)
print(objetos[2],objetos[0])
print(objetos)
print(numeros_loteria)

'''Ejercicio de clase'''


lista_compras=['leche','huevos','pan','lechuga']
pedido_cliente=input('Ingrese que desea: ')
if lista_compras[2] == pedido_cliente:
    print('El pan cuesta 1.200')
elif lista_compras[0] == pedido_cliente:
    print('La leche cuesta 5.500')
elif lista_compras[1] == pedido_cliente:
    print('EL cuaderno cuesta 7.500')
elif lista_compras[3] == pedido_cliente:
    print('La lechuga cuesta 3.000')
else:
    print('Suerte pecueca')

'''metodo append '''

lista_compras=['leche','huevos','pan','lechuga']
print('Esta es tu lista de compra: ',lista_compras)

lista_compras.append('Azucar') # anade un dato al final de la lista
print('Esta es tu lista de compra: ',lista_compras)

'''metodo extent sirve para combinar dos listas o una tupla a una lista'''
lista1= [1,2,3]
lista2= [4,5,6]

lista1.extend(lista2) # Combina la lista 2 en la lista 1 al final
print(lista1)

'''metodo inset'''

lista_compras=['leche','huevos','pan','lechuga']
print('Esta es tu lista de compra: ',lista_compras)

lista_compras.insert(1,'Arroz') # anade un dato en la pisicion indicada en la lista y desplaza a la derecha los demas elementos
print('Esta es tu lista de compra: ',lista_compras)

'''Ejercicio de clase'''

producto_pedido=input('Quiere agregar un producto: ').lower()
lista_de_productos=[]
while producto_pedido == 'si':
    producto_nuevo=input('Ingrese el producto: ').lower()
    if producto_nuevo == 'cigarrillos':
        condicion=int(input('cuantos anios tienes: '))
        if condicion>=18:
            print('Eres mayor de edad agregaremos tu producto')
            lista_de_productos.append('cigarrillos')
        else:
            print('Eres menor de edad no puedes agregar este producto')
    else:
        lista_de_productos.append(producto_nuevo)
    producto_pedido=input('Quiere agregar un producto: ').lower()
print('Los productos agregados son: ', lista_de_productos)

'''metodo pop'''

lista_compras=['leche','huevos','pan','lechuga']
print('Esta es tu lista de compra: ',lista_compras)

lista_compras.pop(0) # Elimina un indice de la lista seleccionada y desplaza a la izquierda
print('Esta es tu lista de compra: ',lista_compras)

'''metodo remove'''

lista_compras=['leche','huevos','pan','lechuga']
print('Esta es tu lista de compra: ',lista_compras)

lista_compras.remove('huevos') # elimina el valor exacto de la lista
print('Esta es tu lista de compra: ',lista_compras)

'''ejemplo de clase para recorrer una lista'''

ciudades= ['Pereira', 'Manizales', 'Cali']
ciudades.append('Medellin')

for ciudad in ciudades:
    if ciudad == 'Pereira':
        print('Hola Pereira')
    elif ciudad == 'Manizales':
        print('Hola Patifrios')
    print(ciudad)

'''Ejercicio de clase'''

Listaclase= []
for i in range(1,11):
    Listaclase.append(i)
print(Listaclase)
for j in Listaclase:
    if j%2==0:
        Listaclase.remove(j)
print(Listaclase)

'''Clase 6 de febrero 2025'''

'''Diccionarios en Python''' # Se identifican con {}

midiccionario={
    'Nombre': 'Martha',
    'Edad': 55,
    'Genero':'Femenino'    
}
print(midiccionario)
print(midiccionario['Nombre'])

diccionario={
    'Nombre': 'Martha',
    'Apellido': 'Lenola',
    'Alias':'Martica',
    'Padres':['Maria Chaira','Carlos Cortez'],
    'Edad':55,
    'Genero':'Femenino',
    'Estado civil':'Soltera',
    'Hijos':'Ninguno/a',
    'Mascotas':'Gatos',
    'Nombres de mascotas':['Mango','Doble filo'],
}
diccionario['Nombres de mascotas'][1]='Aurelio'
diccionario ['Ingresos']=1600
diccionario['Salario']= diccionario.pop('Ingresos')
diccionario['Comidas favoritas']=[]

pregunta=input('Desea agregar una comida favorita, responda "si" o "no"').lower()

while pregunta == 'si':
    comida=(input('Ingrese la comida que desea agregar'))
    diccionario['Comidas favoritas'].append(comida)
    pregunta=input('Desea agregar otra comida favorita, responda "si" o "no"').lower()
print(diccionario['Comidas favoritas'])
print('Gracias por su colaboracion')

pregunta2=input('Tiene usted algun estudio, si o no').lower()
diccionario['Estudios']= []

if pregunta2 == 'si':
    estudio= input('Ingrese su estudio')
    diccionario['Estudios'].append(estudio)
    pregunta3=input('Desea agregar otro estudio, "si" o "no"').lower()
    while pregunta3 == 'si':
        estudio= input('Ingrese su estudio')
        diccionario['Estudios'].append(estudio)
        pregunta3=input('Desea agregar otro estudio, "si" o "no"').lower()
elif pregunta2 == 'no':
    diccionario['Estudios']='Sin Estudios'

## Este ciclo for me sirve para recorrer un diccionario en sus indices
for datos in diccionario:
    print(datos,':',diccionario[datos])
    
# Crear un sistema que permita agregar productos, los productos 
# estan compuestos por las siguientes caracteristicas:
# Nombre, Cantidad, Categoria

agregar_producto= input('Desea agregar un producto: ').lower()
inventario={}
producto=[]
contador =1
while agregar_producto == 'si':
    nombre_producto= input('Ingrese el nombre del producto: ')
    cantidad_producto= input('Ingrese la cantidad del producto: ')
    categoria_producto= input('Ingrese la cateroria del producto: ')
    producto.append(nombre_producto)
    producto.append(cantidad_producto)
    producto.append(categoria_producto)
    identificador_producto = 'Producto',contador
    inventario[identificador_producto]= producto
    producto = []
    contador +=1
    agregar_producto = input('Desea agregar otro producto: ')

for datos in inventario:
    print(datos,':',inventario[datos])
    
    
## Ejemplo de random.choice

import random
# Ejemplo con una lista
opciones_frutas = ['Mango', 'Pera', 'Manzana', 'Cereza']
fruta_aleatroria = random.choice(opciones_frutas)
print('Fruta seleccionada: ',fruta_aleatroria)
# Ejemplo con una tupla
opciones_colores = ('rojo', 'verde', 'azul', 'amarillo')
color_aleatorio = random.choice(opciones_colores)
print('Color seleccionado: ', color_aleatorio)
# Ejemplo con una cadena de caracteres 
cadena = "Jhonatan Suarez, Wilmer Molano, Harold Quintero"
caracter = random.choice(cadena)
print("Carácter seleccionado:", caracter)

# Ejemplo de upper, lower, capitalize y tittle

Frase = input('Desea ingresar una fraase: ').lower()
lista_frase=[]
while Frase == 'si':
    Frase= input ('Ingrese una frase:')
    lista_frase.append(Frase)
    Frase = input('Desea ingresar una fraase: ').lower()
    
Frase_uper= print('La frase en mayuscula es: ',lista_frase)
Frase_lower= print('La frase en minuscula es: ',lista_frase.lower())
Frase_capitalize= print('La frase Capitalizada es: ',lista_frase.capitalize())
Frase_title= print('La frase en Titulos es: ',lista_frase.title())

# getpass sirve para crar contrasenas 
import getpass

contasena= input('Guarde su contrasena: ')
clave_de_acceso= getpass.getpass('Intrudocue tu contrasena')

if contasena == clave_de_acceso:
    print('Ingreso la contrasena correcta')
else:
    print('Contrasena incorrecta')

'''Tema'''
# strip() elimina un caracter de una cadena al inicio o fin
# join() convierte una lista en una cadena
# split() convierte una cadena en una lista

# Ejemplo de .strip()
cadena= '*Eliminar caracteres especificos *'
palabra= cadena.strip('*')
print(palabra)
# Salida= Eliminar caracteres especificos

# Ejemplo de .join()
lista= ['probar','si','divide','este','texto']
palabra= ' '.join(lista)
print(palabra)
# Salida= probar si divide este texto

# Ejemplo de .split()
cadena= 'probar si divide este texto'
palabras = cadena.split(' ')
print(palabras)
# Salida= ['probar', 'si', 'divide', 'este', 'texto']

from collections import Counter

frutas= ['manzana','pera','manzana','uva','arandano','manzana','pera','fresa']
