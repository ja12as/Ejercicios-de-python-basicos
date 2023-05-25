""" Tiros de dados."""

# Importa la biblioteca de números aleatorios.
import random

# INICIO

# Inicializa las matrices.
tabla = [ ]
min = 1
max = 6


# Se genera la matriz de tiros:
for r in range(3): # Itera los renglones.
    tabla.append([ ])
    for t in range(5): # Itera las columnas.
        tabla[r].append(random.randint(min, max))

# Se despliega la tabla de tiros:
print("\nLa matriz de tiros es: ")
for k in range(3):
    print()
    for j in range(5):
        print("\t",tabla[k][j], end = "")
        
# Se inicializa el valor de la suma y se calcula la misma:
for r in range(3): # Itera los renglones.
    tabla[r].append(0) # Se inicializa el valor de la suma
    for t in range(5): # Itera las columnas.
        tabla[r][5] = tabla[r][5] + tabla[r][t]

# Se despliega la tabla de tiros con la suma de los tiros.
print("\n\n")
for k in range(3):
    print()
    for j in range(6):
        print("\t",tabla[k][j], end = "")


# Se cuenta cuántas veces se obtuvo un 6:
vez = [0, 0, 0] # Inicialización del vector.
for r in range(3): # Itera los renglones.
    for t in range(5): # Itera las columnas.
        if tabla[r][t] == 6:
            vez[r] = vez[r] + 1
        
# Se despliega cuántas veces sale el 6:
for r in range(3): # Itera los renglones.
    print("\n")
    if vez[r] == 1 :
        print("\nEl jugador ", r + 1, " obtuvo 6 una vez.")
        print("La suma de puntos fue de: ", tabla[r][5])
    elif vez[r] >= 2 :
        print("El jugador ", r + 1, " obtuvo 6 ", vez[r], " veces.")
        print("La suma de puntos fue de: ", tabla[r][5])
    elif vez[r] == 0 :
        print("El jugador ", r + 1, " NO obtuvo 6.")
        print("La suma de puntos fue de: ", tabla[r][5])


                
# FIN
