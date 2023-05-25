'''Algoritmo para calcular números aleatorios
   entre 0 y 20.'''

# Importa la biblioteca random.
import random

# INICIO

# Inicializa las variables.
num = [ ]

# Principio del ciclo for.
for i in range(10):
    n = random.randint(0, 20) # Genera número aleatorio entre 0 y 20.
    num.append(n) # Lo añade a la lista num.
# Termina ciclo for.

# Despliega el resultado:
print( num ) 

# FIN                      
            

