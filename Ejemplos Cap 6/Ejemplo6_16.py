""" Algoritmo de ordenamiento por selección."""

# INICIO

# Inicialización de variables.
calif = [None]*6
calif_ord = [None]*6

# Entrada de datos:
for estudiante in range(6):
    calif[estudiante] = float(input("Dame una calificación: \n"))


# Ordenamiento por selección:
for paso in range(6):
    minima = 0
    for estudiante in range(1, 6):
        if (calif[estudiante] < calif[minima]):
            minima = estudiante
    calif_ord[paso] = calif[minima]
    calif[minima] = 11
# Fin del ordenamiento.

# Se despliega el vector ordenado.
print("\nEl orden es : \n", calif_ord)
        

# FIN
