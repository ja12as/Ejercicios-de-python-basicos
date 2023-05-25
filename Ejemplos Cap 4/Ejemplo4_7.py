'''Programa: Promedio de calificaciones.
   Este programa calcula el promedio de calificaciones
   de tres alumnos durante un semestre.'''

# INICIO

# DATOS DE ENTRADA:
No_est = int(input("Dame el número de alumnos:\n"))
No_califs = int(input("Dame el no. de calificaciones por alumno:\n"))

# Principio del ciclo exterior
for cont_est in range(No_est):
    # Inicializa variables del ciclo Mientras.
    Nombre_est = input("Dame el nombre del estudiante:")
    contador_calificacion = 1
    suma = 0.0

    # Principio del ciclo anidado.
    while( contador_calificacion <= No_califs):
        calificacion = float(input("Dame una calificación: "))
        suma = suma + calificacion
        contador_calificacion += 1
    # Fin del ciclo Mientras anidado.

    # Se calcula el promedio de un estudiante.
    promedio = suma/No_califs
    # Se despliega el nombre y el promedio de un estudiante.
    print("Promedio del estudiante ", Nombre_est, "es: ", promedio)

# Termina ciclo for esterior.

# FIN                      
            

