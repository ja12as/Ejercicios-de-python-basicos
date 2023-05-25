""" Algoritmo: Ordenamiento de burbuja.
    Ordena ascendentemente 100 precios
    generados aleatoriamente sin usar
    espacio adicional"""

# Se importa la biblioteca random.
import random

# INICIO

# Inicialización de variables.
x = [None]*10 # Se realiza para 10 números.
x_ord = [None]*10 #
max = 10
min = 0
hay_cambio = True

# Se genera el vector de tamaño 10 de números aleatorios.
#Inicio del ciclo for:
for indice in range(10):
    x[indice] = min + max*random.random()%(max - min + 1)
# Fin del ciclo Para.

# Ordenamiento por burbuja:
while (hay_cambio == True):
    hay_cambio = False
    for articulo in range(len(x) - 1):
        if (x[articulo] < x[articulo + 1]):
            temp = x[articulo]  #Intercambia precios.
            x[articulo] = x[articulo + 1]
            x[articulo + 1] = temp
            hay_cambio = True
# Fin del ordenamiento.

# Se despliega el vector ordenado.
print("\n\nEl vector ordenado es : \n")
for paso in range(10):
    print("%5.3f\n"  %x[paso])



# FIN
