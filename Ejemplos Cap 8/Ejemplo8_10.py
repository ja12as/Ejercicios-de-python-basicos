""" Variables locales."""

# Función que calcula el factorial.
def f( ):
    global x
    x = x + 1 # Inicializa el valor de x.
    print(" Valor de x dentro de la función = : ", x)
                           
    return x 
# Termina la función.

# INICIO DEL ALGORITMO PRINCIPAL

# Inicializa el valor de x en el programa principal..
x = 3
print("Valor inicial de x = ", x)

# Llamado de la función f(x).
z = f( )

# Se despliega el valor de x después de llamar la función:
print(" El valor de x después de llamar la función es ", x)                   

# FIN
