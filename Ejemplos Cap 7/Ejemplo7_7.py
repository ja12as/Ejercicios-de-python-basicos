""" Selección de columnas."""


# INICIO

# Inicialización de variables.
A = [[9, 12, 1, 44], [16, 7, 2, 14], [2, 3, 1, 8], [2, -5, -6, 0]]
b = [ ]
k = int(input("Dame la columna que deseas obtener: "))

# Generar la lista con el renglón.
for i in range(len(A)):
    b.append(A[i][k])
    
# Desplegar un renglón de la matriz:
print(b)        
        
# FIN
