# Calificaciones numéricas y asistencia.

# INICIO

# Recibe la calificación y la asistencia.
calificacion = float(input("Dame una calificación: "))
print("\nDame la asistencia: 1 si asistió, 0 si no asistió.")
asistencia = bool(input( ))

# Inicio de la condición:
if (calificacion > 9.0 and asistencia == 1):
    print("\nLa calificación es A Excelente con Mención Honorífica.")
elif (calificacion > 9.0 and asistencia != 1):
    print("\nLa calificación es A Excelente.")
elif(calificacion > 8.0 and asistencia == 1):
    print("\nLa calificación es B Muy Bien con Mención Honorífica.")
elif(calificacion > 8.0 and asistencia != 1):
    print("\nLa calificación es B Muy Bien.")
elif(calificacion >= 7.5):
    print("\nLa calificación es C.")
else:
    print("\nLa calificación es R.")

#Fin de la condición anidada.

#FIN
