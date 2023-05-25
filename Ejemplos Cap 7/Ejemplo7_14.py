""" Matriz identidad."""


# INICIO

# Inicializa la matriz con ceros.
I = [[0 for i in range(4) ] for j in range(4)]

# Generar la matriz identidad.
for k in range(4): 
    I[k][k] = 1
    
# Desplegar la matriz:
for k in range(4): # Itera los renglones.
    print()
    for j in range(4): # Itera las columnas.
        print(I[k][j], end = ', ')
                
# FIN
