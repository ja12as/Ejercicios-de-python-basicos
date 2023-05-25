""" Matriz simétrica."""

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
        
# Inicializa la matriz simétrica.
A_sim = [[None for i in range(4) ] for j in range(4)]


        
# Generar la matriz simétrica.
for k in range(4): # Itera los renglones.
    for j in range(4): # Itera las columnas.
        A_sim[j][k] = A[k][j]

# Desplegar la matriz simétrica:
print("\n\nLa matriz simétricads de A es: ")
for k in range(4): # Itera los renglones.
    print()
    for j in range(4): # Itera las columnas.
        print(A_sim[k][j], end = ',\t')
                
# FIN
