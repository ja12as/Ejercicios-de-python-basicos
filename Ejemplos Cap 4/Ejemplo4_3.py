'''Evalúa si un entero positivo es primo.
   Se usa una variable lógica.'''

# Se importa la biblioteca de matemáticas.
from math import *

# INICIO

# Numero a evaluar:
n = int(input("Número a evaluar?  "))

# Inicializa el divisor:

divisor = 2 # Se inicializa en 2 y se llegará hasta raiz cuadrada de n,
            # a menos de que se encuentre que no es primo.
es_primo = True # Variable lógica. Se cambia a False si ni es primo.

# Inicia ciclo Mientras:
while (divisor <= sqrt(n) and es_primo):
    cociente = n//divisor # Verifica con cada divisor posible.
    if ( n == cociente*divisor ):
        es_primo = False # n no es primo.
    else:
        divisor = divisor + 1 # Se incrementa divisor y se sigue la búsqueda.
                              # Tal vez sea primo, verificar siguiente.
    # Fin de la condición
# Fin del ciclo Mientras

# Impresión de resultados:
if (es_primo): # Se encontró un divisor exacto.
    print("SÍ es primo")
else:
    print("NO es primo")

# FIN
    
   
