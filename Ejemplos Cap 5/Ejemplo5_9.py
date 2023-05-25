""" Buscador de caracteres.
    Busca cuántas veces el caracter 'o'
    se encuentra en la palabra 'colombiano'."""

# INICIO

# Se incializa la suma a cero.
suma = 0

# Inicia el ciclo for.
for k in "colombiano":
    if 'o' in "colombiano": # Inicia la condición.
        suma = suma + 1
    # Fin de la condición.    
# Fin del ciclo for.

# Despliegue de variables.
print("Se encuentra ", suma, " veces.")

# FIN
