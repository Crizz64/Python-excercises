#Functions are a fundamental concept in programming, greatly enhancing the efficiency and flexibility of your code. Up until now, you've focused on defining and calling functions. However, Python offers advanced techniques to make your code even more powerful and adaptable.

#In this lesson, we'll learn about decorators, special functions that modify or enhance other functions.

def song_name(name):
  return "Song name: " + name
def info(name, func):
  print(func(name))

info("Hallelujah", song_name)



#Ejercicio 2

#outer function
def outer_function():
    print("Hello from the outer function")

    #inner function
    def inner_function():
        print("Hello from the inner function")

    inner_function()

outer_function()


#Ejercicio 3

def greet(name):
    print("Hey", name)

    def account():
        return "Your account is created!"

    message = account()
    return message

print(greet("Bob"))


# Ejercicio 4
def order():
  def prepare():
    return "Your meal is being prepared!"
  status = prepare()
  return status

print(order())def order():
  def prepare():
    return "Your meal is being prepared!"
  status = prepare()
  return status

print(order())


# Ejercicio 5

#Imagine you have a function that generates a message. 
# Your goal is to create another function that takes this original function 
# as an argument and converts the original message into uppercase, 
# without altering the original function's code.

#These functions are known as decorators. In the code below, the uppercase()
#  function acts as a decorator, and the wrapper() function represents
#  the modified (or decorated) version of the greet() function.


def greet():
    return "Welcome!"

#takes a function as an argument
def uppercase(func):
    #wrapper function to keep the
    #original function code unchanged
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper

greet_upper = uppercase(greet)
print(greet_upper())
