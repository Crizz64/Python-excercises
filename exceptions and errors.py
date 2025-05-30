prices = [250, 300, "240", 400]
try:
  #block that may cause an exception
  total = sum(prices)
  print(total)

except TypeError:
  # to perform if there is an exception
  print("Invalid data type")

print("Happy Shopping")


#ejemplo 2

colors = ['Red', 'Yellow', 'Green']
try:
  #index error
  print(colors[10])
  
  #wrong exception
except NameError:
  print("Error")

#will not be executed
print("Happy Shopping")


#ejemplo 3
#Traducir curso
#You can have multiple except blocks to handle each possible exception specifically. As a best practice, it is recommended to output a definitive message for each type of handled exception.

colors = ['Red', 'Yellow', 'Green']
try:
  print(colors[10])
except IndexError:
  print("Out of range")
except NameError:
  print("Variable is not defined")

print("Happy shopping")

# ejemplo 4
#Exceptions are very helpful when your program interacts with user input. While you can't control what a user inputs, you can control your program's behavior when the input doesn't match the expected format. For instance, this program expects a numerical value as input and will throw an exception when the user inputs a non-numerical one.

price = input()
try:
  price_value = int(price)
except ValueError:
  print("Please enter a number")


  #ejercicio #5

products = ["Water", "Chocolate", "Chips", "Soda", "Sandwich"]
choice_index = int(input())

try:
    print(products[choice_index])

except IndexError:
    print("wrong index")


    #ejercicio #6
    #You can use the finally statement to perform an operation after the try/except block, no matter if an exception occurred or not.

prices = [559, 879, "N/A", 349]
try:
  print(sum(prices))
except TypeError:
  print("Check the prices")
finally:
  print("Need help? Contact us")
    


    #ejercicio 7

books = ['Harry Potter', 'Dune', 'Emma']
try:
  print(books[5])
except IndexError:
  print("Out of range")
finally:
  print("Happy reading!")


    #Ejercicio 8
    #The else statement can be used in conjunction with the try/except block and will execute only when no error occurs in the try block.

books = ['Harry Potter', 'Dune', 'Emma']
try:
  choice = books[1]
except IndexError:
  print("Out of range")
else:
  print(choice + " is a great choice!")


  #ejercicoi 9

products = ['ball', 'toy', 'paper']
try:
  count = len(products)
except:
 print("Error")
else:
  print("Count of products:", count)



  #ejercicio 10

prices = [12, 55, 69.5]
try:
  total = sum(prices)
except:
  print("Error")
else:
  print("Total:", total)


  #ejercicio 11
  #You can trigger your own exceptions based on specific conditions using the raise statement. This will immediately stop the program's execution and indicate an error has occurred.

print("Rate from 0 to 10")
rate = 9
if rate > 10 or rate < 0:
  raise ValueError

  #ejercicio 12

rating = 15
if rating > 10 or rating < 0:
  raise ValueError("Rate from 0 to 10")
