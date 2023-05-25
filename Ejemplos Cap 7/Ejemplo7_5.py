""" Iterador de listas.
    Forma alterna."""


# INICIO

# Inicialización de variables.
matriz = [[-1, 0, -10], [3, 4, 0.5], [6, -23, 8], [7, 3, 9]]


# Desplegar la matriz:
# Inicia ciclo Para:
for renglon in matriz: # Selecciona los renglones.
    print( ) # Salto de renglón.
    for c in renglon: # Selecciona las columnas.
        print(c, end = " ,\t ")        
        
# FIN
