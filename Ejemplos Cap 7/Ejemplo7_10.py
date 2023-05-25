""" Suma de matrices."""


# INICIO

# Inicialización de variables.
a = [[3, 2, 1, 9], [-1, -3, 0, 8], [5, 7, 8, 7]]
b = [[9, 0, 1, 3], [-1, 7, 1, 4], [6, 4, 1, 6]]

# Inicializa la matriz donde se almacena el resultado.
c = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# Generar la suma de a y b.
for i in range(len(a)): # Itera los renglones.
    for j in range(len(a[0])): # Itera las columnas.
        c[i][j] = a[i][j] + b[i][j] 
    
# Desplegar un renglón de la matriz:
print(c)        
        
# FIN
