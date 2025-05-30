#Up to this point, you've been defining functions with a fixed number
#of known arguments.

#In this section, you will learn about techniques 
#that enhance the adaptability of functions, making them more 
#versatile and ready for different scenarios.


#If the number of arguments of your function is unknown and unpredictable, you can always use an iterable as an argument.

#Here is an example of using a list as an argument.
def total(numbers):
  result = 0
  #iterating over the list
  for i in numbers:
    result+=i
  return result

nums = [1,2,3,4,5]

print(total(nums))


#Ejercicio 2
#The *args syntax allows you to 
#pass a variable number of positional arguments to a function.

def total(*args):
  result = 0
  for arg in args:
    result += arg
  return result

print(total(1, 2, 3, 4, 5))
print(total(1, 2, 3, 4, 5, 6, 7))
print(total(1, 2, 3))


#Ejercicio 3
#Note that args is just a name. You’re not required to use the name args.
#  You can choose any name that you prefer.

def total(*prices):
  result = 0
  for arg in prices:
    result += arg
  return result

print(total(1, 2, 3, 4, 5))
print(total(1, 2, 3, 4, 5, 6, 7))
print(total(1, 2, 3))

#Ejercicio 4
def display(*words):
  for item in words:
    print(item)
display("paper", "pen", "pencil")


#Ejercicio 5
#When defining a function with both regular arguments and *args, 
# the regular arguments must come before *args in the function definition.

#For example
def show_items(category, *items):
  print("Category: " + category)
  for item in items:
    print(item)

show_items("Electronics", "Laptop", "Smartphone", "Tablet")

#Ejercicio 6
#Python also allows you to pass keyword arguments using **kwargs. In this case, **kwargs receives arguments in the form of a dictionary, consisting of key:value pairs.

#**kwargs is a dictionary
def display_info(**kwargs):
  #kwargs.items() returns the key:valie pairs
  for key, value in kwargs.items():
    print(key, ":", value)

display_info(name="Alice", age=30, city="New York")


#Ejercicio 7
#The **kwargs syntax allows you to pass a variable number of keyword arguments to a function.
def total(**kwargs):
  result = 0
  for key, value in kwargs.items():
    result += value
  return result


print(total(a=1, b=2, c=3))


#Ejercicio 8
def total(*args, **kwargs):
  result = 0
  for arg in args:
    result += arg
  for key, value in kwargs.items():
    result += value
  return result
