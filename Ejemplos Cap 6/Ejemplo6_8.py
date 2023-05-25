""" Calcula 10 números aleatorios."""

# Se importa la biblioteca random.
import random

# INICIO

# Inicialización de variables.
x = [None]*10 # Se realiza para 10 números.

# Se genera el vector de tamaño 10 de números aleatorios.
#Inicio del ciclo for:
for indice in range(10):
    x[indice] = random.random()
# Fin del ciclo Para.
    

# Se imprime el vector:
for indice in range(10):
    print("\n", x[indice])


# FIN
