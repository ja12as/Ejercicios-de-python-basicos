""" Escritura de matriz."""

# INICIO

# Inicialización de variables.
A = [[1, -2.3, 0], [9.6, -1.5, 4], [5.7, -6.3, 3.1]]

# Inicia ciclo Para:
for i in range(3): # i es para renglones.
    print() # Este print sirve para salto de renglón.
    for j in range (3): # j es para columnas.
        print(A[i][j], "\t", end = ",") # Imprime los elementos del renglón i.
        
# FIN
