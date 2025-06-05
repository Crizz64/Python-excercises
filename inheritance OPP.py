#The strength of OOP lies in organizing a program so its various components, 
# treated as classes and objects, can interact smoothly.

#In this lesson you will learn about the principle of inheritance, 
# an OOP concept that enhances your program's versatility and efficiency.

class Animal:
  def __init__(self, name):
    self.name = name
  
  def move(self):
    print("Moving")

# Inherits from Animal class
class Dog(Animal):
  # Specific behavior
  def bark(self):
    print("Woof!")
    
# Creating an instance
my_dog = Dog("Bob")

# Inherited attribute and behavior
print(my_dog.name)
my_dog.move()

# Specific behavior
my_dog.bark()



#exercise 2

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print("El vehículo ha arrancado")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def abrir_puerta(self):
        print("La puerta se ha abierto")

mi_coche = Coche("Toyota", "Corolla", 4)
print(mi_coche.marca)  # Salida: Toyota
mi_coche.arrancar()  # Salida: El vehículo ha arrancado



#exercise 3

#What if we want to not only inherit attributes but also add specific 
# ones to a child class? In this case, we define an __init__ 
# method in the child class. Use super().__init__() to inherit 
# attributes from the parent class, and then define any additional attributes
#  as usual.

#parent class
class Animal:
  def __init__(self, name):
    self.name = name
  
  def move(self):
    print("Moving")

#child class
class Dog(Animal):
  def __init__(self, name, breed, age):
    # Initialize attributes of the superclass
    super().__init__(name)
    # Additional attributes specific to Dog
    self.breed = breed
    self.age = age

  def bark(self):
    print("Woof!")


my_dog = Dog("Jax", "Bulldog", 5)
#inherited attribute
print(my_dog.name)

#Additional attributes
print(my_dog.breed)
print(my_dog.age)


#The super() function is used to refer to the parent class, 
# allowing access to its methods and attributes from within a subclass.


#exercise 4

#You can define methods with the same name in both parent and child classes, 
# but they can perform different operations. This is known as method overriding. 
# For instance, consider the Animal class with a sound method. 
# The Dog and Cat child classes inherit the sound method from Animal 
# but override it to suit their specific needs.

# Parent class
class Animal:
  def __init__(self, name):
    self.name = name

  # Generic sound method for any animal
  def sound(self):
    print("Making a sound")

# Child class Dog
class Dog(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age
  
  # Overridden sound method for Dog
  def sound(self):
    print("Woof!")

# Child class Cat
class Cat(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age

  # Overridden sound method for Cat
  def sound(self):
    print("Meow!")

# Creating instances
my_dog = Dog("Jax", "Bulldog", 5)
my_cat = Cat("Lily", "Ragdoll", 2)

# Using overridden methods
my_dog.sound()
my_cat.sound()



#exercise 5

#You can use the super()  function if you want to call a method from the parent
#  class while overriding it.

#This is useful when you want to add some functionality to the child class method 
# without changing the original one.

# Parent class
class Animal:
  def __init__(self, name):
    self.name = name

  # Generic sound method for any animal
  def sound(self):
    print("Making a sound")

# Child class Dog
class Dog(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age
  
  # Overridden sound method for Dog
  def sound(self):
    # Call the sound method from Animal
    super().sound()
    # Additional functionality for Dog
    print("Woof!")

# Creating an instance of Dog
my_dog = Dog("Jax", "Bulldog", 5)

# Calling the overridden sound method
my_dog.sound()



#exercise 6

#Method overriding is a demonstration of another key concept in OOP - polymorphism. 
# Polymorphism lets objects use methods in their own way, 
# even if they share the same name.

#In this example, even though each animal in the animals list may be of a 
# different subclass, the code can call sound() on each without 
# needing to know its specific type.
# Parent class

class Animal:
  def __init__(self, name):
    self.name = name

  # Generic sound method for any animal
  def sound(self):
    print("Making a sound")

# Child class Dog
class Dog(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age
  
  # Overridden sound method for Dog
  def sound(self):
    print("Woof!")

# Child class Cat
class Cat(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age

  # Overridden sound method for Cat
  def sound(self):
    print("Meow!")

# Creating instances
my_dog = Dog("Jax", "Bulldog", 5)
my_cat = Cat("Lily", "Ragdoll", 2)

animals = [my_dog, my_cat]

for animal in animals:
  animal.sound()