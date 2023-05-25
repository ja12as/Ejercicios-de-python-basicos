""" Matriz transpuesta."""

# Importa la biblioteca de números aleatorios.
import random

# INICIO

# Inicializa la matriz con números aleatorios.
A = [[random.randint(-10, 10) for i in range(4) ] for j in range(4)]

# Desplegar la matriz A:
print("\nLa matriz A es: ")
for k in range(4): # Itera los renglones.
    print()
    for j in range(4): # Itera las columnas.
        print(A[k][j], end = ',\t')
        
# Inicializa la matriz transpuesta.
A_trans = [[None for i in range(4) ] for j in range(4)]


        
# Generar la matriz transpuesta.
for k in range(4): # Itera los renglones.
    for j in range(4): # Itera las columnas.
        A_trans[j][k] = A[k][j]

# Desplegar la matriz transpuesta:
print("\n\nLa matriz transpuesta de A es: ")
for k in range(4): # Itera los renglones.
    print()
    for j in range(4): # Itera las columnas.
        print(A_trans[k][j], end = ',\t')
                
# FIN
