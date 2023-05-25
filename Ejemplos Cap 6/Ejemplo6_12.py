""" Promedio de calificaciones."""

# INICIO

# Inicialización de variables.
suma = 0
notas = [None]*20

# Lee el número de alumnos y el vector.
N = int(input("\nNúmero de alumnos?\n"))
#Inicio del ciclo for:
for i in range(N):
    print("\nAlumno ", i + 1, "Nota: ")
    notas[i] = float(input( ))
# Fin del ciclo Para.

# Realiza la suma:
for i in range(N):
    suma = suma + notas[i]
# Fin del ciclo Para.
    
# Calcula la media.
media = suma/N

# Se imprimen los resultados:
print("\nNota media: ", media)

# Inicio ciclo Para:
for i in range(N):
    print("\nAlumno número:", i + 1, "Nota :", notas[i])
# Fin del ciclo Para.



# FIN
