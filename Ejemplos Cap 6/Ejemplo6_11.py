""" Varianza y desviación estandar."""

# Se importan la función necesaria.
from math import sqrt

# INICIO

# Inicialización de variables.
suma = 0
vector = [None]*5
var = 0

# Lee el vector y realiza la suma.
#Inicio del ciclo for:
for contador in range(5):
    vector[contador] = int(input("Dame un elemento: \n"))
    # Realiza la suma:
    suma = suma + vector[contador]
# Fin del ciclo Para.
    
# Calcula el promedio.
promedio = suma/5

# Calcula la varianza:
for k in range(5):
    var = var + pow(vector[k] - promedio, 2)

varianza = var/5

# Calcula desviación estandar:
desv = sqrt(varianza)

# Se imprimen los resultados:
print("\nPromedio\t Varianza\t Desviación estandar\n")
print(promedio, "\t\t", varianza, "\t\t", desv)


# FIN
