#ejercicio 1
products = ["apples", "oranges", "bananas"]
products[2] =  "lime"
print(products[2])

#ejercicio 2
words = ["rise", "sun", "glasses"]
print(words[1] + words[0])

#El rebanado te permite extraer una porción de una lista.
# Los índices de inicio y fin están separados por dos puntos : 

#ejercicio 3

animals =["cat", "dog", "bird", "cow"]
print(animals[1:4])


#ejercicio 4

animals = ["cat", "dog", "bird", "cow"]
print(animals[-1]) # Último elemento
print(animals[-2]) # Penúltimo elemento
print(animals[-3:]) # Últimos 3 elementos
print(animals[-3:-1]) # Desde el antepenúltimo hasta el penúltimo elemento



#len() es una de las funciones incorporadas más útiles.

 #len() significa longitud y, cuando se utiliza en listas, devuelve el número de elementos en la lista.

movies = ["Avatar", "Titanic", "Avengers"]
print(len(movies))



#La función append() agrega un nuevo elemento al final de una lista.
#append() se llama utilizando la notación de punto porque es específica de las listas

songs = ["Yesterday", "Hello", "Believer"]
songs.append("Imagine")
print(songs)