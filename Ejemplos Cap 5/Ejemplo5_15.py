""" Ejemplos con listas."""

# INICIO

# Inicialización de variables.
a = ["Pedro", 555,  "Python", "Intel", "HP"]
b = [45, -67.8,  999.99, -2702.2, 1858]
c = ["mouse", "teclado"]


# Longitud de una lista.
la = len(a)
print("\nEl tamaño de a es: ", la)


# Máximo de una lista.
Mb = max(b)
print("\nEl máximo de b es: ", Mb)

# Mínimo de una lista.
mb = min(b)
print("\nEl mínimo de b es: ", mb)

# Añadir un elemento a una lista.
a.append(-2015)
print("\nLa lista a es: ", a)

# Extender la lista a con la lista c.
a.extend(c)
print("\nLa lista a extendida con c es: ", a)


# Insertar 47 en la posición 2 de la lista b.
b.insert(2, 47)
print("\nLa lista b con 47 en la pos. 2 es: ", b)

# Extrae el elemento en la posición 3 de la lista b.
d = b.pop(3)
print("\nEl elemento en la posición 3 de la lista b es: ", d)

# Extrae el último elemento de la lista b.
d = b.pop()
print("\nEl último elemento de la lista b es: ", d)


# Borra el elemento en la posición 0 de la lista b.
print("\nLa lista b es: ", b)
b.remove(45)
print("\nLa lista b sin el primer elemento es: ", b)

# Invierte el orden de los elementos de la lista a.
print("\nLa lista a es: ", a)
a.reverse()
print("\nLa lista a con elementos invertidos es: ", a)

# Ordena  los elementos de la lista b.
print("\nLa lista b es: ", b)
b.sort()
print("\nLa lista b con elementos ordenados es: ", b)

# FIN
