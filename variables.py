
#ejercicio 1
compraTotal = 155000
propina = 15500
total = compraTotal + propina

print(f"El total con propina es: {total}")


#ejercicio 2

anoActual = 2025
fechaNacimiento = int(input("Ingrese su fecha de naciemiento: "))

print(f"su edad es {anoActual - fechaNacimiento}")


#ejercicio 3

num1 = int(input("Ingrese su quincena: "))
num2 = int(input("Ingrese el valor de su bono: "))

total = (num1*2)+num2

print(f"Su salario más bonos es de: {total}")



n = int(input(""))

print(n**2)



N = int(input())

for i in range(2, N + 1, 2):
    print(f"{i}^2 = {i ** 2}")



x = int(input(""))
y = int(input(""))

if x >= 0 and y >=0:
    print("Primeiro")

elif x >= 0 and y < 0:
    print("quarto")

elif x < 0 and y < 0:
    print("terceiro")
    
elif x < 0 and y >= 0:
    print("segundo")

else:
    print("No existe")