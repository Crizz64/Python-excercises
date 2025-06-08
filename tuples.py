
#In Python, tuples are a fundamental collection type used for storing an 
# ordered sequence of items that should remain unchanged.

#In this lesson, you will learn how to work effectively with tuples.

scores = (7, 9, 9, 8, 9)
print("# of 7:",scores.count(7))
print("# of 9:",scores.count(9))
print("# of 2:",scores.count(2))

#ejercicio 2

points = (12, 14, 9, 10, 9)
for point in points:
  if point > 10:
    print(point, ": passed")

#You can use tuples in any control flow structures, 
# such as if-else statements and loops, just as you would with lists.



#Ejercicio 3


birthday_date = (12, "August", 1993)
day, month, year = birthday_date

print(day)
print(month)
print(year)

#Tuple unpacking allows for assigning tuple items to variables. 
# The values will be assigned in the order they appear in the tuple.


#Ejercicio 4

grades = (76, 81, 96)
math, history = grades
print(math, history)

#Tuple unpacking can also be used to assign values to multiple variables at once.

#Ejercicio 5




#The * operator in tuple unpacking is used to gather multiple elements from 
# the tuple into a list. This is useful when dealing with tuples of unknown 
# length.

