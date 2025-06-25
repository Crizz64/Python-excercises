#The map() function applies a specified function to every element 
# in an iterable, like lists or tuples. It produces a result that 
# can be transformed into a list using the list() function 
# for easy viewing or further use.

#List of names in various cases
names = ["alice", "bob", "CHARLIE", "dEborah"]

# Function to capitalize each name
def capitalize(name):
  return name.capitalize()

# Using map() to apply the capitalization to each name
capitalized = map(capitalize, names)

# Converting map object to a list
capitalized = list(capitalized)

print(capitalized)


#Ejercicio 2

prices = [25.99, 14.50, 8.75, 19.95]
def discount(price):
  discounted_price = price * 0.9
  return discounted_price

discounted_prices = list(map(discount, prices))

print(discounted_prices)


#Ejercicio 3

exam_scores = [85, 62, 95, 40, 78]
def is_passing(score):
  return score >= 70

status = list(map(is_passing,exam_scores)) #The map function requires the first argument to be a function and the second argument to be an iterable.

print(status)

#Ejercicio 4
exam_scores = [85, 62, 95]
def passing(score):
  return score >= 70

status = list(map(passing, exam_scores))

print(status)


#Ejercicio 5
#their ability to be directly provided to the map function. This eliminates the need to define a regular function explicitly.

numbers = [1, 2, 3]
doubled = list(map(lambda x: x*2, numbers))

print(doubled)


#Ejercicio 6

#The filter() function, just like the map() function, 
# takes in a function and an iterable as arguments. 
# The key purpose of filter() is to apply a condition 
# specified in the provided function to each item in the 
# iterable and return only those for which the function evaluates to True.

#This code filters and returns products with names 4 characters long.

products = ["Table", "Sofa", "Cushion", "Bookshelf", "Vase"]

# Filters products with name length equal to 4
filtered_prod = list(filter(lambda name: len(name) == 4, products))

print(filtered_prod)



#Ejercicio 7

#The map() and filter() functions can work with any iterable. In the example below, 
# filter() is used to extract items from the products dictionary, 
# where prices are under 90.

products = {'Table': 110, 'Sofa': 120, 'Chair': 45, 'Lamp': 70}

#filtering products with prices less than 90
filtered_products = dict(filter(lambda item: item[1] < 90, products.items()))

print(filtered_products)



#Ejercicio 8

names = ["John", "Emma", "Jake", "Rachel", "James"]
filtered = list(filter(lambda name: name[0] == 'J', names))

print(filtered)


# Ejercicio 9
# The filter() function is used to filter out elements from an iterable based on a condition.
# In this example, we filter out empty answers from a list of user responses.

user_answers = ["Yes", "", "No", "", "Maybe", "", "Yes"]

# Create a new list without empty answers
# using filter with a lambda expression

filter1 = list(filter(lambda x: x != "", user_answers))

# Display the cleaned list of answers

print(filter1)