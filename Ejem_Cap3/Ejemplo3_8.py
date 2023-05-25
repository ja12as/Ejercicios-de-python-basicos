# Ecuación de segundo grado.
# Se importa la biblioteca math
from math import *

# INICIO

a = float(input("\nDame a: "))
b = float(input("\nDame b: "))
c = float(input("\nDame c: "))

# Calcular discriminante:
d = pow(b, 2) - 4*a*c

# Calcular raíces:
if (d > 0):
    print("\nRaíces reales y diferentes")
    x1 = (-b + sqrt(d))/2/a
    x2 = (-b - sqrt(d))/2/a
    print("\nLa primera raíz es ", x1)
    print("\nLa segunda raíz es ", x2)
# Fin de la condición

if (d == 0):
    print("\nRaíces reales e iguales")
    x1 = -b/2/a
    x2 = x1
    print("\nLa primera raíz es ", x1)
    print("\nLa segunda raíz es ", x2)
# Fin de la condición.

if (d < 0):
    print("\nRaíces complejas conjugadas")
    x1_parte_real = -b/2/a
    x1_parte_imaginaria = sqrt(-d)/2/a
    x2_parte_real = x1_parte_real
    x2_parte_imaginaria = -x1_parte_imaginaria
    print("\nLa primera raíz es ", x1_parte_real," + j ", x1_parte_imaginaria)
    print("\nLa segunda raíz es ", x2_parte_real, " - j ", -x2_parte_imaginaria)
# Fin de la condición

#FIN

    
