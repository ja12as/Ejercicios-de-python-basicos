'''Programa: Promedio de calificaciones mejorado.
   Este programa lee las calificacones de alumnos y
   calcula el promedio del semestre y el
   porcentaje de aprobados.'''

# INICIO

# DATOS DE ENTRADA:
No_est = int(input("Dame el número de alumnos:\n"))

# Principio del ciclo exterior
for cont_est in range(No_est):
    # Inicializa variables del ciclo Mientras.
    Nombre_est = input("Dame el nombre del estudiante:")
    contador_calificacion = 0
    suma = 0

    # Principio del ciclo anidado donde se leen las calificaciones.
    # Al menos la primera calificación debe ser >= 0.
    calificacion = float(input("Dame una calificación: "))
    
    while( calificacion > 0):       
        suma = suma + calificacion
        contador_calificacion += 1
        calificacion = float(input("Dame una calificación: "))
    # Fin del ciclo Mientras anidado.
    print("suma ", suma, " contador_calificacion ", contador_calificacion)
    # Se calcula el promedio de un estudiante.
    promedio = suma/contador_calificacion
    # Se despliega el nombre y el promedio de un estudiante.
    print("Promedio del estudiante ", Nombre_est, "es: ", promedio)

# Termina ciclo for esterior.

# FIN                      
            

