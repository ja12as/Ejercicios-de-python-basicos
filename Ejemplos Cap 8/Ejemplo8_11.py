""" Tiro de un dado."""

# Función que calcula el factorial.
def dado( ):
    from random import randint
    global numero
    numero = randint(1, 6)
    print("El dado sale: ", numero)
     
# Termina la función.

# INICIO DEL ALGORITMO PRINCIPAL

dado()                

# FIN
