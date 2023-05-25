""" Suma de matrices."""


# INICIO

# Inicialización de variables.
a = [[7, 3], [2, -6], [6, 7]]
b = [[1, 2], [9, -5], [-4, 7]]

# Inicializa la matriz donde se almacena el resultado.
c = [[0, 0], [0, 0], [0, 0]]


# Generar la suma de a y b.
for i in range(len(a)): # Itera los renglones.
    for j in range(len(a[0])): # Itera los renglones.
        c[i][j] = a[i][j] + b[i][j]
    
# Desplegar un renglón de la matriz:
print(c)        
        
# FIN
