# Sets, unlike lists and tuples, are unordered collections. 
# They are created with curly brackets { }.

guests = {"Mery", "Anna", "Jonathan"}
print(guests)
print(guests[0]) #error


# Sets do not support indexing or slicing, as they are unordered.
# However, you can iterate through a set using a for loop.


dishes = ["Salad", "BBQ", "Spaghetti"]
guests = {"Mery", "Anna", "Jonathan"}
print(dishes[0])
print(guests[0])




# Ejercicio 1

#Sets are mutable, meaning you can add or remove items from them.

#Use the add() and remove() functions, each with a value as an argument, 
# to add or remove it from a set

guests = {'Anna', 'Mery', 'Jonathan'}

#adding 'Robert'
guests.add('Robert')

#removing 'Mery'
guests.remove('Mery')

print(guests)


# Ejercicio 2
#The union() function called returns a new set with all elements 
# from both sets, omitting duplicates.

set1 = {'apple', 'banana'}
set2 = {'banana', 'cherry'}
combined_set = set1.union(set2)
print(combined_set)


# Ejercicio 3

#The difference() function returns a set containing elements that 
# are only in the first set and not in the second.

set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'orange'}
unique = set1.difference(set2)
print(unique)