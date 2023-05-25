""" Calcula 10 números aleatorios.
    No se declara el tamaño del vector."""

# Se importa la biblioteca random.
import random

# INICIO

# Inicialización de variables.
x = [ ]
lim_sup = 100
lim_inf = 50

# Se genera el vector de tamaño 10 de números aleatorios.
#Inicio del ciclo for:
for indice in range(10):
    x += [ lim_inf + lim_sup*random.random()%(lim_sup - lim_inf + 1) ]
# Fin del ciclo Para.
    

# Se imprime el vector:
for indice in range(10):
    print("\n", x[indice])


# FIN
