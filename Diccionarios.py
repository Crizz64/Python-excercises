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


