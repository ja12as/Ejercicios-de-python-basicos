""" Búsqueda binaria."""

# Se importa la biblioteca random.
import random

# INICIO

# Inicialización de variables.
n = 9 # Tamaño del vector
vector = [None]*n # Se realiza para 10 números.
vector_ord = [None]*n #
max = n
min = 0

# Se genera el vector de tamaño 10 de números aleatorios.

#Inicio del ciclo for:
for indice in range(n):
    vector[indice] = random.randint(min, max)
# Fin del ciclo Para.
    

# Se imprime el vector:
for indice in range(n):
    print("\n", vector[indice])

# Se ordena el vector:
for paso in range(n):
    minima = 0
    for k in range(1, n):
        if (vector[k] < vector[minima]):
            minima = k
    vector_ord[paso] = vector[minima]
    vector[minima] = n + 1
# Fin del ordenamiento.
# Se despliega el vector ordenado.
print("\n\nEl vector ordenado es : \n")
for paso in range(n):
    print("\n", vector_ord[paso])


# Se pregunta cuál número se desea buscar.
print("\nDame el número a buscar: \n")
numero_buscado = int(input())

# Inicia la búsqueda binaria:
primero = 0
ultimo = n - 1
medio = (primero + ultimo)//2
print("\nMedio",medio)
while (primero <= ultimo):
    medio = (primero + ultimo)//2
    if (vector_ord[medio] == numero_buscado):
        donde = medio
        primero = n + 1
        print("vector_ord[medio] == numero_buscado")
        
    elif (vector_ord[medio] > numero_buscado):
        ultimo = medio -1

        
    else:
        primero = medio + 1

if ( primero == n+1):
    print("\nNúmero  encontrado en la posicion", donde)
else:
    print("NO Se encontró.")
        
# FIN
