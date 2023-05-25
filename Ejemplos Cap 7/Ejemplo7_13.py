""" Multiplicación de matriz por matriz."""


# INICIO

# Inicialización de variables.
a = [[3, 2, 1], [-1, -3, 0], [5, 7, 8]]
b = [[9, 0, 1], [-1, 7, 1], [6, 4, 1]]
k = 5

# Inicializa la matriz donde se almacena el resultado.
c = [[0 for i in range(3) ] for j in range(3)]

# Generar la multiplicación de a y b.
for k in range(len(a)): # Itera los renglones.
    for j in range(len(b[0])): # Itera las columnas.
        for t in range(len(b)): # Itera las columnas.
            c[k][j] += a[k][t]*b[t][j]
    
# Desplegar la matriz:
print(c)        
        
# FIN
