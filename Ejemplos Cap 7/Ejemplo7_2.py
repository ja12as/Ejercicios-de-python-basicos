""" Generación de matriz.
    Este algoritmo genera una matriz de m x n."""


# INICIO

# Inicialización de variables.
m = int(input("Dame el No. de renglones: "))
n = int(input("Dame el No. de columnas: "))
A = [ ]

# Genera los renglones:
# Inicia ciclo Para:
for i in range(m): # i es para renglones.
    A.append([ ]) 
    for j in range (n): # j es para columnas.
        A[i].append([None]) # Genera los elementos del renglón i.

# Impresión de la matriz.
# Inicia ciclo Para:
for k in range(m): # k es para renglones.
    print() # Este print sirve para salto de renglón.
    for j in range (n): # j es para columnas.
        print(A[k][j], "\t", end = ",") # Imprime los elementos del renglón i.
        
# FIN
