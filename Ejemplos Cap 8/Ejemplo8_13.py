""" Regreso de varias variables."""

# Función que modifica los datos.
def modificar(a, b, c):
    a = a + 3
    b = b + 3
    c = c + 3
    suma = a + b + c

    # Regresa a y la suma.
    return a, suma
     
# Termina la función.

# Función que despliega el resultado.
def escribir (suma):
    print("La suma es: ", suma)
     
# Termina la función.

# INICIO DEL ALGORITMO PRINCIPAL

# Datos iniciales:
a = 1; b = 2.3; c = 7.1
[suma, a] = modificar(a, b, c)
# Se despliega la suma:
escribir(suma)
# Se Muestra el valor de a.
print("El valor de a es: ", a)                

# FIN
