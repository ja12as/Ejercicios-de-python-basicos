""" Algoritmo palíndromos.
    Determina si una frase es palíndromo."""

# Se importa la función ceil.
from math import ceil

# INICIO

# Inicialización de variables.
numero = 0
contador = 0
letra = [ ]

# Lee la frase.
max = int(input("\nDame el número de letras:\n"))
#Inicio del ciclo while de lectura de la frase:
while (numero <= max - 1):
    print("\nDame una letra de la frase: ")
    letra += [input( )]
    numero += 1
# Fin del ciclo while.

# Analiza la frase desde el final:
inverso = max
numero = 0
frase = [None]*max

# Invierte la frase.
#Inicia ciclo while.
while (numero <= max - 1):
    frase[inverso - 1] = letra[numero]
    inverso -= 1
    numero += 1
# Fin del ciclo while.
    
# Compara la frase original con la invertida.
numero = 0
contador = 0
while (numero <= ceil(max/2)):
    if (frase[numero] == letra[numero]):
        contador += 1
    numero += 1

if (contador == ceil(max/2) + 1):
    print("La frase SÍ es palíndromo.")
else:
    print("La frase NO es palíndromo.")

# FIN
