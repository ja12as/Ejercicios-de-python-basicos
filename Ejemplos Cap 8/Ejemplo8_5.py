""" Algoritmo que despliega una lista de 20 enteros."""

# Función que dibuja una línea.
def dibujar_linea( ):
    for i in range(3):
        print("_", end = "")
    print( ) # Para salto de renglón.
# Termina la función.

# INICIO DEL ALGORITMO PRINCIPAL

for k in range(1, 21):
    print(k)
    dibujar_linea()

# FIN
