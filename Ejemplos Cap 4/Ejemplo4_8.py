""" Programa: Cálculo de f(x, y, z).
    Este algoritmo calcula los
    valores de f(x, y, z) = 3x^3 + 7y^2*z."""

# INICIO

# Se inicia el ciclo for exterior.
for x in range(5):
    y = 0.3 # Se inicializa y.
    while( y <= 1.5): # Inicia el primer ciclo anidado.
        z = -1 # Se inicializa z.
        while (z <= 8):  # Inicia el segundo ciclo anidado.
            f = 3*pow(x, 3) + 7 * pow(y, 2)*z
            print("f(x, y, z) = ", f)
            z = z + 3 # Se incrementa z.
        # Fin del segundo ciclo anidado.
        y = y + 0.3 # Se incrementa y.
    # Fin del primer ciclo anidado.
# Fin del ciclo for exterior.

# FIN
            
            
