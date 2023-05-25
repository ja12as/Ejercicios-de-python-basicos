""" Obtención de números primos."""

# Se importa la fucnión sqrt.
from math import sqrt

# Función para evaluar si un número es primo.
def primo(numero):
    # Importa la función para obtener la raíz cuadrada.
    

    es_primo = True # Suponemos que SÍ es primo.
    divisor = 2     #Se inicia el ciclo con divisor = 2. 
                        
    # Se inicia un ciclo Mientras para buscar un divisor exacto.
    while divisor <= sqrt(numero) and es_primo:
        cociente = numero//divisor # División entera.
        if (numero == cociente*divisor):
            es_primo = False # Se encontró un divisor exacto.
        else:
            divisor = divisor + 1 # Se incrementa el divisor
    return (es_primo)

# Termina la función.

# INICIO DEL ALGORITMO PRINCIPAL


# Recibe el número a checar:
n = int(input("Dame un número entero: "))

 
es_primo = primo(n)
if(es_primo):
    print("SÍ es primo")
else:
    print("NO es primo")
                
# FIN
