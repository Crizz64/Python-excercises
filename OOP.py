#To add attributes to a class, you must define the __init__ method. 
# This method's first parameter is always self, which represents 
# the instance of the class. Following self, you specify the attributes 
# you wish to include. Then, inside the function, 
# you assign values to the initialized object's attributes, setting their initial state.

class Car:
  # Initialize attributes
  def __init__(self, brand, color):
    # Assign values to attributes
    self.brand = brand
    self.color = color

# Create an object of the Car class
my_car = Car('Audi', 'yellow')

print(my_car)


# Ejercicio 2

#After an object is created, you can access its attributes by using the dot . 
# notation with the variable holding the object.

class Car:
  # Initialize attributes
  def __init__(self, brand, color):
    # Assign values to attributes
    self.brand = brand
    self.color = color

# Create an object of the Car class
my_car = Car('Audi', 'yellow')

# Display attribute values
print(my_car.brand)
print(my_car.color)


# Ejercicio 3
# In addition to attributes, 
# you can add custom behaviors to a class by defining functions within it. 
# These functions, known as methods, should include the 'self' parameter to interact with the class instance. You can call these methods 
# using the dot . notation, similar to how you access attributes.

class Car:
  def __init__(self, brand, color):
    self.brand = brand
    self.color = color
    
  def honk(self):
    print("Beep beep!")

my_car = Car('Audi', 'yellow')

my_car.honk()

# The main difference between functions and methods is that functions are 
# independent and can be called on their own, while methods are associated 
# with a class and can be called only with its instance. 
# This means that you can't call a method without having the instance
#  of a class where that method is defined.


# Ejercicio 4

#Everything in Python, including functions, is an object. For instance, 
# integers are instances of the int class, and functions are instances 
# of the function class, among others. 
# This object-oriented nature underlies Python's flexibility and power.
#function
def greet():
  print("Welcome!")

#list
prices = [55, 68, 77, 36]

#data types
x = 5
city = "London"
is_open = True


print(type(greet))
print(type(prices))
print(type(x))
print(type(city))
print(type(is_open))