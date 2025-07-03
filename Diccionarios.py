#Dictionaries are collection types used to store data in key:value pairs, 
# which are considered as items. They are ideal for organizing data into pairs, 
# where each piece of data (value) has its unique identifier (key).

#For example


car = {
  "brand": "Audi",
  "model": "Q5",
  "year": "2008"
}

print(car["brand"])
print(car["model"])
print(car["year"])

#ejercicio 1
# In this exercise, you will create a dictionary to store contact information.
# The dictionary should contain the name and company of the contact.

contact = {
  "name": "John",
  "company": "Google",
}
print(contact["company"])



#ejercicio 2

#You can get all the values and keys of a dictionary using 
# the values() and keys() functions, respectively.

contact = {
  "name": "John",
  "company": "Google",
}
info_keys = contact.keys()
info_values = contact.values()

print(info_keys)
print(info_values)


#ejercicio 3

car = {
  "brand": "Audi",
  "model": "Q5"
}
info = car.items()
print(info)

#The items() function returns a list of tuples, where each tuple contains a key-value pair from the dictionary.
# You can use this to iterate over the key-value pairs in a dictionary.


#ejercicio 4

#You can use keys not only to access values in a dictionary,
# but also to change them.

car = {
  "brand": "Audi",
  "model": "Q5",
  "year": "2008"
}

car["year"] = "2010"
print(car["year"])



#ejercicio 5

user = {
  "Name": "Albert",
  "Age": 29
}
user["Age"] = 30

print(user["Age"])
print(user.items())


#The update() function updates the dictionary with the 
# items from the given argument.

#The argument must be a dictionary with the item you want 
# to update.

user = {
  "Name": "Albert",
  "Age": 29
}

# argument: dictionary {"Age": 30}
user.update({"Age": 30})

print(user["Age"])
print(user.items())

#ejercicio 6
#The update() function can accept dictionaries with 
# multiple items.If an item is new, it will be added to the original dictionary.

user = {
  "Name": "Albert",
  "Age": 29
}

# "Surname": "Johnson" will be added
user.update({"Age": 30, "Surname": "Johnson"})

print(user.items())


#ejercicio 7
#The pop() function removes the item with the specified key 
# name. It accepts the key of the item you want to remove 
# as an argument.

user = {
  "Name": "Albert",
  "Age": 29
}

user.pop("Age")

print(user.items())



#ejercicio 8
#You can use the in operator to check if a key or a value 
# occurs in a dictionary.

user = {
  "Name": "Albert",
  "Age": 29
}

print("Name" in user)  # True
print("Surname" in user)  # False
print("Albert" in user.values())  # True
print(30 in user.values())  # False


#ejercicio 9
#You can iterate through a dictionary using a for loop.
#If you loop through a dictionary, it will return the keys.

car = {
  "Brand": "Ford",
  "Model": "Mustang",
  "Color": "red"
}

for i in car:
  print(i)