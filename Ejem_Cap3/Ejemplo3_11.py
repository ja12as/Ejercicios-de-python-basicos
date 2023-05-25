# Ecuación de primer grado.

#INICIO

# Entrada de datos:
a = float(input("Dame a: \n"))
b = float(input("Dame b: \n"))

# Condición
if ( a != 0):
    x = -b/a
    print("Resultado: ", x)
else:
    if ( b == 0):
        print("a = 0 y b = 0")
    else:
        print("No hay solución")
    # Fin del if anidado.
# Fin del if inicial.

#FIN
