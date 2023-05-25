""" Algoritmo que calcula el factorial de un número entero."""

# Función que calcula el factorial.
def factorial( n ):
    fact = 1 # Inicializa el factorial a la unidad.
    # Inicia ciclo for para el cálculo del factorial de n,
    for k in range(2, n + 1):
        fact = fact*k
    # Fin del ciclo for.
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
