""" Multiplicación de matriz por escalar."""


# INICIO

# Inicialización de variables.
a = [[2, -1, 7, 3], [12, -26, 4, -8], [4, -5, 6, 7]]
k = 5

# Inicializa la matriz donde se almacena el resultado.
R = [[None for i in range(4) ] for j in range(3)]

# Generar la multiplicación de a y k.
for renglones in range(len(a)): # Itera los renglones.
    for columnas in range(len(a[0])): # Itera las columnas.
        R[renglones][columnas] = k*a[renglones][columnas]
    
# Desplegar la matriz:
print(R)        
        
# FIN
