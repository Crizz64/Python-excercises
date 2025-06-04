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


