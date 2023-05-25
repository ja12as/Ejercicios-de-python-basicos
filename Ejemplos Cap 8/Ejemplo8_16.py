""" Obtención de la serie de Taylor."""

# Función que calcula el factorial.
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact*i
    # Regresa el factorial.
    return fact
     
# Termina la función.

# INICIO DEL ALGORITMO PRINCIPAL

# Datos iniciales.
# Se recibe el valor de x.
x = float(input("Dame el valor de x: "))
S = 0

# Se calcula la serie para el seno de x.
for i in range(10):
    S = S + pow(-1, i)*pow(x, (2*i + 1))/factorial(2*i + 1)

# Se despliega el valor de la serie para sen(x).
print("El valor de la serie es: ", S)             

# FIN
