""" Ejemplos usando diccionarios."""

# INICIO

# Inicialización de variables.
cosas = {"M" : "manzana", "P" : "plátano", "L" : "limón" }
print("\nDiccionario cosas = ", cosas)

# Convertir diccionario a cadena.
cadena = str(cosas) 
print("\nLa cadena es: ", cadena)


# Regresa el tipo.
tipo = type(cadena)
print("\nEl tipo de cadena es: ", tipo)
tipo = type(cosas)
print("\nEl tipo de cosas es: ", tipo)

#Copia el diccionario en otra variable.
frutas = cosas.copy()
print("\nfrutas es: ", frutas)

# Crea un nuevo diccionario a partir de una lista.
lista = [1, 2, 3, 6, 9]
tres = cosas. fromkeys('lista', 2)
print("\nEl nuevo diccionario es: ", tres)

# Obtiene el diccionario como pares.
pares = cosas. items()
print("\nLos pares son: ", pares)

# Obtiene la lista de los valores del diccionario.
tres = cosas. values()
print("\nLos valores del diccionario son: ", tres)



# FIN
