'''Este algoritmo calcula el número
   de vocales en una frase'''

# INICIO

frase = "El perro corre despacio" # Frase a analizar.
base = "aeiouAEIOU" # Las vocales mayúsculas y minúsculas.
cuenta = 0 # Inicialización del contador.

# Inicio del ciclo Para:
for i in frase: # Para cada caracter en la frase.
    if i in base: # Checa si el caracter está en la base.
        cuenta = cuenta + 1 # Si aparece en la frase incrementa el contador.
# Fin del ciclo Para.

# Despliega el resultado.
print("El número de vocales en la frase es: ", cuenta)

# FIN
