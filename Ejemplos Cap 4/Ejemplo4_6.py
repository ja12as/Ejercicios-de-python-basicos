""" Programa: Población de una colonia de bacterias.
    Se calcula el número de días en que la población
    de una colonia de bacterias se duplica."""

# INICIO

# Inicialización de variables.
nd = 1 # Número de días.
M0 = 10 # Población de bacterias.

# Entrada de datos:
Mmax = int(input("Dame la población máxima: \n"))

# Inicio del ciclo Mientras.
while (M0 <= Mmax):
    M0 = 2*M0
    if (M0 <= Mmax): #Checa si todavía no se llega al máximo.
        nd = nd + 2 # Se incrementa el número de días en 2.
    # Fin de la condición.
# Fin del ciclo Mientras.

# Despliegue de resultados.
print("El número de días es ", nd)
print("La población de bacterias es ", M0)

# FIN
        


