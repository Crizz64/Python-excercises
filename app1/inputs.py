# Convertir los valores en números
wins = int(input())
ties = int(input())

# 1 victoria = 3 puntos
# 1 empate = 1 punto
# Calcular la puntuación
score = wins * 3 + ties

# Concatenar las 2 cadenas para producir un mensaje
message = "Score: " + str(score)

# Mostrar el mensaje
print(message)


