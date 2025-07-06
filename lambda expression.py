#Functional programming has advantages in terms of making your code more efficient and organized.

def total(price, count):
  return price*count

print(total(2,3))

# Ejercicio 2

greet = lambda name: "Welcome, " + name

print(greet("Bob"))

#Lambda expressions perform a single operation and return a result. They are defined using the lambda keyword, followed by its arguments, a colon, and the expression to perform.


#Ejercicio 3

discount = lambda price: price * 0.9 
print(discount(100))


#Ejercicio 4

x = lambda price, count :  price * count
print(x(2,10))


#Ejercicio 5
#You can provide arguments to lambda expressions on-the-fly by adding them in parentheses immediately after the lambda function. The lambda expression should be also enclosed in parentheses.

res = (lambda x, y: x + y) (2, 3)
print(res)


#Ejercicio 6
#The power of lambda is better shown when you use them as an anonymous function inside another function. Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def mult(n):
  return lambda a : a * n

doubler = mult(2)
tripler = mult(3)

print(doubler(5))
print(tripler(5)) 