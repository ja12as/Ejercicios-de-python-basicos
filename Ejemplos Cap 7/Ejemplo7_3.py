""" Generación de matriz por comprensión."""


# INICIO

# Inicialización de variables.
m = int(input("Dame el No. de renglones: "))
n = int(input("Dame el No. de columnas: "))
A = [ ]

# Genera  la matriz.
A = [[ i**2 for i in range(n)] for j in range(m)]

# Inicia ciclo Para:
for k in range(m): # k es para renglones.
    print() # Este print sirve para salto de renglón.
    for j in range (n): # j es para columnas.
        print(A[k][j], "\t", end = ",") # Imprime los elementos del renglón i.
        
# FIN
