""" Algoritmo que realiza una triple sumatoria."""

# INICIO

# Se inicia el ciclo for exterior.
S = 0 # Se inicializa la suma a cero.

# Inician los ciclos anidados.
for i in range(11): # Ciclo exterior.
    for j in range(5, 10): # Primer ciclo anidado.
        for k in range(-1, 8): # Segundo ciclo anidado.
             # Cálculo de la sumatoria.
             S = S + i*j*k
             # Fin del segundo ciclo anidado para k.
        # Fin del primer ciclo anidado para j.
# Fin del ciclo for exterior para i.

# Se le suma 23 a la suma.
S = S + 23

# Se despliega el valor de S.
print("El valor de S es: ", S)

# FIN
            
            
