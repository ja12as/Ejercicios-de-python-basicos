# Se importa la biblioteca de matemáticas.
from math import *

# INICIO

# Numero a evaluar:
n = int(input("Número a evaluar?  "))

# Inicializa el divisor:

divisor = 2 # Se inicializa en 2 y se llegará hasta raiz cuadrada de n,
            # a menos de que se encuentre que no es primo.

# Inicia ciclo Mientras:
while (divisor <= sqrt(n)):
    cociente = n//divisor # Verifica con cada divisor posible.
    if ( n == cociente*divisor ):
        divisor = n + 1 # n no es primo.
    else:
        divisor = divisor + 1 # Se incrementa divisor y se sigue la búsqueda.
                              # Tal vez sea primo, verificar siguiente.
    # Fin de la condición
# Fin del ciclo Mientras

# Impresión de resultados:
if (divisor > n): # Se encontró un divisor exacto.
    print("NO es primo")
else:
    print("SÍ es primo")

# FIN
    
