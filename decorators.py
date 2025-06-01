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



# Ejercicio 6

#You can apply a decorator to a function using the @ sign. 
# It improves the code readability and provides a clean separation between 
# the function and its decoration.

#When a function with a decorator is called, 
# it automatically includes the behavior defined in the decorator.

def uppercase(func):
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper

@uppercase
def greet():
    return "Welcome!"

# Using the decorated function
print(greet())



# Ejercicio 7

#Decorators are a powerful feature, offering a concise,
#  readable, and efficient way to enhance the functionality
#  of existing functions.

#You can apply the same decorator to several different functions:

def stock_status_decorator(func):
    def wrapper(item):
        result = func(item)
        print(result, ": stock status for", item)
        return result
    return wrapper

@stock_status_decorator
def restock_item(item):
    return "Restocked"

@stock_status_decorator
def sell_item(item):
    return "Sold"

print(restock_item("Laptop"))
print(sell_item("Smartphone"))

