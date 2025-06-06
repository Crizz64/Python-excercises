#Data hiding is a key idea in making code with objects (like in games or apps)
#  safer and cleaner. It means keeping some parts of an object private
#  so that only certain parts of your code can change them. 
# This helps prevent mistakes and keeps your code easy to manage.


#In this lesson, you'll explore how data hiding contributes to encapsulation
#  in OOP, enhancing the security and robustness of your code.




#Consider the Car class provided below. After creating an instance of this class,
#  you can access and modify its attributes, as well as call its methods. 
# Open the code, explore its functionality, and run it to observe the results.


class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    self.odometer = odometer

  def describe_car(self):
    print(self.year, self.model)

  def read_odometer(self):
    print("Odometer:", self.odometer, "miles")

my_car = Car('Audi', 2020, 15000)

my_car.describe_car()
my_car.read_odometer()

#changing a value of the attribute
my_car.odometer = 20000

my_car.read_odometer()



# exercise 2
#In Python, data hiding has two levels. 
# The first involves prefixing an attribute with a
#  single underscore _, signaling it's meant for internal use and should
#  be viewed as 'protected'.


class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'protected'
    self._odometer = odometer  

  def describe_car(self):
    print(self.year, self.model)

  def read_odometer(self):
    print("Odometer:", self._odometer, "miles")

my_car = Car('Audi', 2020, 15000)

my_car.odometer = 20000 #odometer has been protected it cannot be accessed directly
my_car._odometer = 20000  # Accessing the protected attribute directly (not recommended)


my_car.describe_car()
my_car.read_odometer()


# exercise 3
#Attributes with a single underscore are accessible but considered protected 
# by convention, signaling they're for internal use and should be accessed 
# cautiously outside the class.

#To access a protected attribute outside of the class, 
# use the single underscore prefix, as that's part of the attribute's name.

class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'protected'
    self._odometer = odometer  

  def describe_car(self):
    print(self.year, self.model)

  def read_odometer(self):
    print("Odometer:", self._odometer, "miles")

my_car = Car('Audi', 2020, 15000)

#accessing the protected attribute
print(my_car._odometer)



# exercise 4
#The next level of data hiding involves making an attribute private. 
# This is achieved by prefixing the attribute name with 
# two underscores (e.g., __attribute). In this case, 
# unlike protected attributes, this is not just a convention - 
# it limits its access outside the class through name mangling, 
# enhancing data protection and encapsulation. 
# This method is used for sensitive or internal data,
# strongly discouraging external access.


class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer

    def describe_car(self):
        print(self.year, self.model)

    def read_odometer(self):
        print("Odometer:", self.__odometer, "miles")

my_car = Car('Audi', 2020, 15000)
# Attempting to access the private attribute directly will raise an AttributeError
my_car.read_odometer()


print(my_car.__odometer)  # This will raise an error



#exercise 5

#Accessing a private attribute directly from outside its class is generally
#  discouraged in Python. However, Python employs name mangling for private 
# attributes, which means you can access them using a specific naming 
# convention from outside the class if necessary. 

class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer  

  def describe_car(self):
    print(self.year, self.model)

  def read_odometer(self):
    print("Odometer:", self.__odometer, "miles")

my_car = Car('Audi', 2020, 15000)

#accesing using name mangling
print(my_car._Car__odometer)


#exercise 6
#You can also designate methods as protected or private, 
# following the same convention as with attributes. Protected methods 
# are prefixed with a single underscore and can be accessed within the class 
# and its subclasses. However, private methods, marked by a double underscore, 
# cannot be directly accessed from outside the class.

class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer  

  def _describe_car(self):  # Making the describe_car method 'protected'
    print(self.year, self.model)

  def __read_odometer(self):  # Making the read_odometer method 'private'
    print("Odometer:", self.__odometer, "miles")


my_car = Car('Audi', 2020, 15000)

#accessing protected method
my_car._describe_car()

#error when accessing a privet method
my_car._Car__read_odometer()