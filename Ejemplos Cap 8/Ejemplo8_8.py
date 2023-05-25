""" Algoritmo que calcula el factorial de un número entero."""

# Función que calcula el factorial.
def factorial( n ):
    fact = 1 # Inicializa el factorial a la unidad.
    # Inicia cálculo recursivo del factorial con una condición.
    if (n > 1):
        fact = n*factorial(n - 1)
    else:
        fact = 1
                           
    return fact # Se regresa el factorial.
# Termina la función.

# INICIO DEL ALGORITMO PRINCIPAL

# Mostrar un mensaje para leer un número.
numero = int(input("Dame un número entero: "))

# Cálculo del factorial:
factor = factorial(numero)

# Se despliega el factorial.
print(" El factorial del número ", numero, " es ", factor)                   

# FIN
