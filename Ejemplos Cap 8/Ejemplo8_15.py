""" Obtención del perímetro de un triángulo."""

# Función que calcula la distamcia entre dos puntos.
def dist(p1, p2):
    distancia = sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)  
    # Regresa la distancia.
    return distancia
     
# Termina la función.

# Función que lee las coordenadas.
def leer_coordenadas(i):
    p = [ ] # Inicializa el vector.
    print("Dame la coordenada x del punto ", i)
    x = float(input( ))
    p.append(x)
    print("Dame la coordenada y del punto ", i)
    y = float(input( ))
    p.append(y)
   
    return p # se regresan las coordenadas de un punto.    
# Termina la función.




# INICIO DEL ALGORITMO PRINCIPAL
from math import sqrt
# Datos iniciales. Se leen las coordenadas de los puntos A, B, C.
A = leer_coordenadas(1)

B = leer_coordenadas(2)
C = leer_coordenadas(3)

# Se calcula el perímetro.
perimetro = dist(A, B) + dist(B, C) + dist(C, A)

# Se despliega el perímetro.
print("El perímetro es: ", perimetro)             

# FIN
