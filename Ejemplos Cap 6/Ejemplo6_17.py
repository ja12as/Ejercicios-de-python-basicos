""" Calcula 10 números aleatorios
    y los ordena por selección."""

# Se importa la biblioteca random.
import random

# INICIO

# Inicialización de variables.
x = [None]*10 # Se realiza para 10 números.
x_ord = [None]*10 #
max = 10
min = 0

# Se genera el vector de tamaño 10 de números aleatorios.
#Inicio del ciclo for:
for indice in range(10):
    x[indice] = min + max*random.random()%(max - min + 1)
# Fin del ciclo Para.
    

# Se imprime el vector:
for indice in range(10):
    print("\n", x[indice])


# Ordenamiento por selección:
for paso in range(10):
    minima = 0
    for estudiante in range(1, 10):
        if (x[estudiante] < x[minima]):
            minima = estudiante
    x_ord[paso] = x[minima]
    x[minima] = 11
# Fin del ordenamiento.

# Se despliega el vector ordenado.
print("\n\nEl vector ordenado es : \n")
for paso in range(10):
    print("\n", x_ord[paso])



# FIN
