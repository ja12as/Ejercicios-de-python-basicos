'''Algoritmo para seleccionar números impares
y terminar al encontrar el primero divisible por 5.
   Se usa la instrucción break'''

# INICIO

# Principio del ciclo for.
for x in range(1, 100):
    # Inicializa condición.
    if (not(x%2) and (x%5)): # Checa si hay residuo y divisible por 5.
        continue
    if (x%5 == 0): # Checa si es divisible por 5.
        break
    print( x, '\n') # Sólo imprime los impares.

# Termina ciclo for.

# FIN                      
            

