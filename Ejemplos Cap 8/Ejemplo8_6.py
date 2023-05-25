""" Algoritmo que obtiene el módulo y
    cociente de dos números enteros."""

# Función que calcula el módulo.
def modulo(a, b):
    residuo = a % b
    cociente = a // b
    print("residuo: ", residuo)
    print("cociente: ", cociente)
# Termina la función.

# INICIO DEL ALGORITMO PRINCIPAL

a = float(input("Dame el valor de a: "))
b = float(input("Dame el valor de b: "))
modulo (a, b)

# FIN
