""" Matriz transpuesta por comprensión."""

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
        
# Generar la matriz transpuesta por comprensión.
A_trans = [[renglon[i] for renglon in A ] for i in range(len(A[0]))]

# Desplegar la matriz transpuesta:
print("\n\nLa matriz transpuesta de A es: ")
for k in range(4): # Itera los renglones.
    print()
    for j in range(4): # Itera las columnas.
        print(A_trans[k][j], end = ',\t')
                
# FIN
