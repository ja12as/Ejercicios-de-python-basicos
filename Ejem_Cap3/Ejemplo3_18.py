# Calculadora básica con menú.

# Se importa la biblioteca math:
from math import log

# INICIO
bandera = False
x = float( input("\nDame el valor del número x: "))
y = float( input("\nDame el valor del número y: "))
print("\nDame la opción que deseas realizar:\n")

# Se despliega el menú para seleccionar la opción que deseas realizar:
print(" 1) Sumar ( El primero más el segundo)")
print(" 2) Restar ( El primero más el segundo)")
print(" 3) Multiplicar ( El primero más el segundo)")
print(" 4) Dividir ( El primero más el segundo)")
print(" 5) Potencia ( El primero más el segundo)")
print(" 6) Logaritmo ( El primero más el segundo)")

opcion = int(input( ))

# Empieza la ejecución del menú con condiciones anidadas.
if (opcion == 1):
    z = x + y
    print(x, "+", y)
elif (opcion == 2):
    z = x - y
    print(x, "-", y)
elif (opcion == 3):
    z = x * y
    print(x, "*", y)
elif (opcion == 4 and y != 0):
    z = x / y
    print(x, "/", y)
elif (opcion == 4 and y == 0):
    print("\nEl denominador es igual a cero y")
    print("\nNO se puede realizar la división.")
    bandera = True
elif (opcion == 5):
    z = pow(x, y)
    print(x, "^", y)
elif (opcion == 6 and x > 0):
    z = log(x)
    print("logaritmo de ", x)
elif (opcion == 6 and x < 0):
    print("\nEl valor de x es <= 0 y")
    print("\nNO se puede calcular el logaritmo.")
    bandera = True
else:
    print("Opción desconocida.")
# Se terminan las condiciones anidadas.

# Se escribe el resultado con otra condición:
if (opcion < 7 and bandera == False):
    print("Resultado = ", z)

# FIN
