""" Obtención de las raíces de una ecuación de segundo grado."""

# Se importa la fucnión sqrt.
from math import sqrt

# Función para calcular la raíz cuadrada del discriminante.
def discriminante(a1, b1, c1):
    d = sqrt(b1*b1 - 4*a1*c1)
    return d
# Termina la función.

# INICIO DEL ALGORITMO PRINCIPAL


# Recibe los coeficientes:
a = float(input("Dame el coeficiente de x**2: "))
b = float(input("Dame el coeficiente de x: "))
c = float(input("Dame el coeficiente independiente: ")) 

# Se calcula el discriminante:
d1 = discriminante(a, b, c)

# Se calculan las raíces:
x1 = (-b + d1)/2/a
x2 = (-b - d1)/2/a

# Se despliegan las raíces:
print("La primera raíz es: ", x1)
print("La segunda raíz es: ", x2)

# FIN
